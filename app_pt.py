from instabot import InstaBot
import getpass
from time import sleep

#--- Start ---#
print('Olá! Seja bem vindo ao InstaBot :)')
username = input('Insira seu usuário: ')
password = getpass.getpass('Insira sua senha: ')
url = input('Insira a URL do sorteio: ')
number_of_posts = int(input('Informe o número de comentários que deseja: '))
number_of_friends = int(input('Informe o número de amigos que devem ser marcados: '))

#--- Application --- #
def get_list_of_friends(file_path='friends.txt'):
    with open(file_path) as fp:
        line = fp.readline()
        while line:
            name = line.split('\n')[0]
            friends.append(name)
            line = fp.readline()

def comment(n, n_friends):
    i = 0
    while i < n:
        try:
            bot.comment(bot.generate_tags(friends, n_friends))
            i += 1
            print(i, ' Comentários')
            sleep(5)
        except Exception:
            print('Você atingiu o limite de requisições. O programa tentará novamente em 10 minutos...')
            sleep(600)
            break

#--- Calls ---#
friends = []
get_list_of_friends()
bot = InstaBot(username, password)
bot.navigate_to(url)
comment(number_of_posts, number_of_friends)
#.?PFJ3uLvk
#https://www.instagram.com/p/CECVkAZJWSt/
