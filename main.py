import random


from Questions import Questions
from PaperFormat import PaperFormat
from utils import *


def paper(questions, format):
    res_easy = find_questions(questions, format.easy, EASY)
    res_medium = find_questions(questions, format.medium, MEDIUM)
    res_hard = find_questions(questions, format.hard, HARD)


    # Printing the results

    print_questions(res_easy)
    print_total_marks(res_easy)
    print_questions(res_medium)
    print_total_marks(res_medium)
    print_questions(res_hard)
    print_total_marks(res_hard)



def find_questions(questions, percentage, difficulty):
    from random import shuffle
    filtered_questions = list(filter(lambda q: q.difficulty == difficulty, questions))
    shuffle(filtered_questions)
    res = next_delta(filtered_questions, percentage, [], [])
    return res


def next_delta(questions, remaining, res, removed):
    for i in range(0, len(questions)):
        if not questions[i]:
            return []
        left = remaining - questions[i].marks
        if left >= 0:
            if left == 0:
                res.append(questions[i])
                return res
            elif left > 0:
                removed.append(questions[i])
                res.append(questions[i])
                del questions[i]
                return next_delta(questions, left, res, removed)
        else:
            del questions[i]
            return next_delta(questions, remaining, res, removed)
    else:
        return []


def generate_questions():
    import json
    questions = []
    with open('MOCK_DATA.json') as f:
        raq_questions = json.load(f)
        for q in raq_questions:
            questions.append(Questions(q['text'], q['subject'], q['topic'], q['difficulty'], q['marks']))
    return questions


def main():
    questions = generate_questions()

    paper_format = PaperFormat(20, 10, 5, 5)

    # Func paper will print all the required meta. Func paper is not a pure func
    paper(questions, paper_format)



if __name__ == '__main__':
    main()
