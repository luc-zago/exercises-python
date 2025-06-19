def gradingStudents(grades):
    g_output = list()
    for g in grades:
        if g >= 38:
            if g % 5 == 0:
                g_output.append(g)
            else:
                g_str = str(g)
                if g_str[1] == "3" or g_str[1] == "8":
                    g += 2
                elif g_str[1] == "4" or g_str[1] == "9":
                    g += 1
                g_output.append(g)
        else:
            g_output.append(g)
    return g_output


if __name__ == "__main__":
    print(gradingStudents([84, 29, 57, 90, 78]))
