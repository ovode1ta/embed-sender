import json
import pyperclip
from colorama import init
import os

init()

with open('config.json') as json_file:
    data = json.load(json_file)

    token = data.get('token')

class c:
	BL = '\033[30m'
	R  = '\033[31m'
	LR = '\033[1;31m'
	G  = '\033[32m'
	YE = '\033[93m'
	B  = '\033[34m'
	LB = '\033[1;34m'
	MA = '\033[35m'
	CY = '\033[36m'
	W  = '\033[37m'
	RS = '\033[0m'
	CLEAR = '\033[0m'
	BD = '\033[1m'
	UL = '\033[4m'

	X = '\033[0m'
	Y = '\033[31m'

    
class logs():

	def error(text):
		print(f"{c.RS}[LOGS]{c.R} {text} {c.CLEAR}")

	def success(text):
		print(f"{c.RS}[LOGS]{c.G} {text} {c.CLEAR}")

	def info(text):
		print(f"{c.LB}[INFO]{c.CY} {text} {c.CLEAR}")    

def main():

    title = input("Enter the title of the embed to send: ")

    description = input("Now enter the description of the embed: ")

    channelid = input("Finally, enter the id of the channel to send the message in (Doesn't work in DMs): ")

    curlCommand = 'curl -X POST https://discord.com/api/v8/channels/' + channelid + '/messages -H "Authorization: ' + token + '" -H "Content-type: application/json" -d "{\\\"content\\\":\\\"\\\",\\\"embed\\\":{\\\"title\\\":\\\"' + title + '\\\", \\\"description\\\": \\\"' + description + '\\\"}}"'
    
    try:
        os.exec(curlCommand)
    except:
        logs.error("An error occured while trying to execute the command. Try again.
    
    main()




main()
