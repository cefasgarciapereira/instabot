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
4. Number of comments you want the program to make
5. Number of friends that will be marked by comment

Your friends list should be available in a friends.txt file, each line referring to a friend with your @, for example:

```
# friends.txt

@ friend1
@ friend2
@ friend3
```

### Source Code
If you are a programmer and want to use the program through the source code, just clone it, install its dependencies through the `pip install` command and run the app.py through `python app.py`

### Executable File
This way is a little less stable, since it depends someone to make the build of the program which may difficult the program to be in date with the source code. 
On the other hand, this form should be easier for less experienced users, as it is enough to run the `.exe` program.
