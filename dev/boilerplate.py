#######################################################
#
#  boilerplate.py: html wrappers for journal generation.
#
#     should be largely independent of the .css file input?
#
#  INCLUDES:
#  --------------
#  global variables to be set
#
#  set_html : makes the boilerplate html to be accessed
#

global rjournal_name, tinyicon, people, bck_image, blurb


# the name to appear in tabs
rjournal_name = '???'

# the image to be the tiny icon
tinyicon = '???'

# names of the involved parties
people = '???'

# main image
bck_image = '???'

blurb = '???'


def set_html():
    global Header, BodyHeader, IntroBoiler, EndSection, CalHeader, QuestionHeader, ReportHeader, LogHeader
    global ToCBoilerTopFreq, ToCBoilerTopRecent, ToCBoilerTopAlpha, ToCBoilerBottom
    global FooterTop, FooterEnd

    
    #
    # full html header, including .js imports
    #

    Header = ['<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n	<meta charset=\"utf-8\" />\n\n	<title>'+\
    rjournal_name\
                 +'</title>\n	<meta name=\"HandheldFriendly\" content=\"true\">\n	<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">\n	<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, maximum-scale=1\">\n	<!-- Import CSS -->\n	<link rel=\"stylesheet\" href=\"css/main.css\">\n	<link href=\"http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css\" rel=\"stylesheet\">\n	<link href=\"http://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css\" rel=\"stylesheet\">\n	<script src=\"js/jquery.min.js\"></script>\n	<script src=\"js/jquery.easing.min.js\"></script>\n	<script src=\"js/jquery.scrollto.min.js\"></script>\n	<script src=\"js/slabtext.min.js\"></script>\n	<script src=\"js/jquery.nav.js\"></script>\n	<script src=\"js/myjs.js\"></script>\n<script src="js/lightbox.min.js"></script>\n	<script src=\"js/main.js\"></script>\n<link href="css/lightbox.css" rel="stylesheet" />\n<link rel=\"shortcut icon\" href=\"'+\
    tinyicon\
            +'\" type=\"image/png\">\n<script type=\"text/x-mathjax-config\">\nMathJax.Hub.Config({\n  tex2jax: {inlineMath: [[\'$\',\'$\']]}\n});\n</script>\n<script type=\"text/javascript\" async\n  src=\"https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML\">\n</script>\n</head>']



    #
    # navigable header, including the table of contents
    #
    BodyHeader = ['<body class=\"home color-1\">\n\n<!-- Super Header -->\n<div id=\"header\">\n\n<div class=\"container\">\n         <div class=\"row\">\n\n	   <i id=\"nav-button\" class=\"icon-circle-arrow-down\"></i>\n	 \
        <h2 id=\"logo\">\n	   <a href=\"index.html\"><span>Research Journal</span>\n	 \
        <span class=\"highlight\">'+\
        people\
               +'</span>\n	   </a></h2>\n\n	 \
    <div id=\"top-nav\" class=\"\">\n		 <ul id=\"fixed-nav\">\n	\
        <li><a href=\"#top\"      >Top</a>      </li>\n	\
        <li><a href=\"#calendar\" >Calendar</a> </li>\n	\
        <li><a href=\"#questions\">Questions</a></li>\n	\
        <li><a href=\"#reports\"  >Reports</a>  </li>\n \
        <li><a href=\"#log\"      >Meetings</a> </li>\n \
        <li><a href=\"#index\"    >Index</a>    </li>\n	\
    </ul>\n		 </div>\n\n	  </div>\n     </div>\n</div><!-- End Header -->\n']


    IntroBoiler = ['<!-- Big Full screen Banner -->\n<div class=\"hero bg-fixed bg-color\" id=\"top\">\n    <div class=\"slogan\">\n        <div  class=\"vcenter container\">\n            <div class=\"row\">\n                 <div class=\"span12\">\n			 -->\n		               <div class=\"row\">\n				     <div class=\" img\" align=\"center\"> \n					 					 <img src=\"'+\
                   bck_image\
                   +'\" width=\"450\">\n					  <br>\n				     </div>\n				</div>\n\n			<h4><font size=\"3\">\n'+\
    blurb\
    +'</font></h4>\n		</div>\n            </div>\n        </div>\n    </div>\n</div>\n<!-- End Full screen banner  -->']






    #
    # header for the calendar section
    #
    CalHeader = ['<!-- ########################################################################## -->\n<!-- Calendar Section -->\n<div class=\"section\" id=\"calendar\">\n    <div class=\"container\">\n        <div class=\"content\">\n            <div class=\"row\" >\n	      \n		<div class=\"title\">\n		     <h2>Calendar</h2>\n <div class=\"hr hr-small hr-center\"><span class=\"hr-inner\"></span>\n<p><font size=\"3"> Meetings are shown in blue. Supporting notes are shown in gray. Click on a date to skip to the meeting log. Return by using the Calendar button on the navigation bar.</font></p></div> <br>\n	</div>']


    #
    # header for the Question section
    #
    QuestionHeader = ['<!-- ########################################################################## -->\n<!-- Open Questions Section -->\n<!-- class section-alt is to give a different color please edit css/style.css to change the color -->\n<div class=\"section section-alt\" id=\"questions\">\n    <div class=\"container\">\n        <div class=\"content\">\n	    <div class=\"row\" >\n	      \n		 <div class=\"title\">\n		     <h2>Open Questions</h2>\n\n<p><font size=\"3"> Click on a date to skip to the meeting log that houses the open question. Return using the Questions button on the navigation bar.</font></p>		  </div>']				

    #
    # header for the Reports section
    #
    ReportHeader = ['<!-- ########################################################################## -->\n<!-- Reports Section -->\n<!-- class section-alt is to give a different color please edit css/style.css to change the color -->\n<div class=\"section section-alt\" id=\"reports\">\n    <div class=\"container\">\n        <div class=\"content\">\n	    <div class=\"row\" >\n	      \n		 <div class=\"title\">\n		     <h2>Reports</h2>\n\n<p><font size=\"3"> Collection of miniature reports written on specific topics.</font></p>		  </div>']	

    #
    # header for the Log section
    #
    LogHeader = ['	<!-- ########################################################################## -->\n<!-- Example Procedural generated Section -->\n<div class=\"section section-alt\" id=\"log\">\n    <div class=\"container\">\n        <div class=\"content\">\n	<div class=\"row\" >\n	<div class=\"title\">\n	  <h2> Meeting Log </h2><p><font size=\"3"> Logs from individual research meetings. Navigation is best accomplished using the Calendar, Questions, or Index buttons on the navigation bar.</font></p>\n	</div>']




    #
    # footer details
    #
    FooterEnd = ['</div>\n</body>\n</html>']
    FooterTop = ['<!-- procedurally generate today\'s date -->\n<div id=\"footer\">']

    #
    # general end section
    #
    EndSection = ['</div>\n	 </div>\n    </div>\n</div>\n<!-- End Section -->']


    ToCBoilerTopAlpha = ['<!-- ############################################## Index Section -->\n<div class=\"section\" id=\"index\">\n<div class=\"container\">\n        <div class=\"content\">\n            <div class=\"row\" >\n     		<div class=\"title\">\n		     <h2>Index<font size=\"3\">  Alphabetically Sorted <a href="recentindex.html#index"> (Recency Sorted) </a> <a href="freqindex.html#index"> (Frequency Sorted) </a></font></h2>	\n<p><font size=\"3"> Topics from meetings are linked in blue. Supporting notes on topics are linked in gray. Click on a date to skip to the meeting log that has the keyword. Return using the Index button on the navigation bar.</font></p>	</div>	\n	             			<h4><font size=\"3\">\n <div class=\"index\">\n']

    ToCBoilerTopFreq = ['<!-- ############################################## Index Section -->\n<div class=\"section\" id=\"index\">\n<div class=\"container\">\n        <div class=\"content\">\n            <div class=\"row\" >\n     		<div class=\"title\">\n		     <h2>Index<font size=\"3\">  Frequency Sorted <a href="recentindex.html#index"> (Recency Sorted) </a> <a href="index.html#index"> (Alphabetically Sorted) </a></font></h2>	\n<p><font size=\"3"> Topics from meetings are linked in blue. Supporting notes on topics are linked in gray. Click on a date to skip to the meeting log that has the keyword. Return using the Index button on the navigation bar.</font></p>	</div>	\n	             			<h4><font size=\"3\">\n <div class=\"index\">\n']

    ToCBoilerTopRecent = ['<!-- ############################################## Index Section -->\n<div class=\"section\" id=\"index\">\n<div class=\"container\">\n        <div class=\"content\">\n            <div class=\"row\" >\n     		<div class=\"title\">\n		     <h2>Index<font size=\"3\">  Recency Sorted <a href="freqindex.html#index"> (Frequency Sorted) </a><a href="index.html#index"> (Alphabetically Sorted) </a></font></h2>	\n<p><font size=\"3"> Topics from meetings are linked in blue. Supporting notes on topics are linked in gray. Click on a date to skip to the meeting log that has the keyword. Return using the Index button on the navigation bar.</font></p></div>	\n	             			<h4><font size=\"3\">\n <div class=\"index\">\n']

    ToCBoilerBottom =  [' </div>  </font></h4>\n		</div>\n            </div>\n        </div>\n    </div>\n</div>\n<!-- End Full screen banner  -->']

