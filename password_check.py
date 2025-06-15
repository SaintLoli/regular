SPEC_SYMB = "^$%@#&*!?"


def check_pass(password):
    rules_correct = {
        "len" : False,
        "lat_up" : False,
        "lat_low" : False,
        "digit" : False,
        "spec_symb" : [0, ""],
        "no_repeat" : True,
        "correct_symb" : True,
        "spec_rules" : False
    }

    if len(password) >= 8:
        rules_correct["len"] = True

    for i in range(len(password)):
        if i != len(password) - 1:
            if password[i] == password[i + 1]:
                rules_correct["no_repeat"] = False
                break

        if not password[i].isdigit() and not password[i].isalpha() and password[i] not in SPEC_SYMB:
            rules_correct["correct_symb"] = False
            break

        if password[i].isalpha() and password[i] == password[i].upper():
            rules_correct["lat_up"] = True

        if password[i].isalpha() and password[i] == password[i].lower():
            rules_correct["lat_low"] = True

        if password[i].isdigit():
            rules_correct["digit"] = True

        if password[i] in SPEC_SYMB:
            if password[i] not in rules_correct["spec_symb"][1]:
                rules_correct["spec_symb"][0] += 1
                rules_correct["spec_symb"][1] += password[i]

                if rules_correct["spec_symb"][0] == 2:
                    rules_correct["spec_rules"] = True

    return all(rules_correct.values())


passwd = input("Введите пароль для теста --> ")

print(check_pass(passwd))

