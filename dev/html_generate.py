#
# the master creator for the html file
#
#
#
# OUTPUTS:
# ---------------
# index.html: the master webpage.
#                -should largely be formatted to be readable for changes to be made
#
#
#


import boilerplate
import jparse


journal_directory = '../journals/'

jparse.img_loc = '../images/'

#
# FOR THE BOILERPLATE HTML
#

# the name to appear in tabs
boilerplate.rjournal_name = 'MSP Research Journal'

# the image to be the tiny icon
boilerplate.tinyicon = 'images/backgroundimg.png'

# names of the involved parties
boilerplate.people = 'Petersen, Weinberg, Katz'

# main image
boilerplate.bck_image = 'images/backgroundimg.png'

# top blurb
boilerplate.blurb = 'This is the research journal for the Galactic Dynamics group at the University of Massachusetts at Amherst: Michael S. Petersen, Martin D. Weinberg, and Neal Katz. Use the options at the top to jump to a calendar of meeting dates, skip to the open research questions, view the meeting logs in their entirety, or skip to the index to search keywords.'


#
# create the html given the above variables
#
boilerplate.set_html()



def make_html(file,sorter):
    g = open(file,'w')

    # parse all the journals
    jrnls,CalDict = jparse.parse_journal_files(journal_directory)


    # build the calendar
    CDict,jorder = jparse.generate_calendar_html(CalDict,journal_directory)

    # pull all keywords
    KDict = {}
    for jfile in jorder:
        KDict = jparse.pull_keywords_dictionary(jfile,KDict)

    # make the table of contents
    PKDict = jparse.parse_toc(KDict,jorder,sort=sorter)

    # print a boilerplate header set-up.
    print >>g,boilerplate.Header[0]
    print >>g,boilerplate.BodyHeader[0]

    ############################# introduction

    print >>g,boilerplate.IntroBoiler[0]

    ############################# calendar section
    print >>g,boilerplate.CalHeader[0]

    # calendar here

    try:
        for i in range(0,len(CDict)):
            print >>g,CDict[i]
    except:
        pass

    print >>g,boilerplate.EndSection[0]

    ############################# question section
    print >>g,boilerplate.QuestionHeader[0]

    # questions here

    QDict = {}
    for jfile in jorder:
        QDict = jparse.pull_open_questions(jfile,QDict)


    try:
        for i in range(0,len(QDict)):
            print >>g,QDict[i]
    except:
        pass


    print >>g,boilerplate.EndSection[0]

    ############################# report section
    print >>g,boilerplate.ReportHeader[0]

    # questions here

    RDict = {}
    for jfile in jorder:
        RDict = jparse.pull_reports(jfile,RDict)


    try:
        for i in range(0,len(RDict)):
            print >>g,RDict[i]
    except:
        pass


    print >>g,boilerplate.EndSection[0]

    ############################# log section
    print >>g,boilerplate.LogHeader[0]

    # print >>g,HDicts here
    for jfile in jorder:
        HDict = jparse.parse_journal_file(jfile)
        try:
            for i in range(0,len(HDict)):
                print >>g,HDict[i]
        except:
            pass
        
        print >>g,'<br>'
        print >>g,'<br>'

    print >>g,boilerplate.EndSection[0]

    ############################# table of contents
    if sorter == 'freq':
        print >>g,boilerplate.ToCBoilerTopFreq[0]

    if sorter == 'recent':
        print >>g,boilerplate.ToCBoilerTopRecent[0]

    if sorter == 'alpha':
        print >>g,boilerplate.ToCBoilerTopAlpha[0]
        
    try:
        for i in range(0,len(PKDict)):
            print >>g,PKDict[i]
    except:
        pass

    print >>g,boilerplate.ToCBoilerBottom[0]

    ############################# footer section
    print >>g,boilerplate.FooterTop[0]
    import time
    print >>g,'Last Updated '+jparse.parse_date_today()

    print >>g,boilerplate.FooterEnd[0]


    g.close()





# three different sortings, linked to each other
make_html('../freqindex.html','freq')

make_html('../recentindex.html','recent')

make_html('../index.html','alpha')



