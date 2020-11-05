import random
import words


    

words= words.words()
wordCollection= list(words.split())
randomNumber= random.randint(0, len(wordCollection)-1)
chosenWord= wordCollection[randomNumber].lower()
unknownWord=""

print(chosenWord)

for letter in range(len(chosenWord)):
  unknownWord+= "*"

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

      print(unknownWord)
      print("Correct guess!")

      if '*' in unknownWord:
        gameState= True
      else:
        gameState= False
        print("")
        print("You Won!")
  else:
    print("Wrong Guess!")
    print(unknownWord)

