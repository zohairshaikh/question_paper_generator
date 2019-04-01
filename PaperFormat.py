"""
Taking total_marks, easy, medium, hard -> Validates the paper format if the marks distribution is correct else raises
an exception
"""

class PaperFormat:

    def __init__(self, total_marks, easy, medium, hard):

        if not easy or not medium or not hard:
            raise Exception('Marks for a difficulty cannot be Zero')

        if not (easy + medium + hard) == total_marks:
            raise Exception('Summation of easy, medium and hard should be equal to total_marks')

        self.total_marks = total_marks
        self.easy = easy
        self.medium = medium
        self.hard = hard
