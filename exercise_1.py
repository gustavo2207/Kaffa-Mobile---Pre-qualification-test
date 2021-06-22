

def validate_cnpj(string):

    if string[2] == "." and string[6] == "." and string[10] == "/" and string[15] == "-":
        separate_cnpj_validate = string.replace(".", "") \
            .replace("/", "").split('-')
    else:
        separate_cnpj_validate = [string[0:12], string[12:14]]

    pure_cnpj = separate_cnpj_validate[0]

    validate_code_real = None

    for n in range(len(pure_cnpj)):
        try:
            int(pure_cnpj[n])
        except ValueError:
            return "Invalid input"

    for i in range(len(pure_cnpj)):
        if i == 0:
            validate_code_real = int(pure_cnpj[i]) * 6
        elif i == 1:
            validate_code_real += int(pure_cnpj[i]) * 7
        elif i == 2:
            validate_code_real += int(pure_cnpj[i]) * 8
        elif i == 3:
            validate_code_real += int(pure_cnpj[i]) * 9
        elif i == 4:
            validate_code_real += int(pure_cnpj[i]) * 2
        elif i == 5:
            validate_code_real += int(pure_cnpj[i]) * 3
        elif i == 6:
            validate_code_real += int(pure_cnpj[i]) * 4
        elif i == 7:
            validate_code_real += int(pure_cnpj[i]) * 5
        elif i == 8:
            validate_code_real += int(pure_cnpj[i]) * 6
        elif i == 9:
            validate_code_real += int(pure_cnpj[i]) * 7
        elif i == 10:
            validate_code_real += int(pure_cnpj[i]) * 8
        elif i == 11:
            validate_code_real += int(pure_cnpj[i]) * 9

    if validate_code_real % 11 != 10:
        pure_cnpj += str(validate_code_real % 11)
    else:
        pure_cnpj += '0'

    for i in range(len(pure_cnpj)):
        if i == 0:
            validate_code_real = int(pure_cnpj[i]) * 5
        elif i == 1:
            validate_code_real += int(pure_cnpj[i]) * 6
        elif i == 2:
            validate_code_real += int(pure_cnpj[i]) * 7
        elif i == 3:
            validate_code_real += int(pure_cnpj[i]) * 8
        elif i == 4:
            validate_code_real += int(pure_cnpj[i]) * 9
        elif i == 5:
            validate_code_real += int(pure_cnpj[i]) * 2
        elif i == 6:
            validate_code_real += int(pure_cnpj[i]) * 3
        elif i == 7:
            validate_code_real += int(pure_cnpj[i]) * 4
        elif i == 8:
            validate_code_real += int(pure_cnpj[i]) * 5
        elif i == 9:
            validate_code_real += int(pure_cnpj[i]) * 6
        elif i == 10:
            validate_code_real += int(pure_cnpj[i]) * 7
        elif i == 11:
            validate_code_real += int(pure_cnpj[i]) * 8
        elif i == 12:
            validate_code_real += int(pure_cnpj[i]) * 9

    if validate_code_real % 11 != 10:
        pure_cnpj += str(validate_code_real % 11)
    else:
        pure_cnpj += '0'

    validate_code_real = pure_cnpj[-2] + pure_cnpj[-1]

    if validate_code_real == separate_cnpj_validate[1]:
        return "This is a real CNPJ!"
    else:
        return "This is a fake CNPJ!"


print(validate_cnpj(input()))
