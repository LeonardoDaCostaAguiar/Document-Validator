def calculate_validator_digit(list: list, remove_entries: int, digit_multiplier: int):
    n = remove_entries
    evaluation_number_list = list[: -n]
    total = []
    multiplier = digit_multiplier
    length = len(evaluation_number_list)
    digit = 0

    for i in range(length):
        multiplier = multiplier - 1
        document_index_number = evaluation_number_list[int(i)]
        result = int(document_index_number) * multiplier
        total.append(result)

    digit_division = sum(total) % 11

    if digit_division < 2:
        return digit
    elif digit_division >= 2:
        digit = 11 - digit_division
        return digit


def get_document_state(document):
    state_digit = int(document[8])
    if state_digit == 8:
        return "📍Este CPF foi expedido no Estado de São Paulo"
    elif state_digit == 6:
        return "📍Este CPF foi expedido no Estado de Minas Gerais"
    elif state_digit == 0:
        return "📍Este CPF foi expedido no Estado Rio Grande do Sul"
    else:
        return ""


def is_cpf_valid(cpf: str):
    if len(cpf) == 11:
        doc_list = []
        for number in list(cpf):
            doc_list.append(number)

        first_digit = calculate_validator_digit(list=doc_list, remove_entries=2, digit_multiplier=(len(doc_list)))
        second_digit = calculate_validator_digit(list=doc_list, remove_entries=1, digit_multiplier=(len(doc_list) +1))

        if first_digit == int(doc_list[9]) and second_digit == int(doc_list[10]):
            return True
        else:
            return False

    else:
        print("Valor de CPF inválido. Insira seu CPF sem pontos e traço.")
