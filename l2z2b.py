from vector2d import Vector2d


def main():

    print"test"

    print "correct vector:"
    correctVector = Vector2d(-6.9, 42)
    correctVector.printVector()
    print "length:", correctVector.vectorLength()
    print

    print "multiplied vector:"
    multipliedVector1 = correctVector.multiplyVector(5)
    multipliedVector1.printVector()
    print

    print "vector multiplied by wrong factor:"
    multipliedVector2 = correctVector.multiplyVector('f')
    multipliedVector2.printVector()
    print

    print "vector multiplied by nothing:"
    multipliedVector2 = correctVector.multiplyVector()
    multipliedVector2.printVector()
    print

    print "wrong argument vector:"
    wrongArgumentVector = Vector2d(-6.9, 'f')
    wrongArgumentVector.printVector()
    print wrongArgumentVector.vectorLength()
    print

    print "not enough arguments vector:"
    notEnoughArgumentsVector = Vector2d(65)
    notEnoughArgumentsVector.printVector()
    print notEnoughArgumentsVector.vectorLength()
    print

    print "no arguments vector:"
    noArgumentsVector = Vector2d()
    noArgumentsVector.printVector()
    print noArgumentsVector.vectorLength()
    print

    print "to much arguments vector:"
    toMuchArgumentsVector = Vector2d(2,3,4)
    toMuchArgumentsVector.printVector()
    print toMuchArgumentsVector.vectorLength()
    print



if __name__ == '__main__':
    main()
