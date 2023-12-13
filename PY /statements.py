# a = int(input("Enter the number : "))
# print('square root of ', a, a**0.5)

# l, b = float(input("Enter the length : ")), float(input("Enter the breadth : "))
# print("Area : ", l*b, " ,", "Perimeter : ", 2 * (l + b))

# a,b = int(input("Enter 1st numbers : ")), int(input("Enter 2nd numbers : "))
# c = a
# a = b
# b = c

# print("Swapping with third variable : ",a,b)
# a,b = int(input("Enter 1st numbers : ")), int(input("Enter 2nd numbers : "))
# b,a = a,b
# print("swapping without third variable : ", a,b)

# # another way 
# a,b = int(input("Enter 1st numbers : ")), int(input("Enter 2nd numbers : "))
# print("a :",a," b :",b)
# a = a+b 
# b = a-b
# a = a-b
# print("After Swapping ")
# print("a:",a,"b:",b)

# # adding elements to list , set , tuples 

# n = int(input("Enter the size of list : "))
# l = list()
# for i in range(n):
#     l.append(int(input(f"Enter the {i} element : ")))
# print("list :",l)

# n = int(input("Enter the size of list : "))
# s = set()
# for i in range(n):
#     s.add(int(input(f"Enter the {i} element : ")))
# print("set :", s)

# n = int(input("Enter size "))
# t = tuple()
# l = list(t)
# for i in range(n):
#     l.append(int(input(f"Enter the {i} element : ")))

# t = tuple(l)
# print("tuple :", t)


n = int(input("Enter the number of rows : " ))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()
    
# factorial 
print("\nFactorial example : ")
n = int(input("Enter the number for factorial : "))
fact = 1
if n<0 : print("factorial does not exist !!")
elif n==0: print("Factorial of 0 is 1 ")
else :
    for i in range(1,n+1):
        fact *= i
print(f"Factorial of {n} with for loop : {fact}")

n = int(input("Enter the number for factorial : "))
fact = 1
i=1
if n<0 : print("factorial does not exist !!")
elif n==0: print("Factorial of 0 is 1 ")
else :
    while i <=n:
        fact *=i
        i+=1
        
print(f"Factorial of {n} with while loop : {fact}")

#Even odd with if else
print("\nEven odd with if else example : ")
n = int (input("Enter a number :"))
if (n%2)==0: print(f"{n} is even")
else: print(f"{n} is odd")

# checking the number
print("\nchecking the number with if elif else example : ")
number = 2+9j
if isinstance(number, int):
    print("Number is an integer.")
elif isinstance(number, list):
    print("Number is a list.")
elif isinstance(number, tuple):
    print("Number is a tuple.")
elif isinstance(number, set):
    print("Number is a set.")
elif isinstance(number, float):
    print("Number is a float data type.")
elif isinstance(number, str):
    print("Number is a string.")
else:
    print("Number is complex.")


# break continue pass
print("\nbreak continue pass example : ")
for letter in 'python':
    if letter == 't' or letter == '0':
        continue
    print('current letter:',letter)

for letter in 'python':
    if letter == 'y':
        break
    print('current letter:',letter)

for letter in 'python':
    if letter in ['p', 'y', 't', 'h']:
        print('hi')
        pass
    print('pass letter:',letter)

# ------------------------------------------------------------------------------------------------------------------------
# def fact(a):
#    if a == 1 or a==0:
#       return 1
#    return a *fact(a-1)

# x=int(input("Enter number "))
# fact = 1
# if x <0:
#    print("error 6000")
# else:
#    for i in range(1,x+1):
#       fact *= i
# print(f"Factorial of {x} is {fact}")

# factorial : : )
# n = int(input("Enter the number of fibonacci : "))
# if n <=0: print("Error : (--)")
# else:
#     l = [0,1]
#     for i in range(1,n-1):
#         l.append(l[-1]+l[-2])
#     print(l)

# n = int(input("Enter the number : "))
# num = n
# fact = 1
# while n!=0:
#     fact *= n
#     n = n-1 
# print (f"factorial of {num} is {fact}") 

