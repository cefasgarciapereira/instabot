from instabot import InstaBot
import getpass
from time import sleep
import settings

#--- Start ---#
#print('Olá, Seja bem vindo(a) ao InstaBot :)')
#username = input('Insira seu usuário: ')
#password = getpass.getpass('Insira sua senha (o conteúdo não será exibido): ')
#url = input('Insira a URL do sorteio: ')
#number_of_friends = int(input('Informe o número de amigos que devem ser marcados: '))

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
        except Exception as err:
            print(err)
            continue

#--- Calls ---#
friends = []
get_list_of_friends()
bot = InstaBot(settings.username, settings.password)
bot.navigate_to(settings.post)
comment(settings.friends)
print('Processo finalizado')
sleep(7)