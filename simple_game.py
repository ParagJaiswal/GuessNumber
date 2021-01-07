import random
print("When you want to exit the game press, q to stop")

score = 0

while True:
    num = random.randint(0,5)
    opt = input("Guess number from 0 to 5 = ")
    if opt== 'q':
        print("Game Over")
        break
    snum = int(opt)
    if num==snum:
        print("Congrats you choose the rigth answer")
        score += 10
        print("Your score is = ",score)
    else:
        print("Your guess was wrong, rigth number is = ",num)
        
