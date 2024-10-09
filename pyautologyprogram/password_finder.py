import string, random

pasw=input("enter your password :- ")
ch=string.printable 
 
while True:
    pGuess=random.choices(ch, k=len(pasw))
    pGuess=''.join(pGuess)
    print(pGuess)
    
    
    if pasw==pGuess:
        print(f"\nMatch password is :{pGuess}")
        break
    
 