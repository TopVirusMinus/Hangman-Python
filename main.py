import random
import words


    

words= words.words()
wordCollection= list(words.split())
randomNumber= random.randint(0, len(wordCollection)-1)
chosenWord= wordCollection[randomNumber].lower()
unknownWord=""
health = 10


for letter in range(len(chosenWord)):
  unknownWord+= "*"
print(unknownWord)
gameState = True
while gameState == True:

  guessedLetter= input("Enter Your Guess: ")
  if guessedLetter in chosenWord:
      for i in range(len(chosenWord)):
        if chosenWord[i] == guessedLetter:
          guessedIndex = chosenWord.index(guessedLetter)
          unknownLst= list(unknownWord)
          unknownLst[i] = chosenWord[i]
          unknownWord = "".join(unknownLst)
          unknownWord = unknownWord

      
      print("Correct guess!")
      print("Current health is: ", health)
      print(unknownWord)
      print("-----------------")
      print("")

      if '*' in unknownWord:
        gameState= True
      else:
        gameState= False
        mistakes= 10 - health
        print("You Won! , You Made: ", mistakes, "Mistakes!" )

  else:
    
    print("Wrong Guess!")
    health -= 1
    print("Current health is: ", health)
    print(unknownWord)
    print("-----------------")
    print("")
  
  if health == 0:
    print("You Lost")
    print("You Used All Your Health...")
    print("Word Was: ",chosenWord)
    gameState = False
