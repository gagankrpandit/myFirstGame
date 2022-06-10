# This is a game of rock, paper and scissors
import random
rock = 1
paper = 2
scissors = 3
print('computer turn, computer has chosen.')
comp = random.randint(1,3)
print('your turn, choose one: rock(1), paper(2), scissors(3)')
you = int(input())
if you > 3 or you < 1:
    print('please enter number between 1 and 3 only, rock(1), paper(2), scissors(3)')
def game(comp, you):
    if comp == you:
        print(f'its a tie, as computer chose {comp} and you chose {you}')
    elif comp == 1 and you == 2:
        print(f'You won, you chose paper and computer chose rock')
    elif comp == 2 and you == 1:
        print(f'Computer won, computer chose paper and you chose rock')
    elif comp == 3 and you == 1:
        print(f'You won, you chose rock and computer chose scissors')
    else:
        # comp == 1 and you == 3
        print(f'Computer won, computer chose rock and you chose scissors')
game(comp, you)
