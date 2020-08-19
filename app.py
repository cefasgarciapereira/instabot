from instabot import InstaBot
import getpass
from time import sleep

friends = ['@plmacch', '@gregoryassis', '@tulio3m', '@ana.carolina.poscidonio', '@machatelie', '@marcela_danza', '@lucas.rte', '@maceli_berloques', '@arquiteta.danza', '@swatboss93', '@gabrielradec']
#https://www.instagram.com/p/CECVkAZJWSt/
#--- Start ---#
username = input('Insert your @username: ')
password = getpass.getpass('Insert your password (the text wont be shown): ')
url = input('Insert the contest URL: ')
number_of_posts = int(input('Inform the number of comments: '))
number_of_friends = int(input('Inform the number of friends to be tagged: '))

bot = InstaBot(username, password)
bot.navigate_to(url)

for i in range(0, number_of_posts):
    bot.comment(bot.generate_tags(friends, 2))
    sleep(5)