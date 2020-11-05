import random
import words

words= words.words()
wordCollection= list(words.split())

randomNumber= random.randint(0, len(wordCollection)-1)
chosenWord= wordCollection[randomNumber]

guessedLetter=""

print(chosenWord)


for letter in range(len(chosenWord)):
  guessedLetter+= "*"

print(guessedLetter)