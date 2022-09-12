import random
x = (random.randint(1, 20))
print ('i am thinking of a number between 1 and 20')
while True :
       print ('take a guess')
       a = int(input()) 
       if a < x :
          print ('Your guess is too low.')
          continue
       elif a > x :
          print ('Your guess is too high.')
          continue
       else:
          print ('Good job! You guessed my number in 4 guesses!')
          break



