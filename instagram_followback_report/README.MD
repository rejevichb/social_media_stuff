##Instagram Follower Check

This program allows you to get a 100% accurate list of people who do not follow you back on instagram. 

It requires basic and simple use of the command prompt and checking for/downloading python. 

##Step 1.

###Aquire your insagram data. 

Log onto the mobile app and click `Settings > Security > Download Data`. You will be prompted 
for your password and then your data will be emailed to the account on file with instagram. When you receive the data in 
an email, you will be guided to a web page and presented with a multi part data download page. Only `Part 1` of the data download is required, but you can access all photos ever shared if you download all 5.

##Step 2. 


Unzip the gzipped file and Identify the file connections.json
Place this file in a subdirectory (create a new one and name it)

##Step 3.
Make sure you have python 3 downloaded on your computer. If not, download before proceeding. 

>To check if you have python3, open a Terminal (CommandPrompt) window and type python3 and press enter. 
If you see three arrows >>>, you have python already. 

If you do not have python, download the appropriate operating system version from https://www.python.org/downloads/
The latest is fine.

##Step 4.
Open a command prompt and navigate to the folder you created. To view the contents of the folder you are in, type `ls -la`'
and press enter. Use `cd`, `ls -la`, and `pwd` from https://www.codecademy.com/articles/command-line-commands 

If you have trouble, google `"how to open command line at a folder (insert your OS here)"`

##Step 5. 
Once you have a command line at the folder, when you type pwd you will see a path ending in the name of the folder
displayed. If you type `ls -la` in the folder, you should see the two files, connections.json and GetFollowers.py.

Execute the following command:
python3 Get_Unfollowers.py connections.json

##Step 6

There is a new file in the directory now, called InstagramFolloweAnalysis.txt
There you will find counts and lists of your closest friends and those who do not follow you back.

