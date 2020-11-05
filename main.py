import random
import words

words= words.words()
wordCollection= list(words.split())
randomNumber= random.randint(0, len(wordCollection)-1)
chosenWord= wordCollection[randomNumber]
unknownWord=""

print(chosenWord)

for letter in range(len(chosenWord)):
  unknownWord+= "*"

print(unknownWord)


guessedLetter= input("Enter Your Guess: ")
if guessedLetter in chosenWord:
     guessedIndex = chosenWord.index(guessedLetter)
     unknownLst= list(unknownWord)
     unknownLst[guessedIndex] = chosenWord[guessedIndex]
     updatedUnkown= "".join(unknownLst)
     print(updatedUnkown)
     print("Correct guess!")
else:
  print("Wrong Guess!")
    