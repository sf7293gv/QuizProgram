# A quiz program. 
print('Welcome!\n')
print('This is a random questions quiz on the topic of Art or Space.\n'
        'You will choose one of the two topics, and answer the questions and then you will get your score.\n')
print('Good Luck!\n')

""" A method that has a tuple of two dictionary that have questions for the test, will recieve 
 a number when called and will return one of the two dictionaries. """

def what_topic(topic_num):
    qs_and_As = (
        { # first dictionary is art.
            'Who painted the Mona Lisa? ': 'Leonardo Da Vinci',
            'What precious stone is used to make the artist\'s pigment ultramarine? ': 'Lapiz lazuli',
            'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city? ': 'Chicago'
        },

        { # second dictionary is space.
            'Which planet is closest to the sun? ': 'Mercury',
            'Which planet spins in the opposite direction to all the others in the solar system? ': 'Venus',
            'How many moons does Mars have? ': '2'
        }
    )
    return qs_and_As[topic_num]


# This method will ask user for the topic that s/he want to be tested on, and will return that value when called.
def user_topic_choice():
    while True: # repeat until told otherwise.
        topic = input('Enter the number 0 for art, and 1 for space questions: ')
        topic = int(topic) # convert from string to int
        if topic == 0 or topic == 1:
            # if the user enters 0 or 1, return the value and break from the loop.
            return topic
            break
        else:
            topic = input('Please enter the number 0 for art, and 1 for space: ')

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
        print(f'Congrats! You got {score} out of {score}')
    else:
        print(f'Your score is {score} out of {num_of_dict_items}')


# Call the methods and store their responses in variables if they return anything:

num = user_topic_choice() # get the user choice, store it in this variable.
response = what_topic(num) # pass the choice this method and store its response in the variable
score = start_test(response) # pass the response (dectioanry) to this method and store the score in this variable
scoring(score, len(response)) # call this method and pass these values to it.
print('End of quiz!')



