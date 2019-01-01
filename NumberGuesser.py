import random
rand = random.randint(0,100)
while True:
    inputX = input("Enter a number")
    inputX = int(inputX)
    if(inputX > rand):
        print("Too High")
    if(inputX < rand):
        print("Too Low")
    if(inputX == rand):
        print("Good Job")
        break;

