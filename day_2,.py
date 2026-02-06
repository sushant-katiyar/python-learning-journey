#Task 1
while True:    
    num = int(input("enter your number: "))
    if num>0:
        print("num is positive")
    elif num<0:
        print("num is negative")
    else:
        print("num is zero")
    
# Task 2
while True:    
    num = int(input("enter a number: "))
    for i in range(1, num+1):
        if i%2==0:
            print(i)

#Task 3
while True:    
    marks = int(input("enter your marks: "))
    if marks>=90:
        print("A")
    elif marks>=75:
        print("B")
    elif marks>=50:
        print("C")
    else:
        print("D")
    