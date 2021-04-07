def fileToWords(filePath):
    file = open(filePath, "rt")
    data = file.read()
    words = data.split()
    file.close()
    return words


def checkAllWords(words, exemplaryWord, threshold):
    import levenshtein
    wordsList = []
    for i in range(0, len(words)):
        distance = levenshtein.calculateDistance(words[i], exemplaryWord)
        if (distance <= threshold):
            wordsList.append(words[i])

    return wordsList


def main():
    import sys

    if len(sys.argv) is 4:

        try:
            filePath = sys.argv[1]
            # filePath = "/Users/piotrnarecki/Desktop/text1.txt"
            exemplaryWord = sys.argv[2].upper()
            try:
                threshold = int(sys.argv[3])
                if threshold > 0:

                    words = fileToWords(filePath)
                    wordsList = checkAllWords(words, exemplaryWord, threshold)

                    print 'exemplary word: ', exemplaryWord
                    print 'threshold: ', threshold
                    print wordsList

                else:
                    print ('treshold should greather than 0')
            except ValueError:
                print ('treshold should be number')

        except IOError:
            print ('this file does not exist')

    elif (len(sys.argv) is 3):

        try:
            filePath = sys.argv[1]
            exemplaryWord = sys.argv[2].upper()
            threshold = 1
            words = fileToWords(filePath)

            wordsList = checkAllWords(words, exemplaryWord, threshold)

            print 'exemplary word: ', exemplaryWord
            print 'threshold: ', threshold
            print wordsList

        except IOError:
            print ('this file does not exist')




    else:
        print ('not enough arguments')


if __name__ == '__main__':
    main()
