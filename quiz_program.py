# A quiz program.

def start_program():
    print('Welcome to the quiz.')
    print('You will choose one of two topics, answer the questions and then you will get your score.\n')
    print('Good Luck!\n')

""" A method that has a tuple of three dictionary that have questions for the test, will recieve 
 a number when called and will return one of the two dictionaries. """

def what_topic(topic_num):
    qs_and_As = (
        { # first dictionary is art.
            'Who painted the Mona Lisa? ': 'Leonardo Da Vinci',
            'What precious stone is used to make the artist\'s pigment ultramarine? ': 'Lapiz lazuli',
            'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city? ': 'Chicago',
            'Which kid\'s TV characters are named after Renaissance artists? ': 'Teenage Mutant Ninja Turtles',
            'The graphite in an artist\'s pencil is made of what chemical element? ': 'Carbon'
        },

        { # second dictionary is space.
            'Which planet is closest to the sun? ': 'Mercury',
            'Which planet spins in the opposite direction to all the others in the solar system? ': 'Venus',
            'How many moons does Mars have? ': '2',
            'What was the first human-made object to leave the solar system? ': 'Voyager 1',
            'When an asteroid enters the Earth\'s atmosphere and burns up, it is known as what? ': 'Meteor'
        },

        { # Another one - third dictionary is on sports
            'Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after? ': 'Simone Biles',
            'Which country has won the soccer world cup the most times? ': 'Brasil',
            'What does MLB stand for? ': 'Major League Baseball'
        }
    )
    return qs_and_As[topic_num]


# This method will ask user for the topic that s/he want to be tested on, and will return that value when called.
def user_topic_choice():
    while True: # repeat until told otherwise.
        topic = input('Enter the number 1 for Art, 2 for Space questions or 3 for Sports: ')
        if topic == '1' or topic == '2' or topic == '3':
            print() # print an empty line
            topic = int(topic) # convert from string to int
            # if the user enters 1, 2 or 3, return the value and break from the loop.
            return topic - 1
            break
        

""" This method will be passed a dictionary of questions when called, will loop over the questions (keys and values)
    to ask the user and will calcualte and return the score. """
def start_test(dictionary):
    score = 0; # A counter for the score
    d_items = dictionary.items(); # items (key and value pairs of the dictionary)
    for key, value in d_items:
        question = input(key)
        # check if answer is correct, but ignore case
        if question.lower() == value.lower():
            print('Correct!') # if correct print this and add 1 to the score
            score = score + 1
        else: # if not correct, print this:
            print(f'Sorry the answer is: {value}')
    return score # return the score

# When this method is called it will be passed the score of the test, and the number of questions.
# And it will print the score of the user.
def scoring(score, num_of_dict_items):
    if score == num_of_dict_items:
        print(f'\ncongrats! You got {score} out of {score} \n')
    else:
        print(f'\nYour score is {score} out of {num_of_dict_items}\n')


# Call the methods and store their responses in variables if they return anything:

start_program()
num = user_topic_choice() # get the user choice, store it in this variable.
response = what_topic(num) # pass the choice this method and store its response in the variable
score = start_test(response) # pass the response (dectioanry) to this method and store the score in this variable
scoring(score, len(response)) # call this method and pass these values to it.

print('End of quiz!')



