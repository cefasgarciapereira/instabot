from instabot import InstaBot
import getpass
from time import sleep
import json

#--- Start ---#
print('Olá, Seja bem vindo(a) ao InstaBot :)\n')
f = open('logo.txt', 'r')
print (f.read())
f.close()
flux = input('Deseja ler os dados de settings.json? \n\nSim: [s/sim] Não: [n/não]\n\n=> ')

if(flux == "s" or flux == "sim"):
    f = open('settings.json')
    settings = json.load(f)
    username = settings['username']
    password = settings['password']
    post = settings['post_url']
    number_of_friends = settings['number_of_friends']
    f.close()
else:
    username = input('Insira seu usuário: ')
    password = getpass.getpass('Insira sua senha (o conteúdo não será exibido): ')
    post = input('Insira a URL do sorteio: ')
    number_of_friends = int(input('Informe o número de amigos que devem ser marcados: '))

#--- Application --- #
friends = []

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
            bot.comment(bot.generate_tags(friends, n_friends))
            i += 1
            print(i, ' Comentários')
            sleep(65)
        except Exception as err:
            print(err)
            continue

#--- Calls (Interface) ---#
get_list_of_friends()
bot = InstaBot(username, password)
bot.navigate_to(post)
comment(number_of_friends)
print('Processo finalizado')
sleep(7)