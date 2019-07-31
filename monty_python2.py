#!/usr/bin/env_python3

def main():
    round = 0 
    while(True):
        round = round + 1
        print('Finish the movie title, "Monty Python\'s The life of ____"')
        answer = input('your guess -->')
       #if (answer == 'Brian'):
        if (answer.lower() == 'brian'):
            print('correct')
            break
        elif (round == 3):
            print('sorry the answer is brian.')
            break
        else:
            print('sorry, try again')
main()
