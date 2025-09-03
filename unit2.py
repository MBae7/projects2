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
    
testGreeting("Mia", "Hello, Mia, how are you?") 
testGreeting("Dr. Seuss", "Hello, Dr. Seuss, how are you?")   
