import time
name=input("please enter your name here:")
print("Hello "+ name+". Welcome to this journey. You will try to find a treasure in a chest.") 
answer1=input("You are standing in front of a castle and there is a forest behind you. Do you want to go into castle or forest?")
if answer1=="forest":
    print("You are now walking in forest and it's getting dark.")
    time.sleep(2)
    print("You are hearing sounds...")
    answer2=input("There is an interesting looking tree do you want to search it?(yes or no)")
    if answer2=="yes":
        print("You died because tree was poisonous.")
        quit()
    else:
        print("You didn't search tree.")
        print("You are now walking deeper into forest.")
        time.sleep(3)
        print("You saw a weird looking man sitting on a chair alone in the middle of the forest.")
        answer3=input("Do you want to talk with him?(yes or no)")
        if answer3=="yes":
            print("The man helped you and said you to search treasure in castle.")
            print("he is offering you to give a box.")
            answer4=input("do you want to take this box(yes or no)")
            if answer4=="yes":
                print("you lost the game because the box sent you a diffrent place that is far away from treasure")
                quit()
            else:
                print("you are now running")
                time.sleep(1)
                print("still running")
                time.sleep(1)
                print("you are finally in the castle")
                answer5=input("do you want to go upstairs or downstairs?")
                if answer5=="upstairs":
                    print("you searched everywhere and found a writing on the wall")
                    print("it says:'you should jump down to find the treasure'")
                    answer6=input("will you jump?(yes or no)")
                    if answer6=="yes":
                        print("you died,it was a trap")
                        quit()
                    else:
                        print("congrulations "+name+"!")
                        time.sleep(1)
                        print("YES YOU WON THE GAME BECAUSE YOU FOUND THE TREASUR IT WAS JUST HIDDEN UNDER A BLANKET!")
                
                else:
                    print("you are now searching the cellar")
                    time.sleep(3)
                    print("you found nothing here. and you lost the game because you were so tired to find")
                    quit()
        else:
            print("you got lost in the forest and lost the game.")
            quit()
else:
    print("you fell into a hole and you lost the game")
    quit()