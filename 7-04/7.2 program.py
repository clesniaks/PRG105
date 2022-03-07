outfile = open("cypher.txt", "w")
phrase_final = ""


def main():
    global phrase_final
    cypher = ['!', '✪', '_', '*', '+', '}', '{', '^', '#', '💫', ';', '>', ')', '&', '<', '✈', '☊', '?', '(', '=', '$', '№', 's', '♤', '1', '↦', ' ', ',', '.', '/']
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ',', '.', '/']
    phrase = input("Please enter a phrase to encrypt: ")
    for letter in phrase:
        for item in range(0, len(alpha)):
            if letter.lower() == alpha[item]:
                phrase_final += (cypher[item] + "\n")


main()
outfile.write(phrase_final)
outfile.close()
