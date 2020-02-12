#Michael Suter
#A program with a bunch of self made operations
#2/11/2020
from statistics import mode
print("Hello World, this code is dedicated to list operations, enter 5 numbers")

number_list = []

for num in range(0,5):
    val = int(input("Enter a number>>>"))
    number_list.append(val)


print("Ok here's your list", number_list)
print("Now lets sort this list")
input("Press Enter to advance>>>")
number_list.sort()
print(number_list)

input("Enter to advance")

print("Now lets add all these")
total = 0
for numbers in number_list:
    total = total + int(numbers)
    print(total)

print("And multiply...")
total2 = 1
for number in number_list:
    total2 = total2 * int(number)
    print(total2)

print("Now that that's over lets find the mean, median and mode of the data you entered")
print("First we will find the mean")
input("Enter>>>")
mean = int(total) / 5
print(mean)

input("Enter to advance")
print("Now we will find the median")
print(number_list[2])
print("Lastly we will print the mode, if there is one.")
input("Enter to advance")


def mode_check():
    if len(number_list) == len(set(number_list)):
        return print(False, "there is no mode")
    else:
        print("Heres the mode", mode(number_list))


mode_check()

print("SIKE you thought this was over! It just keeps going!")
print("Now I'll find the largest and smallest number in the list.")

input("Enter to advance")

print(f"Here is the highest number, {number_list[4]}")
print(f"Here is the lowest number, {number_list[0]}")

print("Now I will remove any duplicates within the list you created")

number_list = list(set(number_list))
print(f"Now here is your list, {number_list}")

input("Enter to advance")
print("Lastly I will remove the odd numbers then the evens from the list")

even_list = []
odd_list = []

for num in number_list:
    if num % 2 != 0:
        even_list.append(num)

print("Here is the list without even numbers", even_list)

for num in number_list:
    if num % 2 == 0: # % 2 checks to see if the number is divisible by 2
        odd_list.append(num)

print("Here is the list without odd numbers", odd_list)

input("Enter to advance")
print("Guess a number and ill tell you if its in the list or not ")

guess = int(input("Enter your guess here>>>"))
if guess == number_list[0] or guess == number_list[1] or guess == number_list[2] or guess == number_list[3] or guess == number_list[4]:
    print("This number is in the list!")
else:
    print("This number is not in the list")

print('This is your list', number_list)
print("That is all Goodbye...")
