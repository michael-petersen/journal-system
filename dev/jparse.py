#
# parser for .jrn files
#

# python imports
import os
import glob
import time


def parse_journal_files(journal_directory):
    '''
    do the basic journal parsing

    make calendar dictionary


    '''
    jrnls = glob.glob(journal_directory+'*.*jrn')
    CalDict = {}
    for raw_x in jrnls:
        extension = raw_x.rpartition('.')[-1][0]
        x     = raw_x.rpartition('/')[-1]
        yrx       = str(x[4:6])
        mox       = str(x[0:2])
        dax       = str(x[2:4])
        # check year
        if '20'+yrx not in CalDict.keys():
            # make the months dictionary

            CalDict['20'+yrx] = {}
            
        # move on to months
        if mox not in CalDict['20'+yrx].keys():
            
            # make the days list
            CalDict['20'+yrx][mox] = {}

        if dax not in CalDict['20'+yrx][mox].keys():

            # make the sub-days list (for multiple-entry days
            sub_day_num = -1
            CalDict['20'+yrx][mox][dax] = {}

        # now that all possible dictionaries have been opened, populate
        sub_day_num += 1
        
        if str(extension[0])=='j':
            # raw journal files
            CalDict['20'+yrx][mox][dax][sub_day_num] = 0
            
        elif str(extension[0])=='a':
             # supplemental notes
            CalDict['20'+yrx][mox][dax][sub_day_num] = 1
            
        elif str(extension[0])=='c':
            # colloquium notes
            CalDict['20'+yrx][mox][dax][sub_day_num] = 2
        else:
            # catchall in case of unexpected extension
            print 'File extension not supported, skipping file:',x

    return jrnls,CalDict




def generate_calendar_html(CalDict,journal_directory='./'):
    '''
    generate a calendar by marching through years, months, days

    '''
    jorder = []
    c_increment = -1
    CalPrint = {}
    years = ['2017','2016','2015','2014','2013']
    months = ['%02i'%i for i in range(12,0,-1)]
    days = ['%02i'%i for i in range(32,0,-1)]
    #
    for y in years:
        #print y
        # check if year exists
        if y in CalDict.keys():
            c_increment += 1
            CalPrint[c_increment] = '<div class=\"row\" id=\"cal-year\">'+y+'</div>'
            #print '<div class=\"row\" id=\"cal-year\">'+y+'</div>'
            # now open months
            for m in months:
                if m in CalDict[y].keys():
                    c_increment += 1
                    CalPrint[c_increment] = '<div class=\"row\" id=\"cal-month\"><span>'+month_trans[m]+'</span>'
                    #print '<div class=\"row\" id=\"cal-month\"><span>'+month_trans[m]+'</span>'
                    # now open days
                    for d in days:
                        if d in CalDict[y][m].keys():
                            # cycle through sub-days:
                            for sd in CalDict[y][m][d].keys():
                                c_increment += 1
                                if CalDict[y][m][d][sd] == 0:
                                    CalPrint[c_increment] ='<a href=\"#'+m+d+y+'\"><span class=\"cal-day\">'+d+'</span></a>'
                                    jorder.append(journal_directory+m+d+str(y)[2:4]+'.jrn')
                                if CalDict[y][m][d][sd] == 2:
                                    CalPrint[c_increment] ='<a href=\"#'+m+d+y+'\"><span class=\"cal-daycolloq\">'+d+'</span></a>'
                                    jorder.append('./'+m+d+str(y)[2:4]+'.cjrn')
                                if CalDict[y][m][d][sd] == 1:
                                    CalPrint[c_increment] ='<a href=\"#'+m+d+y+'\"><span class=\"cal-dayalt\">'+d+'</span></a>'
                                    jorder.append('./'+m+d+str(y)[2:4]+'.ajrn')
                            #print '<a href=\"#'+m+d+y+'\"><span class=\"cal-day\">'+d+'</span></a>'
                            
                    c_increment += 1
                    CalPrint[c_increment] = '</div>'
    return CalPrint,jorder



