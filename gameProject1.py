import random
print("To end the game enter (N or n) ")
user_score = 0
cpu_score = 0
while True:
   choices=["rock","paper","scissor"]
   user = input("User choice (Rock,Paper or Scissor)? ")
   if user == "N" or user == "n":
      break
   if user in choices:
      random_choice=random.choice(choices)
      computer = random_choice
      print(f"cpu: {computer}")
 
   if user == computer:
      print("Game Tie!")
   
   elif user == "rock":
      if computer == "paper":
         print("You lose! Paper Rock")
         cpu_score +=1

      else:
         print("You Win! Rock smashes Scissor")
         user_score+=1

   elif user == "paper":
      if computer == "rock":
         print("You Win! paper cover rock")
         user_score += 1
      else:
         print("You lose.... scissor cut paper")
         cpu_score += 1
         
   elif user == "scissor":
      if computer == "rock":
         print("You lose.... Rock smashes Scissor")
         cpu_score += 1
      else:
         print("You win! scissor cut paper")
         user_score +=1
   else:
      print("enter valid word")



print(f"final scores cpu score: {cpu_score} and user score: {user_score}")
if cpu_score == user_score:
   print("score are equal")
elif cpu_score > user_score:
   print(f"Game Winner is computer highest score : {cpu_score}")
else:
   print(f"Game Winner is User highest score : {user_score}")