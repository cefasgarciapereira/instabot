<p align="center">
  <img src="https://i.imgur.com/sJzfZsL.jpg" width="154">
  <h1 align="center">InstaBot</h1>
  <p align="center">This application is a personal project to make automatic comments on Instagram posts. This program allows the user to enter their credentials to log in to Instagram, choose a post using its URL and tag friends in the posts in order to facilitate participation in contests.
</p>

## How to use it?
Regardless of how you decide to run the program, you must perform the following steps:

1. Inform your instagram user without @
2. Inform your password, which will not be saved anywhere
3. Inform the URL of the contest post that you want to participate
5. Number of friends that will be marked by comment

These fields can be informed in two ways. You can inform it while te program is running or write a file called `settings.json` like below:

```json
# settings.json
{
    "username": "<insert_your_username>",
    "password": "<insert_your_password>",
    "post_url": "<insert_post_url>",
    "number_of_friends": 2 // this line should not contain quotes
}
```

You also must provide a friends list in a text file named as `friends.txt`, with each line referring to a friend with its @, for example:

```
# friends.txt

@friend1
@friend2
@friend3
```

### Source Code
If you are a programmer and want to use the program through the source code, just clone it, install its dependencies through the `pip install` command and run the app.py through `python app.py`

### Executable File
This way is a little less stable, since it depends someone to make the build of the program which may difficult the program to be in date with the source code. 
On the other hand, this way should be easier for less experienced users, as it is enough to run the `.exe` program.

# Documentação em Português

## Como usar?
Independentemente de como você decidir executar o programa, você deverá realizar os seguintes campos:


1. Informar seu usuário do Instagram sem o @
2. Informar sua senha, que não será salva em lugar algum
3. Informar a URL da postagem do concurso que você deseja participar
5. Número de amigos que serão marcados por comentário

Esses campos podem ser informados de duas formas. Você pode informá-los enquanto o programa está rodando ou escrever um arquivo chamado `settings.json` como abaixo:

```json
# settings.json
{
    "username": "<substitua_pelo_seu_usuário>",
    "password": "<substitua_pela_sua_senha>",
    "post_url": "<substitua_pela_url_do_post>",
    "number_of_friends": 2 // esta linha não deve conter as aspas no número
}
```
Sua lista de amigos deve estar disponível em um arquivo `friends.txt`, cujo cada linha se refere a um amigo com seu @, por exemplo:

```
# friends.txt

@amigo1
@amigo2
@amigo3
```

### Código Fonte
Se você é um programador e deseja usar o programa através do código-fonte, basta cloná-lo, instalar suas dependências através do comando `pip install` e executar o app.py através do` python app.py`.

### Arquivo Executável
Esta forma pode ser um pouco menos estável, pois depende de alguém que faça a compilação do programa o que pode implicar em versões diferentes do executável para o código fonte. Por outro lado, esta forma deve ser mais fácil para usuários menos experientes, pois basta executar o programa `.exe`.

