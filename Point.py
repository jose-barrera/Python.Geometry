import math

#    -------------------------------------------------
#    |                    Point                      |
#    |-----------------------------------------------|
#    | x: numeric                                    |
#    | y: numeric                                    |
#    |-----------------------------------------------|
#    | <<constructor> Point()                        |
#    | <<constructor> Point(x: numeric, y: numeric)  |
#    | translate(dx: numeric, dy: numeric)           |
#    | distanceto(other: Point): numeric             |
#    -------------------------------------------------


class Point:

    # region INTERNAL FIELDS

    # REMEMBER: In Python there is no declaration of 
    #           variables.

    # endregion

    # region PROPERTIES

    # REMEMBER: Properties are a protection mechanism to accomplish
    #           encapsulation. Any property may have 2 components:
    #           a) ACCESSOR, responsible to give access to the
    #              internal field (read).
    #           b) MUTATOR, responsible to allow modification of
    #              the internal field (write).
    #           Properties with both accessor and mutator are READ/WRITE.
    #           Properties with only accessor are READ-ONLY.
    #           Properties with only mutator are WRITE-ONLY.

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # endregion

    # region CONSTRUCTORS

    # REMEMBER: Constructors are special functions whose name is
    #           always the same of the class. Its responsibility
    #           is to establish an initial VALID state of the object.
    #           In Python there is only 1 constructor, if we need
    #           other variants, we use default values.

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # endregion

    # region METHODS

    # REMEMBER: Methods are functions inside the class that defines
    #           the behaviour of the objects.

    # Moves the point offsetting it a given horizontal
    # and vertical distance. If vertical displacement is
    # positive, the point moves up; otherwise if vertical 
    # displacement is negative, the point moves down. If
    # horizontal displacement is positive, the point moves
    # right; otherwise if horizontal displacement is negative,
    # the point moves left.
    def translate(self, dx, dy):
        self.__x += dx
        self.__y += dy

    # Calculates the distance between this point (self)
    # and other point.
    def distance_to(self, other):
        return math.sqrt((other.x - self.__x) ** 2 + (other.y - self.__y) ** 2)

    # endregion
