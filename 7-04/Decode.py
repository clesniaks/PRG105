try:
    outfile = open(input("What is the name of the file?:"), "r")
except IOError:
    print("File name not found")

phrase_final = ""


def main():
    global phrase_final
    cypher = ['!', '✪', '_', '*', '+', '}', '{', '^', '#', '💫', ';', '>', ')', '&', '<', '✈', '☊', '_', '(', '=', '$', '№', 's', '♤', '1', '↦', ' ', ',', '.', '/']
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ',', '.', '/']
    phrase = outfile.read()
    for letter in phrase:
        for item in range(0, 29):
            if letter.lower() == cypher[item]:
                phrase_final += (alpha[item])


main()
print(phrase_final)
print("The phrase has been decoded!")
outfile.close()
