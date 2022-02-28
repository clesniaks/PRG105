lines = []
num_lines = 0
run_total = 0


def main():
    global num_lines
    global run_total
    global lines
    user_info = open("sales_totals-1.txt", 'r')
    for line in user_info:
        lines.append(line.strip())
        run_total = run_total + float(lines[num_lines])
        num_lines += 1
    displayfileinfo()
    user_info.close()

def displayfileinfo():
    global num_lines
    global lines
    counter = 0
    while counter < num_lines:
        print(format(float(lines[counter]), ",.2f"))
        counter += 1
    print("Total:" + format(run_total, "22,.2f"))
    print("Number of Entry's:" + format(num_lines, '8.0f'))
    print("Average:" + format((run_total / num_lines), '20,.2f'))


main()
