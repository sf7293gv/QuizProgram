# A quiz program.   
# 
""" More explanation needed here. A Python docstring uses triple double quotes. """ 

def start_program():   # does this start the program? How about calling this welcome_message() or instructions() or ?
    print('Welcome to the quiz.')
    print('You will choose one of two topics, answer the questions and then you will get your score.\n')
    print('Good Luck!\n')


# this could be a global variable. Several parts of the program read it. The function you had is just returning this so it's not really needed. 
# What about using a dictionary instead of a tuple? The keys are the topics, values are Qs and As
qs_and_As = {
    'art': { # first dictionary is art. Now you don't need this comment 
        'Who painted the Mona Lisa? ': 'Leonardo Da Vinci',
        'What precious stone is used to make the artist\'s pigment ultramarine? ': 'Lapiz lazuli',
        'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city? ': 'Chicago',
        'Which kid\'s TV characters are named after Renaissance artists? ': 'Teenage Mutant Ninja Turtles',
        'The graphite in an artist\'s pencil is made of what chemical element? ': 'Carbon'
    },

    'space': {
        'Which planet is closest to the sun? ': 'Mercury',
        'Which planet spins in the opposite direction to all the others in the solar system? ': 'Venus',
        'How many moons does Mars have? ': '2',
        'What was the first human-made object to leave the solar system? ': 'Voyager 1',
        'When an asteroid enters the Earth\'s atmosphere and burns up, it is known as what? ': 'Meteor'
    },

    'sport': {
        'Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after? ': 'Simone Biles',
        'Which country has won the soccer world cup the most times? ': 'Brasil',
        'What does MLB stand for? ': 'Major League Baseball'
    }
}



# This method will ask user for the topic that s/he want to be tested on, and will return that value when called.
def user_topic_choice():
    while True: # repeat until told otherwise.
        # How will this handle more topics? 

        # Build dictionary of numbers 1, 2, 3 .... keys and topic name values 
        numbers_and_topics = {} 


        number = 1
        for topic in qs_and_As:
            numbers_and_topics[str(number)] = topic  # Save numbers as strings to simplify input and avoid converting strings to numbers and ValueErrors
            number += 1

        # numbers_and_topics will be {'1': 'art', '2': 'space', '3': 'sport'} for this data 
        print('Your choices are:')

        for number, topic in numbers_and_topics.items():
            print(f'Enter {number} for {topic}')

        number_selected = input('Enter your chosen topic number')

        while number_selected not in numbers_and_topics:
            print('Not a valid topic, try again: ')
            number_selected = input('Enter your chosen topic number: ')
        
        topic_selected = numbers_and_topics[number_selected] 
        
        return topic_selected  # Return the topic name  - no longer need indexes if data is in a dictionary


""" This method will be passed a dictionary of questions when called, will loop over the questions (keys and values)
    to ask the user and will calcualte and return the score. """
def start_test(questions):
    score = 0; # A counter for the score
    # Variable names - be more specific. 
    for question, correct_answer in questions.items():  # more common to combine these lines    
        user_answer = input(question)  # is question the best name for the user's answer? 
        # check if answer is correct, but ignore case
        if user_answer.lower() == correct_answer.lower():
            print('Correct!') # if correct print this and add 1 to the score
            score = score + 1
        else: # if not correct, print this:
            print(f'Sorry the answer is: {correct_answer}')
    return score # return the score

# When this method is called it will be passed the score of the test, and the number of questions.
# And it will print the score of the user.
def scoring(score, number_of_questions):  # be specfic with names. 
    # Does this function need to know the questions are in a dictionary? All it needs to know is the number of questions and how many the user got right. 
    if score == number_of_questions:
        print(f'\ncongrats! You got {score} out of {score} \n')
    else:
        print(f'\nYour score is {score} out of {number_of_questions}\n')


# Call the methods and store their responses in variables if they return anything - do you need this comment?

# create a main method for high-level tasks in the program
def main():
    start_program()
    topic = user_topic_choice() # get the user choice, store it in this variable. - do you need this comment?
    questions = qs_and_As[topic]
    # response = what_topic(num) # pass the choice this method and store its response in the variable  -- or this one? A better variable name than 'response' would make this more self-documenting
    score = start_test(questions) # pass the response (dectioanry) to this method and store the score in this variable   -- or even this one? 
    scoring(score, len(questions)) # call this method and pass these values to it. - do you need this comment?

    print('End of quiz!')


main()
