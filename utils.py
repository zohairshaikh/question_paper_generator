
EASY = 0
MEDIUM = 1
HARD = 2

def print_total_marks(questions):
    marks = 0
    for x in range(0, len(questions)):
        marks += questions[x].marks
    print "TOTAL MARKS: {}\n".format(marks)


def print_question(question):
    difficulty_map = {
        EASY: "EASY",
        MEDIUM: "MEDIUM",
        HARD: "HARD"
    }

    print "DIFFICULTY : {} \t MARKS: {}".format(difficulty_map[question.difficulty], question.marks)


def print_questions(questions):
    if questions:
        map(print_question, questions)