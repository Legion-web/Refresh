from Question import Question

Question_prompts = [
    "What colour are Apples?\n(a) Red/Green\n(b)Violet\n(c)Orange\n\n",
    "What colour are Bananas?\n(a) Teal\n(b)Yellow\n(c)Orange\n\n",
    "What colour are Strawberries?\n(a) Blue\n(b)Yellow\n(c)Red\n\n",
]
questions = [
    Question(Question_prompts[0], "a"),
    Question(Question_prompts[1], "b"),
    Question(Question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == questions.answers:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + "correct")


run_test(questions)
