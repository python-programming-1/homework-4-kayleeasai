Last login: Mon Jul 22 18:33:55 on ttys002
(base) Kaylees-MacBook-Pro:~ kayleeasai$ cd homework-4-kayleeasai
(base) Kaylees-MacBook-Pro:homework-4-kayleeasai kayleeasai$ python
Python 3.7.3 (default, Mar 27 2019, 16:54:48) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> #HW4
... 
>>> import random
>>> ComputerWins=0
>>> HumanWins=0
>>> while True:
...     print('Make a move!(R/P/S):')
...     Human=input()
...     Computer=random.choice(['R','P','S'])
...     if Human==Computer:
...         print('Draw!')
...     elif Human=='P':
...         if Computer=='S':
...             print('You chose '+Human+' and the computer chose '+Computer)
...             print('Computer Wins!')
...             ComputerWins+=1
...         elif Computer=='R':
...             print('You chose '+Human+' and the computer chose '+Computer)
...             print('You Win!')
...             HumanWins+=1
...     elif Human=='S':
...         if Computer=='R':
...             print('You chose '+Human+' and the computer chose '+Computer)
...             print('Computer Wins!')
...             ComputerWins+=1
...         elif Computer=='P':
...             print('You chose '+Human+' and the computer chose '+Computer)
...             print('You Win!')
...             HumanWins+=1
...     elif Human=='R':
...         if Computer=='P':
...             print('You chose '+Human+' and the computer chose '+Computer)
...             print('Computer Wins!')
...             ComputerWins+=1
...         elif Computer=='S':
...             print('You chose '+Human+' and the computer chose '+Computer)
...             print('You Win!')
...             HumanWins+=1
...     elif Human=='sc':
...         print('Human: '+str(HumanWins)+', Computer: '+str(ComputerWins))
...     print('Do you want to play again? (y/n)')
...     Play=input()
...     if Play == 'n':
...         print('Thanks, Bye!!!')
...         break
... 
Make a move!(R/P/S):
R
You chose R and the computer chose S
You Win!
Do you want to play again? (y/n)
y
Make a move!(R/P/S):
S
You chose S and the computer chose P
You Win!
Do you want to play again? (y/n)
y
Make a move!(R/P/S):
sc
Human: 2, Computer: 0
Do you want to play again? (y/n)
n
Thanks, Bye!!!
>>> 
