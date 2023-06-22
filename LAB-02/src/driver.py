import json
import sys
from credit import credit_card_validator

card_numbers = {
    'AMEX': ['3754 35757275339', 376950668275326, '-3774 438954 92392', '3436.506822.48982', '3411-666590-54883'],
    'MASTERCARD': ['550184647887 1352', 5446232595608191, '-5268 7242 4132 0408', '5518.2974.1766.4055', '5249- '
                                                                                                         '3814- '
                                                                                                         '8309- '
                                                                                                         '7485'],
    'VISA': ['4532 5831 63626165', 4916335750754306, '-4532 8166 9683 2896', '4024.0071.8874.9336', '4716-5975-'
                                                                                                    '5735-1907'],
    'INVALID': [-24323, 2132984902840184928, 000000000000000000, '-312038912038210', '329392']
}


def valid_cards_types(type_card):
    print(f'\nTEST {type_card} NUMBERS...')
    score = 25
    for i in range(0, len(card_numbers[type_card])):
        try:
            card = credit_card_validator(card_numbers[type_card][i])
            if card != type_card:
                print('Test %s/%s failed!' % (i + 1, len(card_numbers[type_card])))
                print(f'Number tested: {card_numbers[type_card][i]}')
                score = 0
                return score, f'Number tested: {card_numbers[type_card][i]}'
            else:
                print('Test %s/%s passed!' % (i + 1, len(card_numbers[type_card])))
        except:
            print('Exeption found...')
            print('Test %s/%s failed!' % (i + 1, len(card_numbers[type_card])))
            print(f'Number tested: {card_numbers[type_card][i]}')
            score = 0
            return score, f'Number tested: {card_numbers[type_card][i]}'

    return score, 'ok'


def is_passed(score):
    if score == 25:
        return True
    else:
        return False


def formatted_feedback(score1, score2, score3, score4):
    json_output = {
        "_presentation": "semantic",
        #"Output": "only instructor",
        "stages": ["Test Cards", "Test Invalid Inputs"],
        "Test Cards": {
            "AMEX": {
                "passed": is_passed(score1[0]),
                "hint": score1[1]
            },
            "MASTERCARD": {
                "passed": is_passed(score2[0]),
                "hint": score2[1]
            },
            "VISA": {
                "passed": is_passed(score3[0]),
                "hint": score3[1]
            }
        },
        "Test Invalid Inputs": {
            "Invalid Inputs": {
                "passed": is_passed(score4[0]),
                "hint": score4[1]
            }
        }
    }
    print(json.dumps(json_output))


score_1 = valid_cards_types('AMEX')
score_2 = valid_cards_types('MASTERCARD')
score_3 = valid_cards_types('VISA')
score_4 = valid_cards_types('INVALID')

formatted_feedback(score_1, score_2, score_3, score_4)
print("{\"scores\": {\"TOTAL\": %s}}" % (score_1[0] + score_2[0] + score_3[0] + score_4[0]))
