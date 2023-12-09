#!/usr/bin/env python3

def happy_new_year():
    counting =10
    while counting >=1:
        print(counting)
        counting -=1
    print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
     numbers=[num ** 2 for num in int_list]
     return numbers

print(square_integers([1, 2, 3, 4, 5]))

def fizzbuzz():
    for nums in range(1, 101):
        if nums % 3 == 0 and nums % 5 == 0:
            print("FizzBuzz")
        elif nums % 3 == 0:
            print("Fizz")
        elif nums % 5 == 0:
            print("Buzz")
        else:
            print(nums)


fizzbuzz()



# i = 0
# while i < 5:
#   print("Looping!")
#   i += 1