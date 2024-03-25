dailychallenge
1
sentence = input("Write a sentence: ")
if len(sentence) < 10:
    print("String not long enough.")
elif len(sentence) > 10:
    print("String too long.")
else:
    print("Perfect string.")

#2
if sentence:
    print("First character:", sentence[0])
    print("Last character:", sentence[-1])

#3
for i in range(1, len(sentence) + 1):
    print(sentence[:i])
    
#4
import random
characters = list(sentence)
random.shuffle(characters)
jumbled_text = ''.join(characters)
print(jumbled_text)
