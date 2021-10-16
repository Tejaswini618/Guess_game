import random
print("Welcome to Guess Game...")
low,high =[int(x) for x in input("Enter the lower and upper limit for guess: ").split()]
n = 0
count = 0
num = random.randint(low,high)
while(n != num):
    n = int(input())
    if(n>0):
        if(n<num):
            print("Number smaller than guess!")
            print("Try Again")
            count = count+1
        elif(n>num):
            print("Number larger than guess!")
            print("Try Again")
            count = count+1
        else:
            print("Congratulations! You made it...")
            print("Number of guess: ",count)
            
    else:
        print("Give up!")
        print("The number is: ",num)
        break
