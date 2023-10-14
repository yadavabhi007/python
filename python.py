# import requests
# url = "http:127.0.0:8000/api/add-student/"
# data = {
#   "first_name": "Abhishek",
#   "last_name": "Yadav",
#   "age": 26,
#   "phone": "+918080808080",
# }
# post_data = requests.post(url=url, data=data)
# my_data = post_data.json()
# print(my_data)


# t=(3,4,[5,6])
# t[2][1]=7
# print(t)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[1 : : 2])


# salary_in_usd = {'jack': 100, 'michael': 200, 'guido': 300}
# usd_to_inr = 75.10
# new_salary = {item:value*usd_to_inr for (item,value) in salary_in_usd.items()}
# print(new_salary)


# num = 4
# for i in range (2,num):
#     if num % i == 0:
#         print('Not Prime')
#         break
# else:
#     print('Prime')


# num=int(input("Enter range : "))
# print("Prime numbers : ", end=' ')
# for n in range(2, num+1):
#     for i in range(2, n):
#         if n%i==0:
#             break
#     else:
#         print(n, end=' ')


# n = [1,5,7,4,2,8,1]
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i]>n[j]:
#             n[i],n[j]=n[j],n[i]
# print(n[len(n)::-1])


# def fib(n):
#     a = 0
#     b = 1
#     if n<=0:
#         print('Enter number greater than 0')
#     elif n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#     for i in range(2,n):
#         c = a + b
#         a = b
#         b = c
#         print (c)
# fib(-4)


# f = lambda a : a*a
# print(f(6))


# for i in range(4):
#     for j in range(4-i):
#         print('#', end='')
#     print()


# def triangle(n):
#     # number of spaces
#     k = n - 1
#     # outer loop to handle number of rows
#     for i in range(0, n):
#         # inner loop to handle number spaces
#         # values changing acc. to requirement
#         for j in range(0, k):
#             print(end=" ")
#         # decrementing k after each loop
#         k = k - 1
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i+1):
#             # printing stars
#             print("* ", end="")
#         # inner loop to handle number of columns
#         # ending line after each row
#         print("\r")
# n = int(input())
# triangle(n)


# def binaryToDecimal(val):
#     return int(val, 2)
# print(binaryToDecimal('111'))
# print(bin(111))


# def decimalToBinary(val):
#     if val >= 1:
#     # recursive function call
#         decimalToBinary(val // 2)
#     # printing remainder from each function call
#     print(val % 2, end = '')
# val = int(input())
# decimalToBinary(val)



# str = 'abhishek'
# for i in str:
#     if i=='e':
#         print('f', end='')
#     else:
#         print(i, end='')


# a = 27
# b = 6
# a = a^b
# b = a^b
# a = a^b
# print(a)
# print(b)


# for i in range(1,11):
#     if i%3==0:
#         continue
#     print(i)


# from numpy import *
# m = matrix('1,2; 4,5')
# print(diagonal(m))
# print(m.max())


# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# result = fact(5)
# print(result)


# a = [1,4,6,3,7,8]
# b = list(filter(lambda n : n%2!=0, a))
# print(b)


# a = [1,4,6,3,7,8]
# b = list(map(lambda n : n*2, a))
# print(b)


# t = tuple(map(int, input().split()))
# print(t)


# number=int(input("Enter a number :"))
# rev=0
# while(number!=0):
#     digit=number%10
#     rev=(rev*10)+digit
#     number=number//10
# print(rev)


# input_string = "Hello, World!"
# reversed_str = ""
# for char in input_string:
#     reversed_str = char + reversed_str
# print(reversed_str)


# def topten():
#     n = 1
#     while n<=10:
#         sq = n*n
#         yield sq
#         n += 1
# values = topten()
# for i in values:
#     print (i)


# class A:
#     def __str__(self):
#         return '1'
# class B(A):
#     def __init__(self):
#         super().__init__()
# a1 = A()
# b1 = B()
# print(a1, b1)


# class MyClass:
#     def __init__(self):
#         self.__my_var = 42

#     def __my_method(self):
#         print("This is a private method.")

# class SubClass(MyClass):
#     def print_private_var(self):
#         print(self._MyClass__my_var)  # Accessing the private attribute from the superclass

#     def call_private_method(self):
#         self._MyClass__my_method()  # Accessing the private method from the superclass

# # Create an instance of SubClass
# obj = SubClass()

# obj.print_private_var()
# obj.call_private_method()


# a = [1,2,7,4]
# b = []
# j = len(a)-1
# while j>=0:
#     b.append(a[j])
#     j-=1
# print(b)


# a = [1,2,7,4]
# b = [a[i] for i in range(len(a)-1,-1,-1)]
# print(b)


# a = range(5,12,2)
# b = list(a)
# print(b)


# a = "this is     a   cat."
# b = ' '.join(a.split())
# print(b)




# def sum_of_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_of_digits(n // 10)
    
# try:
#     num = int(input('Enter A Positive Integer: '))
#     if num < 1:
#         print('Please Enter A Positive Integer')
#     else:
#         digit_sum = sum_of_digits(num)
#         print(f'The Sum Of Gigits In {num} Is {digit_sum}')
# except ValueError:
#     print('Please Enter A Positive Integer')







