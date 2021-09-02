from tkinter import *
import random

# This program will generate random simple multiplication questions (x * y)
# Where 0 <= x < 100 and 0 <= y < 100
root = Tk()

# Multiplication variables
x = 0
y = 0

# Score tracking variables
total_questions = 0
correct_questions = 0

response = StringVar()
question = StringVar()
num_correct = StringVar()
# Get random values for x and y
def getRandom():
    #Python functions will assume these primitive variables are local unless declared as global
    global x
    global y
    prev_x = x
    prev_y = y
    #If the two variables have the same values as the previous variables, get another random variable until it is a different value
    while x == prev_x:
        x = int(round(random.random(), 2) * 100)
    while y == prev_y:
        y = int(round(random.random(), 2) * 100)
    
    question.set(f"What is {x} times {y}?")

def generateResponse(answer):
    #Python functions will assume these primitive variables are local unless declared as global
    global x
    global y
    global total_questions
    global correct_questions
    correct_answer = x * y
    #Try in case answer cannot be converted to an int. If so, change response to "Not a number"
    try: 
        #Determine if answer is correct or incorrect and update counter.
        if int(answer) == correct_answer:
            response.set("Correct!")
            total_questions = total_questions + 1
            correct_questions = correct_questions + 1
            num_correct.set(f"{correct_questions}/{total_questions}")
            getRandom()
        else:
            response.set(f"Incorrect! The answer was {correct_answer}. You answered {answer}")
            total_questions = total_questions + 1
            num_correct.set(f"{correct_questions}/{total_questions}")
            getRandom()
    except ValueError:
        response.set("Not a number!")

    
getRandom()
num_correct.set("Score: 0/0")

#Prints the multiplication question
qLabel = Label(root, textvariable=question)
qLabel.pack()

#User input entry
answer_input = Entry(root)
answer_input.pack()

#Submit button that will get the user entry and generate a response if it is correct or not.
submitButton = Button(root, text="Submit", command=lambda: generateResponse(answer_input.get()))
submitButton.pack()

#Space for a response to be given once generated
responseLabel = Label(root, textvariable=response)
responseLabel.pack()

#User score to be shown.
scoreLabel = Label(root, textvariable=num_correct)
scoreLabel.pack()

root.mainloop()


