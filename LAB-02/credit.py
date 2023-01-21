import re


def credit_card_validator(number_card):
    number_card = str(number_card)

    # Regex para remover qualquer caractere que não for numero
    number_card = re.sub('[^0-9]', '', number_card)
    #if len(number_card) < 13 or len(number_card) > 16:
    #    return "INVALID"

    list_number = []
    list_number_underlined = []
    list_number_no_underlined = []
    len_list = len(number_card)
    sum_digits = 0

    for i in range(len_list):
        list_number.append(number_card[i])

    # PASSO 1. Começando pelo penúltimo dígito e indo em direção ao primeiro,
    # multiplique cada dígito sim, dígito não, por 2
    for j in range(1, len_list, 2):
        list_number_underlined.append(str(int(number_card[~j]) * 2))

    # Tranformo a lista "list_number_underlined" para uma unica string
    list_number_underlined = ''.join(list_number_underlined)

    # Soma dos dígitos dos resultados da multiplicação do PASSO 1
    for k in list_number_underlined:
        sum_digits += int(k)

    # PASSO 2. Adicione a soma dos dígitos dos resultados obtidos no PASSO 1, à soma dos dígitos que
    # não foram multiplicados por 2.
    for m in range(0, len_list, 2):
        list_number_no_underlined.append(int(number_card[~m]))
    for n in list_number_no_underlined:
        sum_digits += int(n)

    # 3. Se o último dígito do total for 0, então o número representa um cartão de crédito válido
    ld = str(sum_digits)[1]  # last_digit

    fd = list_number[0]  # fist_digit
    f2d = list_number[0] + list_number[1]  # fist_two_digits

    if ld != '0':
        return "INVALID"
    elif fd == '4':
        return "VISA"
    elif f2d == '51' or f2d == '52' or f2d == '53' or f2d == '54' or f2d == '55':
        return "MASTERCARD"
    elif f2d == '34' or f2d == '37':
        return "AMEX"


