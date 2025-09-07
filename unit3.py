def sum_of_squares(n) :
    answer = 0 
    string = ""
    for i in range(n+1):
        if i>0:
            string= f"{string}{i**2} + "
            answer+=i**2
    print( f"{string} = {answer}" )
        
sum_of_squares(1)
sum_of_squares(2)
sum_of_squares(3)
sum_of_squares(4)

def count_occurrences(full, part) :
    count = 0
    for i in range(len(full)) :
        if full[i:i+len(part)]==part:
            count+=1
    print (count)
    
count_occurrences("Mississippi", "iss")
count_occurrences("banananana", "na")

def reverse(word) :
    new = ""
    for i in range(len(word)) :
        new = word[i:i+1]+new
    print(new)
reverse("bad")
reverse("Hello, world!")
reverse("tacocat")

def factorial(n) :
    answer = 1 
    string = ""
    for i in range(n+1):
        if i>0:
            string= f"{string}{i} x "
            answer=answer*i
    print( f"{string} = {answer}" )

factorial(3)
factorial(4)
factorial(7)

def interlace(first, second) :
    new = ""
    for i in range(len(first)) :
        new = new+first[i:i+1]
        new = new+second[i:i+1]
    print(new)

interlace("abc", "123")
interlace("bed", "ras")

def count_occurrences(full, part) :
    count = 0
    for i in range(len(full)) :
        if full[i:i+len(part)]==part:
            count+=1
    print (count)
    
def find_2nd(word) :
    count = 0
    one =False
    for i in range(len(word)) :
        if word[i:i+1]=="a" and one==True :
            count=i
            i=len(word)
        if word[i:i+1]=="a":
            one=True
    print (count)
find_2nd("banana")
find_2nd("happy birthday")

def add_na(amount) :
    new = "ba"
    for i in range(amount) :
        new = new+"na"
    print(new)

add_na(0)
add_na(2)
add_na(6)

def sum_powers(n) :
    last = 1
    answer = 0 
    string = "1 + "
    for i in range(n):
            string= f"{string}{last*2} + "
            last=last*2
            answer+=last
    print( f"{string} = {answer}" )
    
sum_powers(0)
sum_powers(3)
        