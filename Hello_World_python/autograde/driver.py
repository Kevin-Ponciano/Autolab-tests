import os
import sys
import json
import pytest
import yaml

results = [False,False]

def formatted_feedback(p1,p2):
    formatted_feedback = {
        "_presentation": "semantic",
        "stages": ["Test Results"],
        "Test Results": 
        {
            "Problem1": {
                "passed": p1,
                "hint" : "Verifica a escrita"
            },
            "Problem2": {
                "passed": p2,
                "hint": "falta colocar mais empenho"
            }
        }
    }

    print(json.dumps(formatted_feedback))


def score_assignment(problems):
    global results
    i = 0

    student_eval = {
        'scores': {}
    } 

    for p in problems:
        name = p
        score = problems[p]['score']
        test = problems[p]['test']

        test_result = pytest.main([test])
        # Exit code 0:	All tests were collected and passed successfully
        # Exit code 1:	Tests were collected and run but some of the tests failed
        # Exit code 2:	Test execution was interrupted by the user
        # Exit code 3:	Internal error happened while executing tests
        # Exit code 4:	pytest command line usage error
        # Exit code 5:	No tests were collected
        earned = 0
        if test_result == 0:  # success
            earned = score
            results[i] = True

        i = i + 1
        student_eval['scores'][name] = earned
    return student_eval


if __name__ == "__main__":
    current_dir = os.path.dirname(sys.argv[0])
    if current_dir is not '':
        os.chdir(current_dir)

    with open(sys.argv[1], 'r') as stream:
        problems = yaml.load(stream)
        student_eval = score_assignment(problems)
        
        print(results)
        formatted_feedback(results[0],results[1])
        print(json.dumps(student_eval))  # required to autograde
