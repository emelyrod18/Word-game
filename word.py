import random

words = [
    "bubblegum", "undertale", "roblox", "butterfly", "yourself", "python", "cheese", "sourdough",
    "nine", "clock", "flan", "alliteration", "mickey", "fortnite", "hacker"
]

random.shuffle(words)

total = 15
correct = 0
mistakes = 0

print("word game!!")

for i in range(total):
    print("word", i + 1, "of", total)
    print("type this word:", words[i])

    answer = input()

    if answer == words[i]:
        print("correct!")
        correct = correct + 1
    else:
        print("incorrect")
        mistakes = mistakes + 1
    
print("game overrr")
print("mistakes:", mistakes)

accuracy = (correct / total) * 100
print("accuracy:", accuracy, "%")