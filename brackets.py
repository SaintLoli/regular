def check_brackets(exp):
    br = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }

    queue = []

    for i in exp:
        if i in br.keys():
            queue.append(i)
        else:
            if br[queue[-1]] == i:
                del queue[-1]

    if len(queue) == 0:
        return True

    return False


print(check_brackets(input("Введите последовательность --> ")))