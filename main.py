import json
import pyperclip
from termcolor import colored, cprint


with open('config.json') as json_file:
    data = json.load(json_file)

    token = data.get('token')



def main():

    title = input("Enter the title of the embed to send: ")

    description = input("Now enter the description of the embed: ")

    channelid = input("Finally, enter the id of the channel to send the message in (Doesn't work in DMs): ")

    curlCommand = 'curl -X POST https://discord.com/api/v8/channels/' + channelid + '/messages -H "Authorization: ' + token + '" -H "Content-type: application/json" -d "{\\\"content\\\":\\\"\\\",\\\"embed\\\":{\\\"title\\\":\\\"' + title + '\\\", \\\"description\\\": \\\"' + description + '\\\"}}"'

    pyperclip.copy(curlCommand)

    cprint('Success! Copied the curl command to clipboard. Now just paste this in your terminal.', 'green')

    main()




main()
