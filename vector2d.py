class Vector2d:

    def __init__(self, *arguments):
        if len(arguments) == 2:
            try:
                try:
                    self.x = float(arguments[0])
                    self.y = float(arguments[1])
                except ValueError:
                    print "x and y are numbers"
            except TypeError:
                print "type error"
        else:
            print "vector contains two number"

    def printVector(self):

        try:
            x = self.x
            y = self.y

            try:
                x = float(x)
                y = float(y)
                print "v =", [x, y]
            except ValueError:
                print "argument is not a vector"
        except AttributeError:
            print "can not print vector"

    def multiplyVector(self, *arguments):
        if len(arguments) == 1:
            try:
                factor = float(arguments[0])
                mulitipliedVector = Vector2d(self.x * factor, self.y * factor)
                return mulitipliedVector
            except ValueError:
                print "factor should be a number"
                return Vector2d(self.x, self.y)
        else:
            return Vector2d(self.x, self.y)
            print "factor should not be empty"

    def vectorLength(self):
        try:
            length = round((float(self.x) ** 2 + float(self.y) ** 2) ** 0.5, 3)
            return length

        except AttributeError:
            print "vector is 2 numbers"
            return 0
