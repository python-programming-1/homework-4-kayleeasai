#HW4

import random
ComputerWins=0
HumanWins=0
while True:
     print('Make a move!(R/P/S):')
     Human=input()
     Computer=random.choice(['R','P','S'])
     if Human==Computer:
         print('Draw!')
     elif Human=='P':
         if Computer=='S':
             print('You chose '+Human+' and the computer chose '+Computer)
             print('Computer Wins!')
             ComputerWins+=1
         elif Computer=='R':
             print('You chose '+Human+' and the computer chose '+Computer)
             print('You Win!')
             HumanWins+=1
     elif Human=='S':
         if Computer=='R':
             print('You chose '+Human+' and the computer chose '+Computer)
             print('Computer Wins!')
             ComputerWins+=1
         elif Computer=='P':
             print('You chose '+Human+' and the computer chose '+Computer)
             print('You Win!')
             HumanWins+=1
     elif Human=='R':
         if Computer=='P':
             print('You chose '+Human+' and the computer chose '+Computer)
             print('Computer Wins!')
             ComputerWins+=1
         elif Computer=='S':
             print('You chose '+Human+' and the computer chose '+Computer)
             print('You Win!')
             HumanWins+=1
     elif Human=='sc':
         print('Human: '+str(HumanWins)+', Computer: '+str(ComputerWins))
     print('Do you want to play again? (y/n)')
     Play=input()
     if Play == 'n':
         print('Thanks, Bye!!!')
         break

