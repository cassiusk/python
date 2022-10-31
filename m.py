QUESTIONS = [{"Question": "What's the name of the river that runs through Egypt?",
              "Answers": ["the nile", "the mississippi river", "the yangtze river", "the amazon river"],
              "CorrectAnswer": "the nile"},
             {"Question": " in the raid on trumps house what was stolnd?",
              "Answers": ["money", "documints", "pasport", "phone"],
              "CorrectAnswer": "pasport"},
	     {"Question": " whill drew bo the trade?",
              "Answers": ["yes", "yes", "yes", "yes"],
              "CorrectAnswer": "yes"}]
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
