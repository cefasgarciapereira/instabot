from instabot import InstaBot
import getpass
from time import sleep

#https://www.instagram.com/p/CECVkAZJWSt/

#--- Start ---#
#.?PFJ3uLvk
username = input('Insert your @username: ')
password = getpass.getpass('Insert your password (the text wont be shown): ')
url = input('Insert the contest URL: ')
number_of_posts = int(input('Inform the number of comments: '))
number_of_friends = int(input('Inform the number of friends to be tagged: '))

#--- Application --- #
friends = []
get_list_of_friends()
bot = InstaBot(username, password)
bot.navigate_to(url)

def get_list_of_friends(file_path='friends.txt'):
    with open(file_path) as fp:
        line = fp.readline()
        while line:
            name = line.split('\n')[0]
            friends.append(name)
            line = fp.readline()


for i in range(0, number_of_posts):
    while True:
        try:
            bot.comment(bot.generate_tags(friends, 2))
            sleep(5)
            print('Commented ',i)
        except Exception:
            print('Comment failed, waiting 10 minutes to retry...')
            sleep(600)
            continue
        break