# these are purely cosmetic.
month_trans = {'01':'January',\
               '02':'February',\
               '03':'March',\
               '04':'April',\
               '05':'May',\
               '06':'June',\
               '07':'July',\
               '08':'August',\
               '09':'September',\
               '10':'October',\
               '11':'November',\
               '12':'December'}


day_ending = {'01':'st',\
          '02':'nd',\
          '03':'rd',\
          '21':'st',\
          '22':'nd',\
          '23':'rd',\
          '31':'st'}



# first, parse the filename

def parse_jrn_name(jrn_name):
    '''

    helper to convert the filename into useful items for the machine
    
    '''

    # strip any leads
    jrn_name = jrn_name.rpartition('/')[-1]
    
    yr = '20'+str(jrn_name[4:6])
    
    mo = month_trans[str(jrn_name[0:2])]
    
    # check day ending. this piece is purely cosmetic
    ender = 'th'
    
    if str(jrn_name[2:4]) in day_ending.keys():
        ender = day_ending[str(jrn_name[2:4])]
        
    da = str(jrn_name[2:4])+ender
    id_string = jrn_name[0:4]+'20'+jrn_name[4:6]
    
    return id_string,'<div class=\"title2\" id=\"'+id_string+'\"><h3>'+mo+' '+da+', '+yr+'</h3>'




def parse_date_today():
    '''

    return a formatted version of today's date.
    
    '''
    time.strftime("%m%d20%y")
    yr = '20'+time.strftime("%y")
    mo = month_trans[time.strftime("%m")]
    # check day ending
    ender = 'th'
    if time.strftime("%d") in day_ending.keys():
        ender = day_ending[time.strftime("%d")]
    da = '%i'%float(time.strftime("%d"))+ender
    return mo+' '+da+', '+yr


def parse_kwords(kwords):
    '''

    merge keywords from the same meeting into a single string.
    
    '''
    kword_string = ''
    for index,word in enumerate(kwords):
        if index != 0:
            kword_string += ', '+word
        else:
            kword_string += word
    return kword_string


def pull_keywords(file):
    '''

    rip through journal files for keywords (lines leading with &)


    '''
    f = open(file)
    #
    JDict = {}
    keyword_lines = []
    #
    i = -1
    kwords = []
    for line in f:
        # skip all the protected lines
        if (line[0] == '#') | (line[0] == " ") | (line[0] == "\n") | (line[0] =='@'):# | (line[0] =='*'):
            continue
        # increment line counter
        i += 1
        # tag keyword lines
        if (line[0] == '&'):
            keyword_lines.append(i)

            if ':' in line: # is there a secondary title expansion?

                # guard against starting spaces
                kwords.append(   (line[1:[index for index,value in enumerate(line) if value == ':'][0]]).lstrip(" ") )
                
            else:

                kwords.append(  (line[1:-1]).lstrip(" "))
                
        #print line
        JDict[i] = line
    #
    f.close()
    return JDict,kwords,keyword_lines


def pull_keywords_dictionary(file,KDict):

    id_string,div_string = parse_jrn_name(file)
    f = open(file)
    #
    q_number = len(KDict.keys())
    #
    for line in f:
        if (line[0] == '&'):
            if ':' in line: # is there a secondary title expansion?
                KDict[q_number] = [(line[1:[index for index,value in enumerate(line) if value == ':'][0]]).lstrip(" "),id_string,file]
            else:
                KDict[q_number] = [(line[1:-1]).lstrip(" "),id_string,file]
            q_number += 1

    #
    f.close()
    return KDict



