import random
d=["snake","gun","water"]
user_point=0
computer_point=0
chance=10
print("enter the user choice\n")
for i in range(10):
     x=str(input())
     y=choice=random.choice(d)
     
     if x==y:
          chance-=1
          user_point +=0
          computer_point +=0
          print("Match tie")
          print(f"userpoint.={user_point}:")
          print(f"computer point={computer_point}:")
          print(f"rem chance={chance}:")
          print(f"userchoose={x}:")
          print(f"computer choose={y}:")
          
          
    
          
                
     elif x=="snake" and y=="water":
         user_point +=1
         chance -=1
         print("user win the game")
         print(f"userpoint.={user_point}:")
         print(f"computer point.={computer_point}:")
         print(f"rem chance={chance }")
         print(f"userchoose={x}:")
         print(f"computerchoose={y}:")
     elif x=="water" and y=="gun":
         user_point +=1
         chance -=1
         print("user win the game👱")
         print(f"user point={user_point }")
         print(f"computer point.={computer_point}:")  
         print(f"rem chance={chance}:")
         print(f"userchoose={x}:") 
         print(f"computerchoose={y}:")     
     elif x=="snake" and y=="gun":
         computer_point +=1
         chance -=1
         print("computer win the game🔳")
         
         print(f"user point={user_point }:")
         print(f"computer point.={computer_point}:")      
         print(f"rem chance={chance }:")
         print(f"userchoose={x}:")
         print(f"computer choose={y}:")
     elif x=="water" and y=="snake":
         computer_point +=1
         chance -=1
         print("computer win the game")
         
         print(f"user point={user_point}:")
         print(f"computer point.={computer_point }:")
         print(f"rem chance={chance }:")
         print(f"user choose={x}:")
         print(f"computer choose={y}:")
     elif x=="gun" and y=="water":
         computer_point +=1
         chance -=1
         print("computer win the game")
         
         print(f"user point={user_point}:")
         print(f"computer point.={computer_point }:")
         print(f"rem chance={chance }:")
         print(f"userchoose={x}:")
         print(f"computer choose={y}:")
    
     elif x=="gun" and y=="snake":
         user_point +=1
         chance -=1
         print("user win the game")
         
         print(f"user point={user_point }:")
         print(f"computer point={computer_point }:")
         print(f"rem chance={chance }:")
         print(f"user choose={x}:")
         print(f"computer choose={y}:")
  
     else:
        print("wrong input")
        chance -=1




print("Game over")

if user_point>computer_point:
         print("\nyou win")
elif user_point<computer_point:
         print("\n you loss")
else:
         print("\n match tie")

print(f"userpoint={user_point}: computerpoint={computer_point }: remaning chance={chance}")
print("Game over 👍😍")
    

                  
         
         


         
         

          
         
         

          
