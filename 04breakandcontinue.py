number = 59
 
while True:
    guess = int(input('Enter an integer : '))
    if guess == number:
        # New block starts here
        break
 
        # New block ends here
    if guess < number:
        # Another block
        print('No, the number is higher than that, keep guessing')
        continue
        # You can do whatever you want in a block ...
    else:
        print('No, the number is a  lower than that, keep guessing')
        continue
        # you must have guessed > number to reach here
 
print('Bingo! you guessed it right.')
print('(but you do not win any prizes!)') 
print('Done') 

