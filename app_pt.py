from instabot import InstaBot
import getpass
from time import sleep

#--- Start ---#
print('Primeiramente, eu te amo! <3')
print('Segundamente, Seja bem vinda ao InstaBot :)')
username = input('Insira seu usuário: ')
password = getpass.getpass('Insira sua senha (o conteúdo não será exibido): ')
url = input('Insira a URL do sorteio: ')
number_of_friends = int(input('Informe o número de amigos que devem ser marcados: '))

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
            bot.comment(bot.generate_tags(friends, n_friends))
            i += 1
            print(i, ' Comentários')
            sleep(65)
        except Exception:
            print(Exception)
            print('Você atingiu o limite de requisições. O programa tentará novamente em 10 minutos...')
            sleep(600)
            continue

#--- Calls ---#
friends = []
get_list_of_friends()
bot = InstaBot(username, password)
bot.navigate_to(url)
comment(number_of_friends)
print('Processo finalizado')
sleep(7)