#!/usr/bin/env python
# coding: utf-8

# In[17]:


print("ROCK PAPER SCISSOR")
print("Winning Rules"+"\n 1. Rock vs Paper : paper wins"+"\n 2. Rock vs Scissor : Rock wins"
      +"\n 3. Scissor vs Paper : Scissor wins")
x=0
y=0
while(True):
    print("Choose between: \n* Rock \n* Paper \n* Scissor")
    user_input=input()
    user_input=user_input.lower()
    while True:
        if user_input not in ["rock","paper","scissor"]:
            print("Invalid Input")
        else:
            break
        user_input=input()
        user_input=user_input.lower()
            
    import random
    com_choice=random.choice(["rock","paper","scissor"])
    print("Computer Chose : "+ com_choice)
    
    print("\t"+ user_input + "\n \t vs \n"+"\t"+ com_choice)
    
    if (com_choice=="rock" and user_input=="paper") or (com_choice=="paper" and user_input=="rock"):
        result="paper"
    elif (com_choice=="rock" and user_input=="scissor") or (com_choice=="scissor" and user_input=="rock"):
        result="rock"
    else:
        result="scissor"
        
    
    if(result==user_input):
        print("\t---User wins---")
        x+=1
    elif(result==com_choice):
        print("\t---Computer wins---")
        y+=1
    elif(user_input==com_choice):
        print("\t---DRAW---")
        print("Play Again to Gain a Score.")
    
    inp=input("Do you want to play again ? (y/n)")
    inp= inp.lower()
     
    if inp=='y':
        continue
    elif inp=='n':
        break
    else:
        print("Please enter the correct literal.")
    
print("--------------Score Board Is-------------")
print("--------User------------Computer---------")
print("-\t",format(x,"d"),"\t\t",format(y,"d"),"\t\t-")


# In[ ]:




