import random

def greeting(name) : 
    final = "Hello, "+ name +", how are you?"
    return final

def testGreeting(name,expected) :
    if greeting(name)==expected :
        print(" Success! "+greeting(name))
        return True 
    else :
        print("FAIL "+greeting(name))
        return False 
    
#testGreeting("Mia", "Hello, Mia, how are you?") testGreeting("Dr. Seuss", "Hello, Dr. Seuss, how are you?")   

def attention(string) :
    cut =string[0:8]
    if cut =="Hey you!":
        return True
    else :
        return False

def testAttention(string, expected) :
    if attention(string) == expected :
        print("Success! "+string) 
    else :
        print("FAIL "+string[0:8])
        
#testAttention("Hey you! Come here", True) testAttention("Hi! I'm a frog", False)

def coinToss() :
    chance = random.randint(1, 2)
    if chance == 1 :
        result = "heads"
    elif chance ==2 :
        result = "tails"
    print(result)

for i in range(10) :
    coinToss()
    
    
def diceRoll() :
    num = random.randint(1, 6)
    print(num)

for i in range(10) :
    diceRoll()