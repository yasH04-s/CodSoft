import random
opt=int(input("if continue then 1 or to stop press 0"))
if(opt==1):
    user=input("enter choice: ")
    choice=["rock","paper","scissor"]
    cc=random.randint(0,2)
    print(choice[cc])
    if (choice[cc]=='rock'and user=='paper'):
      print("you won")
    elif (choice[cc]=='rock'and user=='scissor'):
      print("you lose")
    elif (choice[cc]=='paper'and user=='scissor'):
      print("you won")
    elif (choice[cc]=='paper'and user=='rock'):
      print("you won")
    elif (choice[cc]=='scissor'and user=='rock'):
      print("you won")
    elif (choice[cc]=='scissor'and user=='paper'):
      print("you lose")
else:
    print("Game ends!")