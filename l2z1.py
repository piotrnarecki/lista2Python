def file_to_words(file_path):
    file = open(file_path, "rt")
    data = file.read()
    words = data.split()
    file.close()
    return words


def check_all_words(words, exemplary_word, threshold):
    import levenshtein
    words_list = []
    for i in range(0, len(words)):
        distance = levenshtein.calculate_distance(words[i], exemplary_word)
        if (distance <= threshold):
            words_list.append(words[i])

    return words_list


def main():
    import sys

    if len(sys.argv) is 4:

        try:
            file_path = sys.argv[1]
            # file_path = "/Users/piotrnarecki/Desktop/text1.txt"
            exemplary_word = sys.argv[2].upper()
            try:
                threshold = int(sys.argv[3])
                if threshold > 0:

                    words = file_to_words(file_path)
                    words_list = check_all_words(words, exemplary_word, threshold)

                    print ('exemplary word: ', exemplary_word)
                    print ('threshold: ', threshold)
                    print (words_list)

                else:
                    print ('treshold should greather than 0')
            except ValueError:
                print ('treshold should be number')

        except IOError:
            print ('this file does not exist')

    elif (len(sys.argv) is 3):

        try:
            file_path = sys.argv[1]
            exemplary_word = sys.argv[2].upper()
            threshold = 1
            words = file_to_words(file_path)

            words_list = check_all_words(words, exemplary_word, threshold)

            print ('exemplary word: ', exemplary_word)
            print ('threshold: ', threshold)
            print (words_list)

        except IOError:
            print ('this file does not exist')




    else:
        print ('not enough arguments')


if __name__ == '__main__':
    main()
