def main():
    word_to_num = {}
    input_text = get_text()
    def_word_in_text(input_text, word_to_num)


def get_text():
    input_text = input("Text: ")
    return input_text


def def_word_in_text(input_text, word_to_num):
    words = input_text.split()
    for word in words:
        number = word_to_num.get(word, 0)
        word_to_num[word] = number + 1
    words = list(word_to_num.keys())
    words.sort()
    for word in words:
        print("{} : {}".format(word, word_to_num[word]))


main()
