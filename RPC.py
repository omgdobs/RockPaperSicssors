
import random

r = 'rock'
p = 'paper'
s = 'scissors'
y = random.choice([r,p,s])
  
print(" Hello todya we are going to play rock, paper, sisers") 
x = input(" What is your choice of weapon, rock, paper, or scissors") 

# user chose rock and program chose rock
if x == r and y == r:
    print("I choose " + y +  " Wow you got luckey its a tie!")
# user choose rock and program chose paper
if x == r and y == p: 
    print("I choose " + y +  " Haha you lose")
# user chose rock and program chose sicssors
if x == r and y == s:
    print("I choose " + y + " You win this time") 
#user chose paper and program chose rock
if x == p and y == r:
    print("I choose " + y + " Wow you got luckey its a tie!")
#user chose paper and program chose paper
if x == p and y == p:
    print("I choose " + y + " Wow you got luckey its a tie!")
# user chose paper and program chose sicssors
if x == p  and y == s:
    print("I choose " + y + " Haha you lose")
# user chose sicssors and program chose rock
if x == s and y == r:
    print("I choose " + y + " Haha you lose")
# user chose sicssors and program chose paper
if x == s and y == p:
    print("I choose " + y + " You win this time")
# user chose sicssors and program chose sicssors
if x == s and y == s:
    print("i choose " + y + " Wow you got luckey tis a tie!")











# if user says r then say y if y = r print you tie
 
# if y = p and user input = s print  you lose hahaha and so on