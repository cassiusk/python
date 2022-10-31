QUESTIONS = [{"Question": "What's the name of the river that runs through Egypt?",
              "Answers": ["The Nile", "The Mississippi River", "The Yangtze River", "The Amazon River"],
              "CorrectAnswer": "The Nile"},
             {"Question": "Who was the Prime Minister before Theresa May?",
              "Answers": ["David Cameron", "John Mayor", "Tony Blair", "Harold Wilson"],
              "CorrectAnswer": "David Cameron"}]

score = 0
for question in QUESTIONS:
    while True:
        answer = input(question['Question'] + '\n>> ' + '\n>> '.join(question['Answers']) + '\n')
        if answer in question['Answers']:
            if answer == question['CorrectAnswer']:
                score += 1
            break
        else:
            print('That is not a valid answer, make sure to input one of\nthe answers and if you did, make sure its written how it is displayed in the question...')

iq = score * 20 + 60
if score == 0:
    print(f'You answered none of the questions correctly so you have an IQ of {iq}')
elif 0 < score < len(QUESTIONS):
    print(f'You answered {score} out of {len(QUESTIONS)} questions correctly so you have an IQ of {iq}')
elif score == len(QUESTIONS):
    print(f'You answered all of the questions correctly so you have an IQ of {iq}')QUESTIONS = [{"Question": "What's the name of the river that runs through Egypt?",
              "Answers": ["The Nile", "The Mississippi River", "The Yangtze River", "The Amazon River"],
              "CorrectAnswer": "The Nile"},
             {"Question": "Who was the Prime Minister before Theresa May?",
              "Answers": ["David Cameron", "John Mayor", "Tony Blair", "Harold Wilson"],
              "CorrectAnswer": "David Cameron"}]

score = 0
for question in QUESTIONS:
    while True:
        answer = input(question['Question'] + '\n>> ' + '\n>> '.join(question['Answers']) + '\n')
        if answer in question['Answers']:
            if answer == question['CorrectAnswer']:
                score += 1
            break
        else:
            print('That is not a valid answer, make sure to input one of\nthe answers and if you did, make sure its written how it is displayed in the question...')

iq = score * 20 + 60
if score == 0:
    print(f'You answered none of the questions correctly so you have an IQ of {iq}')
elif 0 < score < len(QUESTIONS):
    print(f'You answered {score} out of {len(QUESTIONS)} questions correctly so you have an IQ of {iq}')
elif score == len(QUESTIONS):
    print(f'You answered all of the questions correctly so you have an IQ of {iq}')
