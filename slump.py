import random
looping = True
valu = 0
guesses = 0

chosennumber = random.randint(1, 100) #a random number gets chosen as the answer

while looping: #loops the function so you are able to guess more
    print("Input Number from 1 to 100:")

    try: #if a number is not written then it says "invalid"
     rnum = int(input())
    except ValueError:
     print("Invalid Symbol.")
     continue
    except KeyboardInterrupt: 
      break

    if valu < 9:
        if rnum < chosennumber: #tells you if the number is higher, lower or correct
            valu += 1
            guesses += 1
            print("Higher.")
        elif rnum > chosennumber:
            valu += 1
            guesses += 1
            print("Lower.")
        elif rnum == chosennumber:
            print("Right Answer.")
            print(f"Guesses: {guesses}")
            looping = False #turns off the loop after you guess the right answer
    elif valu <= 9:
        print("No guesses left.")
        looping = False 
    