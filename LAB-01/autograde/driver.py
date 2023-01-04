import os
import sys
import json
import pytest
import yaml

# os resultados por padrão são "não concluido"
results = [False, False, False, False]


def formatted_feedback(p1, p2, p3, p4):
    formatted_feedback = {
        "_presentation": "semantic",
        "stages": ["Test Results"],
        "Test Results":
            {
                "calc_hipotenusa": {
                    "passed": p1,
                    "hint": "https://www.todamateria.com.br/hipotenusa-como-calcular-sua-medida/#:~:text=O%20c%C3%A1lculo%20da%20hipotenusa%20%C3%A9,soma%20dos%20catetos%20ao%20quadrado%E2%80%9D."
                },
                "calc_area_comprimento_circulo": {
                    "passed": p2,
                    "hint": "https://brasilescola.uol.com.br/matematica/comprimento-area-circunferencia.htm"
                },
                "calc_imc": {
                    "passed": p3,
                    "hint": "https://centrodeobesidadeediabetes.org.br/tudo-sobre-obesidade/calculadora-de-imc/#:~:text=O%20IMC%20%C3%A9%20reconhecido%20como,ao%20quadrado%20(em%20metros)."
                },
                "calc_distancia_2pontos": {
                    "passed": p4,
                    "hint": "https://mundoeducacao.uol.com.br/matematica/distancia-entre-dois-pontos.htm#:~:text=Dados%20os%20pontos%20A(x,B%20%E2%80%93%20yA)%C2%B2."
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
        formatted_feedback(results[0], results[1],results[2], results[3])
        print(json.dumps(student_eval))  # required to autograde
