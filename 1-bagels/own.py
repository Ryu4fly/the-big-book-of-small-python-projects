import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
  print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:   That meas:
  Pico        One digit is correct but in the wrong position.
  Fermi       One digit is correct and in the right position.
  Bagels      No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

  while True:
    secret_num = getSecretNum()
    print('I have thought of a {} digit number'.format(NUM_DIGITS))
    print('You have {} guesses'.format(MAX_GUESSES))
    num_guesses = 1

    while num_guesses <= MAX_GUESSES:
      print('Guess #{}:'.format(num_guesses))
      guess = input('> ')
      clues = getClues(guess, secret_num)
      print(clues)

      num_guesses += 1

      if guess == secret_num:
        break

      if num_guesses > MAX_GUESSES:
        print('You ran out of guesses!')
        print('The correct number is {}'.format(secret_num))

    print('Play again? (y/n)')
    if not input('> ').lower().startswith('y'):
      break
  print('Thanks for playing!')

def getSecretNum():
  numbers = list('0123456789')
  random.shuffle(numbers)
  secret_num = ''
  for i in range(NUM_DIGITS):
    secret_num += str(numbers[i])
  return secret_num

def getClues(guess, secret):
  if guess == secret:
    return "That's correct! It's {}".format(secret)

  clues = []

  for i in range(len(guess)):
    if guess[i] == secret[i]:
      clues.append('Fermi')
    elif guess[i] in secret:
      clues.append('Pico')

  if len(clues) == 0:
    return 'Bagel'

  clues.sort()
  return ' '.join(clues)

if __name__=='__main__':
  main()
