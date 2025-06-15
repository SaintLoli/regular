
def check_color(color):
    if color[:3] == "rgb":
        return parse_rgb(color[3:])
    elif color[:3] == "hsl":
        return parse_hsl(color[3:])
    else:
        if color[0] == "#":
            return parse_hex(color[1:])
        else:
            return False


def parse_rgb(color):
    if color[0] == "(" and color[-1] == ")":
        if color.count(",") == 2:
            r, g, b = color[1:-1].split(", ")

            if r[-1] == "%" and g[-1] == "%" and b[-1] == "%":
                try:
                    r, g, b = int(r[:-1]), int(g[:-1]), int(b[:-1])

                    if r <= 100 and g <= 100 and b <= 100:
                        return True
                    else:
                        return False

                except Exception as e:
                    return False

            elif r[-1].isdigit() and g[-1].isdigit() and b[-1].isdigit():
                try:
                    r, g, b = int(r), int(g), int(b)

                    if r <= 255 and g <= 255 and b <= 255:
                        return True
                    else:
                        return False

                except Exception as e:
                    return False

    return False


def parse_hex(color):
    req_colors = "0123456789abcdef"
    if len(color) == 3 or len(color) == 6:
        for i in color:
            if i.lower() not in req_colors:
                return False
        return True

    return False


def parse_hsl(color):
    if color[0] == "(" and color[-1] == ")":
        if color.count(",") == 2:
            h, s, l = color[1:-1].split(", ")

            if s[-1] == "%" and l[-1] == "%":
                try:
                    h, s, l = int(h), int(s[:-1]), int(l[:-1])

                    if 0 <= h <= 360 and s <= 100 and l <= 100:
                        return True
                    else:
                        return False

                except Exception as e:
                    return False

    return False




col = input("Введите цвет для теста --> ")
print(check_color(col))
