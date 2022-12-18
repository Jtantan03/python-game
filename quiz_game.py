
# # quiz game 
# # we need 

from time import time, sleep

questions = ["What is the largest animal alive?",
 "Who is the richest person in the world in year 2021?",
  "When was the first Starbucks built?",
   "Where is the largest cave in the world?"]

options =[("A. Antarctic blue whale ", "B. Supersaurus ", "C. Megalodon", "D. Chihuahua"),
 ("A. Jeff Bezos", "B. Elon Musk ", "C. Bernard Arnault", "D. Gautam Adani"),
 ("A. 1969", "B. 1900", "C. 1971 ", "D. 69 B.C."),
 ("A. Laos", "B. China", "C. Metro Manila", "D. Central Vietnam ")]

answers = ( "A", "B", "C", "D")
guesses = []
score = 0
question_num = 0
# Countdown = 5
start = time()

def countdown(t):
    guess_timer = "" 
  
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        guess_timer = input()
        print(timer, end="\r")
        sleep(1)
        t -= 1
    return guess_timer


for question in questions:
    print("------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    # countdown(Countdown)   
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)


    if guess == answers[question_num]:
        score += 1
        print ("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    end=time()

    # input("Click anywhere to continue!")
    question_num += 1

print("------------------------------")
print("          RESULT              ")
print("------------------------------")

print("answer: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = score / len(questions) * 100
print(f"your score is: {score}%")

