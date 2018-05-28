TEAM_NAME: Invincible
TEAM_MEMBERS:
	Junkai Huang, z5148077
	Yuan Gao, z5050229
	Junnan Chen, z5037336

Installation Guide 
- Environment:Python 3.6.1 
- step1: Unzip server.zip
- step2: Create a new project
- step3: Paste all the file into the ./server under the root of the new project
- step4: Set up the virtual environment and then open up the terminal window
- step5: Install the libraries using the following command
		pip3 install -r requirements.txt
- step6: run app.py in PyCharm
- step7: open ./Front/index.html in a browser
	if chrome:
		Windows: chrome.exe --user-data-dir="C:/Chrome dev session" --disable-web-security
		Linux: google-chrome --disable-web-security
		Mac: open -a Google\ Chrome --args --disable-web-security

Introduction
This Data Mashup application combines geographic information and online job data to demonstrate job research and statistics of Australia and the United Kingdom.The web application is designed to do researches on three dimensionality, including Jobs by Location, Jobs by Industry, Weekly Work Hours which provides an overview on job geographic distrubution, indurtry job amount and workload by gender in the two countries.
There are diversified interaction for users to do quick filter or search for specific contents and due to RESTful apis design, much more functions is easy to expanded.
