import time

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
abcup = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", ",", ".", "<", ">", "/", "?", "`", "~", " "]



text = input("What would you want to print out? ")
DONEletters = []
num = 0

for i in text:
    if i in abc:
        while i != abc[num]:
            time.sleep(0.05)
            print(*DONEletters, sep="", end="")
            print(abc[num], end="\n")
            num += 1
        time.sleep(0.05)
        DONEletters.append(abc[num])
        print(*DONEletters, sep="")
        num = 0
    elif i in abcup:
        while i != abcup[num]:
            time.sleep(0.05)
            print(*DONEletters, sep="", end="")
            print(abcup[num], end="\n")
            num += 1
        time.sleep(0.05)
        DONEletters.append(abcup[num])
        print(*DONEletters, sep="")
        num = 0
    elif i in special_chars:
        while i != special_chars[num]:
            time.sleep(0.05)
            print(*DONEletters, sep="", end="")
            print(special_chars[num], end="\n")
            num += 1
        time.sleep(0.05)
        DONEletters.append(special_chars[num])
        print(*DONEletters, sep="")
        num = 0
    else:
        raise ValueError(f"Unsupported character found: {i}")