#
# generate a dictionary that 
#
def parse_toc(KDict,jorder,sort='freq'):
    '''
    parse_toc

    generate an ORDERED dictionary of unique values for the index.

    comes in three flavors for sorting.


    '''
    PKDict = {}
    lnumber = 0

    #
    # make a dictionary of the unique keywords from a master keyword dictionary
    #
    UKDict = {}
    for i in range(0,len(KDict.keys())):

        #
        # 04.02.2017: change to be all .lower() for keyword comparison
        #
        if KDict[i][0].lower() not in UKDict.keys():
            UKDict[KDict[i][0].lower()] = [1.,[KDict[i][1]],[KDict[i][2]]]
        else:
            UKDict[KDict[i][0].lower()][0] += 1.
            UKDict[KDict[i][0].lower()][1].append(KDict[i][1])
            UKDict[KDict[i][0].lower()][2].append(KDict[i][2])
    
    if sort=='recent':
        for jrnfile in jorder:
            id_string,div_string = parse_jrn_name(jrnfile)
            for key in UKDict.keys():
                if UKDict[key][1][0] == id_string:
                    PKDict[lnumber] = '<li style="color: #000000">'+key
                    lnumber += 1
                    for ntime in range(0,len(UKDict[key][1])):
                        if UKDict[key][2][ntime][-4:]=='.jrn':
                            PKDict[lnumber] = ' <a href=\"#'+UKDict[key][1][ntime]+'\" style="color: #1a53ff"> ['+UKDict[key][1][ntime]+'] </a>'
                        if UKDict[key][2][ntime][-5:]=='.ajrn':
                            PKDict[lnumber] = ' <a href=\"#'+UKDict[key][1][ntime]+'\" style="color: #bfbfbf"> ['+UKDict[key][1][ntime]+'] </a>'
                        if UKDict[key][2][ntime][-5:]=='.cjrn':
                            PKDict[lnumber] = ' <a href=\"#'+UKDict[key][1][ntime]+'\" style="color: #ef6b51"> ['+UKDict[key][1][ntime]+'] </a>'
                        
                        lnumber += 1
                    PKDict[lnumber] = '</li>'

                    
    if sort=='freq':
        j = 0
        while j < len(UKDict.keys()):
            for counter in range(100,0,-1):
                for key in UKDict.keys():
                    if UKDict[key][0] == counter:
                        PKDict[lnumber] = '<li style="color: #000000">'+key
                        lnumber += 1
                        for ntime in range(0,len(UKDict[key][1])):
                            if UKDict[key][2][ntime][-4:]=='.jrn':
                                PKDict[lnumber] = ' <a href=\"#'+UKDict[key][1][ntime]+'\" style="color: #1a53ff"> ['+UKDict[key][1][ntime]+'] </a>'
                            if UKDict[key][2][ntime][-5:]=='.ajrn':
                                PKDict[lnumber] = ' <a href=\"#'+UKDict[key][1][ntime]+'\" style="color: #bfbfbf"> ['+UKDict[key][1][ntime]+'] </a>'
                            if UKDict[key][2][ntime][-5:]=='.cjrn':
                                PKDict[lnumber] = ' <a href=\"#'+UKDict[key][1][ntime]+'\" style="color: #ef6b51"> ['+UKDict[key][1][ntime]+'] </a>'
                            lnumber += 1
                        PKDict[lnumber] = '</li>'
                        lnumber += 1
                        j += 1

                        
    if sort=='alpha':
        alphalist = sorted(UKDict.keys())
        for key in alphalist:
            PKDict[lnumber] = '<li style="color: #000000">'+key
            lnumber += 1
            for ntime in range(0,len(UKDict[key][1])):
                if UKDict[key][2][ntime][-4:]=='.jrn':
                    PKDict[lnumber] = ' <a href=\"#'+UKDict[key][1][ntime]+'\" style="color: #1a53ff"> ['+UKDict[key][1][ntime]+'] </a>'
                if UKDict[key][2][ntime][-5:]=='.ajrn':
                    PKDict[lnumber] = ' <a href=\"#'+UKDict[key][1][ntime]+'\" style="color: #bfbfbf"> ['+UKDict[key][1][ntime]+'] </a>'
                if UKDict[key][2][ntime][-5:]=='.cjrn':
                    PKDict[lnumber] = ' <a href=\"#'+UKDict[key][1][ntime]+'\" style="color: #ef6b51"> ['+UKDict[key][1][ntime]+'] </a>'
                lnumber += 1
            PKDict[lnumber] = '</li>'
            lnumber += 1
    return PKDict




