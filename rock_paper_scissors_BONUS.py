#HW4_BONUS

import random
ComputerWins=0
HumanHistory=['','']
HumanWins=0
while True:
     print('Make a move!(R/P/S):')
     Human=input()
     HumanHistory.append(Human)
     if Human==HumanHistory[-1]==HumanHistory[-2]==HumanHistory[-3]:
         if Human=='P':
             Computer='S'
         elif Human=='R':
             Computer='P'
         elif Human=='S':
             Computer='R'
     else:
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

