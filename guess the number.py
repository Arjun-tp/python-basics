# guess the number
guess_count = 1
while guess_count <= 5:
    print('*' * guess_count)
    guess_count += 1
print("Done")

secret_number = 9
guess_count = 1
guess_limit = 3
while guess_count <= guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You WIN!!")
        break

else:
    print('Sorry. You failed!')
