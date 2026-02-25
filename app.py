from instabot import InstaBot
import getpass
from time import sleep
import json

logo = """
                                                          
                                .((((((*                        
                                     ./(((*                     
                                .((((*   (((,                   
                                    /(((  *((*                  
                              (((((* .(((  (((                  
                             ,((((((                            
                               (((                              
                    ,*/(((((((((((((((((((/*.                   
                (((*.     ....,,*///((((((((((((*               
             .(/ .((((((((((((((((((((((((/.(((((((             
            ,(.,(((((((((((((((((((((((((     ((((((            
            (/,(((((((((((((((((((((((((((/,/(((((((/           
                         /(((((((((((((,                        
                       ((((/        ,((((.                      
       ,((((((((((((((((((  ,((((     ,#((##############/       
     /(((, .(*/(((((* (((, ,(((((((((  (##( ########(  /###.    
    *((,   .(*/(((((/ (((/  /(((((((, .(##/ ########(    (##.   
    /((.   .(*/((((((* ((((   .**,   *(#(( #########(    /##.   
    /((.   .(**(((((((( *(((((////((((((.,##########(    /##.   
    /((.   ./**//////////, ,/(((((((/  ((((#########(    /##.   
    ///.    // *///////////////((((((((((((((#######.    /##.   
    ///.     */ .****//////////////((((((((((((####.     (##,   
 .//////**     **,         */////////,      .((((,    .###(###( 
 ///   ,**         ,  ,***** .**//* ,,  /((((/        (##   *##.
                 ..  ,,******.     *. .//((((((                 
                                                                
"""

#--- Start ---#
try:
    print (logo)
    print('Olá, Seja bem vindo(a) ao InstaBot :)\n')
    flux = input('Deseja ler os dados de settings.json? \n\nSim: [s/sim] Não: [n/não]\n\n=> ')

    if(flux == "s" or flux == "sim"):
        try:
            f = open('settings.json')
            settings = json.load(f)
            username = settings['username']
            password = settings['password']
            post = settings['post_url']
            number_of_friends = settings['number_of_friends']
            auth_code = settings.get('auth_code', None)
            f.close()
        except Exception:
            print("Erro ao carregar dados de settings.json")
    else:
        username = input('Insira seu usuário: ')
        password = getpass.getpass('Insira sua senha (o conteúdo não será exibido): ')
        post = input('Insira a URL do sorteio: ')
        number_of_friends = int(input('Informe o número de amigos que devem ser marcados: '))
        auth_code = None

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
                print("O programa tentará de novo em instantes")
                continue

    #--- Calls ---#
    try:
        get_list_of_friends()
        bot = InstaBot(username, password, auth_code=auth_code)
        bot.navigate_to(post)
        comment(number_of_friends)
        print('Processo finalizado')
        sleep(7)
    except Exception as err:
        print("Erro: "+str(err))
        input("Pressione qualquer tecla para fechar o programa")
except Exception as err:
    print("Erro: "+str(err))
    input("Pressione qualquer tecla para fechar o programa")