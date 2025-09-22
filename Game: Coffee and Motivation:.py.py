import random

#images
coffee =('''
    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \|
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \|
\_____________________/''')

sleepiness =(''' 
     |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)  ''')

motivation = ('''        
       ,O,
      ,OOO,
'oooooOOOOOooooo'
  `OOOOOOOOOOO`
    `OOOOOOO`
    OOOO'OOOO
   OOO'   'OOO
  O'         'O''')

print("Welcome to this game!\n")

print("Coffee vs. Motivation – A playful take on 'Rock-Paper-Scissors'.\n")

print("Who will win?\n")

user_choice= int(input("What do you choose? Type 0 für coffee (☕), 1 for sleepiness (😴) or 2 for motivation (⭐) \n"))
game_images =[coffee, sleepiness, motivation]

print(game_images[user_choice])


computer_choice = random.randint(0,2)

print(f"Computer chose {game_images[computer_choice]}")


if user_choice >= 3:
    print("You typed a wrong number!\n")
elif computer_choice == 1 and user_choice ==0:
    print("You lose!\n")
elif user_choice == 1 and computer_choice == 0:
    print("You win!\n")
elif computer_choice == 2 and user_choice == 1:
    print("You lose!\n")
elif user_choice == 2 and computer_choice == 1:
    print("You win :)!\n")
elif computer_choice == 0 and user_choice == 2:
    print("You lose! :(\n")
elif user_choice == 0 and computer_choice == 2:
    print("You win! :)\n")
#It's a draw
elif user_choice == 1 and computer_choice == 1:
    print("It's a draw :)\n")
elif user_choice == 2 and computer_choice == 2:
    print("It's a draw :)\n")
elif user_choice == 0 and computer_choice == 0:
    print("It's a draw :)\n")