def index_jorder(jorder):
    return [x for x in range(0,len(jorder))]




def pull_reports(file,RDict):
    '''

    rip through journal files to find open questions, that is, those leading with '@'

    '''
    id_string,div_string = parse_jrn_name(file)
    
    f = open(file)
    #
    r_number = len(RDict.keys())
    #
    for line in f:
        
        if (line[0] == '$'):
            
            RDict[r_number] = '<li><a href=\"#'+id_string+'\"> ['+id_string+'] </a><a href=\"images/'+line[1:-1]+'.pdf\">'+line[1:-1]+'</a></li>'
            
            r_number += 1

    
    f.close()
    
    return RDict



def pull_open_questions(file,QDict):
    '''

    rip through journal files to find open questions, that is, those leading with '@'

    '''
    id_string,div_string = parse_jrn_name(file)
    
    f = open(file)
    #
    q_number = len(QDict.keys())
    #
    for line in f:
        
        if (line[0] == '@'):
            
            QDict[q_number] = '<li><a href=\"#'+id_string+'\"> ['+id_string+'] '+line[1:-1]+'</a></li>'
            
            q_number += 1

    
    f.close()
    
    return QDict



def pull_figures(file):
    '''

    rip through journal files to find images or movies, that is, those leading with '*'

    return a dictionary of images, IDict.

    lines with a leading * should be in the format *source  :  everything after colon is treated as a caption.
    
    '''
    IDict = {}

    # grab the id_string and div_string corresponding to the journal file
    id_string,div_string = parse_jrn_name(file)
    
    f = open(file)

    
    f_number = 0     # figure number index

    for line in f:
        if (line[0] == '*'):
            f_number += 1
            # check for a caption
            if ':' in line: # is there a secondary title expansion?
                figloc = line[1:[index for index,value in enumerate(line) if value == ':'][0]]
                figcap = line[[index for index,value in enumerate(line) if value == ':'][0]+1:-1]
            else:
                figloc = line[1:-1]
                figcap = ""
            # check to see if movie
            if 'mp4' in figloc:
                #
                # the poster image must have the same name as the movie, except be a .png
                postername = figloc.strip('mp4')+'png'
                IDict[f_number-1] = boilerimage0+'images/'+figloc+boilerimage1a+'images/'+postername + \
              boilerimage2+'images/'+figloc + boilerimage3 + str(f_number) + boilerimage4 + figcap + boilerimage5
            else:
                IDict[f_number-1] = boilerimage0+'images/'+figloc+boilerimage1+'images/'+figloc + \
              boilerimage2+'images/'+figloc + boilerimage3 + str(f_number) + boilerimage4 + figcap + boilerimage5

    #
    f.close()
    return IDict



# really want data-title=" " to go after data-lightbox if want to do an adaptive way

# boilerplate html to wrap the images
boilerimage0 = '<div class=\"row\">\n<div class=\"span2 i-block\" align=\"center\">\n <a href=\"'
boilerimage1 = '\"data-lightbox=\"image-1\"><img src=\"'
boilerimage1a = '\"><img src=\"'

boilerimage2 = '\" width=\"200\"></a><br><a href=\"'
boilerimage3 = '\"target=\"_blank\">Figure '
boilerimage4 = '</a></div><br>'
boilerimage5 = '</div>'



