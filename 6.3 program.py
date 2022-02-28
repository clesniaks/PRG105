num_lines = 0
lines = []
er_value = ""


def main():
    global num_lines
    global lines
    global er_value
    user_info = open("sales_error.txt", 'r')
    for line in user_info:
        lines.append(line)
        er_value = lines[num_lines]
        print(format(float(lines[num_lines]), ",.2f"))
        num_lines += 1
    user_info.close()


try:
    main()
except IOError:
    print("The file does not exist, check the file-name")
except ValueError:
    print("Line " + str(num_lines) + " with a value of " + er_value + " was invalid")
