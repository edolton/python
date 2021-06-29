numbers = [1, 45, 31, 17, 60]

for number in numbers:
    if number % 8 == 0:
        print("The numbers are unacceptable")
        break
else:
    print("All numbers are fine")
