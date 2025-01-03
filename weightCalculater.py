weight = input("Enter the weight")
unit = input("(L)bs or (K)g: ")
message = ''
if unit == 'L' or unit == 'l':
    message = f'You are {int(weight) * 0.453592} kg'
    print(message)
elif unit == 'K' or unit == 'k':
    message = f'You are {int(weight) * 2.20462} pounds'
    print(message)
else:
    print("Invalid entry!!")
