import random

animals = ['elephant', 'bear', 'cheetah', 'giraffe', 'wolf', 'tiger', 'penguin',
           'rabbit', 'lion', 'monkey', 'rhinoceros', 'sheep', 'kangaroo', 'zebra']
fruits = ['apple', 'banana', 'grapes', 'mango', 'lime', 'watermelon', 'jackfruit',
          'guava', 'orange', 'papaya', 'pear', 'peach', 'pomegranate', 'strawberry']
stationary = ['pencil', 'eraser', 'sharpener', 'envelope', 'paper', 'stapler', 'folder',
              'marker', 'inkpot', 'calculator', 'glue', 'notebook', 'scissors', 'ruler']
foods = ['rice', 'beans', 'ofadarice', 'beansandcorn', 'amala', 'indomie', 'suya', 
         'friedpotatoes', 'spaghetti', 'friedrice', 'yam', 'fufu', 'egusisoup', 'moimoi']

while 1:
    words = animals + fruits + stationary + foods
    random_word=random.choice(words)
    print('***** WORD GUESSING GAME *****')
    if random_word in animals:
        print('Hint:It is an animal')
    elif random_word in fruits:
        print('Hint:It is a fruit')
    elif random_word in foods:
        print('Hint:It is a food')
    else:
        print('Hint:It is not a stationary item')
        
    user_guesses = ''
    chances = 5 

    while chances > 0:
        wrong_guess = 0
        for ch in random_word:
            if ch in user_guesses:
                print(ch, end = ' ')
            else:
                wrong_guess+=1
                print('_', end = ' ')
                
        if wrong_guess == 0:
            print('\nCongrats...You Won. The word is ', random_word)
            again = input('Do you like to play again?Y or N ')
            break
        guess = input('\nMake a guess ')
        user_guesses += guess 
        
        if guess not in random_word:
            chances-=1
            print(f'Wrong...You have {chances} more chances')
            if chances == 0:
                print('Game over... You Lose. The word is ', random_word)
        