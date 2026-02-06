#Task 1
a=int(input("Enter first no.: "))
b=int(input("Enter second no.: "))
def add(a, b):
    return(a+b)

c=add(a,b)
print(c)

#Task 2
marks = [78, 92, 67, 88, 45]
print(sum(marks))
print(max(marks))
print(min(marks))
print(sum(marks)/len(marks))

#Task 3
marks = [78, 92, 67, 88, 45]
def grades(marks):
    for mark in marks:
        if mark>90:
            print("Grade:A")
        elif mark>80:
            print("Grade:B")
        elif mark>70:
            print("Grade:C")
        elif mark>60:
            print("Grade:D")
        else:
            print("Grade:E")

grades(marks)