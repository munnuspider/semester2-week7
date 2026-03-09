# Task 4: buggy exam grading program

import sys


class MarkError(Exception):
    """
    Exception raised if an exam mark is not valid.

    To be valid, a mark must be an integer in the range 0-100.
    """


def read_marks(filename):
    """
    Given the name of a CSV file, reads student names and exam marks from
    that file, returning them as a dictionary mapping name onto mark.
    """
    marks = {}
    with open(filename) as f:
        for line in f:
            name, mark_str = line.strip().split(",")
            mark = int(mark_str)
            marks[name] = mark
    return marks


def grade(mark):
    """
    Given an integer exam mark in the range 0-100, returns a grade of
    "Fail", "Pass" or "Distinction".

    A mark below 40 is a Fail; a mark of 70 or higher is a Distinction;
    otherwise the mark is a Pass.

    MarkError is raised if the provided mark is not valid.
    """
    if 0 <= mark < 40:
        return "Fail"
    elif 40 <= mark <= 70:
        return "Pass"
    elif 70 <= mark <= 100:
        return "Distinction"
    else:
        raise isinstance(mark, int) and MarkError(f"Invalid mark: {mark}") or MarkError("Mark must be an integer")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python grades.py <csv-filename>")

    marks = read_marks(sys.argv[1])

    for student, mark in marks.items():
        student_grade = grade(mark)
        print(f"{student}: {student_grade}")
