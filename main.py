##################################################
'''
Q1: 
'''

sentence = ["It", "was", "a", "stormy", "night"]

##################################################
'''
Q2:
'''

sentence.insert(3, "dark")
sentence.insert(4, "and")

##################################################
'''
Q3:
'''

sentence[1] = "IS"

##################################################
'''
Q4:
'''

for word in sentence:
    if "a" in word:
        sentence.remove(word)

##################################################
'''
Q5:
'''

multiples = []
for i in range(10):
    multiples.append(i * 2)

##################################################
'''
Q6:
'''

def fill(list, number):
    new = []
    for i in range(len(list)):
        new.append(number)
    return new

##################################################
