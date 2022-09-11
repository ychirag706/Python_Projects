# a dictionary that stores questions and answers 
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs 
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1": {
    "question": "what is the capital of france",
    "answer": "Paris"
    },"questionn2": {
    "question": "what is the capital of Germany?",
    "answer": "Berlin"   
    },"questionn3": {
    "question": "what is the capital of Italy?",
    "answer": "Rome"   
    },"questionn4": {
    "question": "what is the capital of Australia?",
    "answer": "Vienna"   
    },"questionn5": {
    "question": "what is the capital of Spain?",
    "answer": "Madrid"   
    },"questionn6": {
    "question": "what is the capital of Portugal?",
    "answer": "Lisbon"   
    },"questionn7": {
    "question": "what is the capital of Switzerland?",
    "answer": "Bern"   
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer?")
    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("your score is: " +str(score))
    else:
        print("wrong")
        print(" The answer is: "+ value['answer'])
        print("your score is: "+ str(score))