def print_single_image(line,f_number):
    '''

    take an image line and return proper html code
    
    '''
    f_number += 1
    # check for a caption
    if ':' in line: # is there a secondary title expansion?
        figloc = line[1:[index for index,value in enumerate(line) if value == ':'][0]]
        figcap = line[[index for index,value in enumerate(line) if value == ':'][0]+1:-1]
    else:
        figloc = line[1:-1]
        figcap = ""
    # check to see if movie
    if 'mp4' in figloc:
        #
        # the poster image must have the same name as the movie, except be a .png
        postername = figloc.strip('mp4')+'png'
        html_image = boilerimage0+'images/'+figloc+boilerimage1a+'images/'+postername + \
              boilerimage2+'images/'+figloc + boilerimage3 + str(f_number) + boilerimage4 + figcap + boilerimage5
    else:
        html_image = boilerimage0+'images/'+figloc+boilerimage1+'images/'+figloc + \
              boilerimage2+'images/'+figloc + boilerimage3 + str(f_number) + boilerimage4 + figcap + boilerimage5
    #
    return html_image,f_number




def parse_journal_file(file):
    #
    # the master dictionary
    f_number = 0
    h_increment = -1
    HDict = {}
    #
    # make the title line and print to file
    id_string,div_string = parse_jrn_name(file)
    h_increment += 1
    HDict[h_increment] = div_string
    
    JDict,kwords,keyword_lines = pull_keywords(file)
    #
    kword_string = parse_kwords(kwords)

    h_increment += 1
    HDict[h_increment] = '<h3>'+kword_string+'</h3></div>'
    #
    nlines = len(JDict.keys())
    nkwords = len(keyword_lines)
    #

    for line_index,line_val in enumerate(keyword_lines):
        # go through different headings
        line = JDict[line_val]
        if ':' in line: # is there a secondary title expansion?
                ekword = line[[index for index,value in enumerate(line) if value == ':'][0]+1:-1]
        else:
                ekword = (line[1:-1]).lstrip(" ")

        # increment the html line
        h_increment += 1

        # place a break header
        HDict[h_increment] = '<br><div class=\"rlog\">'+ekword
        
        # loop through lines after keyword
        if line_index == nkwords - 1: maxline = nlines
        else: maxline = keyword_lines[line_index+1]
        #
        for sub_line in range(line_val+1,maxline):
            if (JDict[sub_line][0] == '>') & (JDict[sub_line][1] != '>'):
                #print '<li>'+JDict[sub_line][1:-1],
                h_increment += 1
                HDict[h_increment] = '<li>'+JDict[sub_line][1:-1]
                extra = 0
                while (JDict[sub_line+extra][0] != '>') & (JDict[sub_line+extra][0] != '&'):
                    extra += 1
                    #print JDict[sub_line+extra][0:-1],
                    h_increment += 1
                    HDict[h_increment] = JDict[sub_line+extra][0:-1]
    
                    if (sub_line+extra == nlines): break
                #print '</li>' # close the list
                h_increment += 1
                HDict[h_increment] = '</li>'
            if (JDict[sub_line][0:2] == '>>'):
                #print '<p>&rarr; '+JDict[sub_line][2:-1],
                h_increment += 1
                HDict[h_increment] = '<p>&rarr; '+JDict[sub_line][2:-1]
                extra = 0
                while (JDict[sub_line+extra][0] != '>') & (JDict[sub_line+extra][0] != '&'):
                    extra += 1
                    #print JDict[sub_line+extra][0:-1],
                    h_increment += 1
                    HDict[h_increment] = JDict[sub_line+extra][0:-1]
                    
                    if (sub_line+extra == nlines): break
                #print '</p>' # close the paragraph
                h_increment += 1
                HDict[h_increment] = '</p>'
            if (JDict[sub_line][0] == '*'):
                html_image, f_number = print_single_image(JDict[sub_line],f_number)

                # increment dictionary line and add to dictionary
                h_increment += 1
                HDict[h_increment] = html_image
        #
    #print '</div>' # end of the keyword div
    h_increment += 1
    HDict[h_increment] = '</div>'
    return HDict


'''

jrnls,CalDict = jparse.parse_journal_files()
CD,jorder = jparse.generate_calendar_html(CalDict)

for jfile in jrnls:
    HDict = jparse.parse_journal_file(jfile)
    for i in range(0,len(HDict)):
        print HDict[i]

'''


