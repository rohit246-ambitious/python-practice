import random

print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random float between 0 and 1:", random.random()) 

print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))
print("Random sample of 2 elements from a list:", random.sample(range(10), 2))
print("Shuffled list:", random.sample(range(10), 10))   

print("Random uniform float between 1 and 10:", random.uniform(1, 10))
print("Random gauss float with mu=0 and sigma=1:", random.gauss(0, 1))

print("Random betavariate with alpha=2 and beta=5:", random.betavariate(2, 5))
print("Random expovariate with lambda=1.5:", random.expovariate(1.5))
print("Random triangular float between 1 and 10 with mode=5:", random.triangular(1, 10, 5))
print("Random choice from a range with step 2:", random.randrange(0, 20, 2))    
# Demonstrating various functions from the random module

#shuffle requires a mutable sequence, so we create a list
lst = list(range(10))
random.shuffle(lst) 
print("Shuffled list using shuffle():", lst)
