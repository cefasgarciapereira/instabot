from instabot import InstaBot
import getpass
from time import sleep

#--- Start ---#
username = input('Insert your @username: ')
password = getpass.getpass('Insert your password (the text wont be shown): ')
url = input('Insert the contest URL: ')
number_of_friends = int(input('Inform the number of friends to be tagged: '))

#--- Application --- #
def get_list_of_friends(file_path='friends.txt'):
    with open(file_path) as fp:
        line = fp.readline()
        while line:
            name = line.split('\n')[0]
            friends.append(name)
            line = fp.readline()

def comment(n_friends):
    i = 0
    while True:
        try:
            bot.comment(bot.generate_tags(friends, 2))
            i += 1
            print('Commented ',i)
            sleep(5)
        except Exception:
            print(Exception)
            print('Comment failed, waiting 10 minutes to retry...')
            sleep(600)
            break

#--- Calls ---#
friends = []
get_list_of_friends()
bot = InstaBot(username, password)
bot.navigate_to(url)
comment(number_of_friends)
#.?PFJ3uLvk
#https://www.instagram.com/p/CECVkAZJWSt/
