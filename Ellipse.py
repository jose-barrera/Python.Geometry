import math
from Point import Point


#    ----------------------------------------------------------------
#    |                        Ellipse                               |
#    |--------------------------------------------------------------|
#    | center: Point                                                |
#    | semi-major axis: numeric                                     |
#    | semi-minor axis: numeric                                     |
#    | orientation: text                                            |
#    | eccentricity: numeric                                        |
#    | focus1: Point                                                |
#    | focus2: Point                                                |
#    | vertex1: Point                                               |
#    | vertex2: Point                                               |
#    | covertex1: Point                                             |
#    | covertex2: Point                                             |
#    | area: numeric                                                |
#    | perimeter: numeric                                           |
#    |--------------------------------------------------------------|
#    | <<constructor> Ellipse(center: Point,                        |
#    |                        semi-major axis: numeric,             |
#    |                        semi-minor axis: numeric,             |
#    |                        orientation: text)                    |
#    | translate(dx: numeric, dy: numeric)                          |
#    | resize(factor: numeric)                                      |
#    ----------------------------------------------------------------


class Ellipse:

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
    def center(self):
        return self.__center

    @property
    def semimajor_axis(self):
        return self.__semimajor_axis

    @property
    def semiminor_axis(self):
        return self.__semiminor_axis

    @property
    def orientation(self):
        return self.__orientation

    @property
    def eccentricity(self):
        return self.__eccentricity

    @property
    def focus1(self):
        return self.__focus1

    @property
    def focus2(self):
        return self.__focus2

    @property
    def vertex1(self):
        return self.__vertex1

    @property
    def vertex2(self):
        return self.__vertex2

    @property
    def covertex1(self):
        return self.__covertex1

    @property
    def covertex2(self):
        return self.__covertex2

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter

    # endregion

    # region CONSTRUCTORS

    # REMEMBER: Constructors are special functions whose name is
    #           always the same of the class. Its responsibility
    #           is to establish an initial VALID state of the object.
    #           In Python there is only 1 constructor, if we need
    #           other variants, we use default values.

    def __init__(self, center, semimajor_axis, semiminor_axis, orientation):
        # Axes must be positive values, major axis must be greater
        # than minor axis, and valid orientations are "Horizontal"
        # and "Vertical". If any of these conditions is not met, 
        # object cannot be created and an error will be generated.
        if semimajor_axis > 0 and semiminor_axis > 0:
            if semimajor_axis > semiminor_axis:
                # Stores the data.
                self.__center = center
                self.__semimajor_axis = semimajor_axis
                self.__semiminor_axis = semiminor_axis
                self.__orientation = orientation
                # Makes general calculations.
                linear_eccentricity = math.sqrt(semimajor_axis ** 2 -
                                                semiminor_axis ** 2)
                self.__eccentricity = linear_eccentricity / semimajor_axis
                self.__area = math.pi * semimajor_axis * semiminor_axis
                # Calculates the approximation of perimeter
                h = (self.__semimajor_axis - self.__semiminor_axis) ** 2 / \
                    (self.__semimajor_axis + self.__semiminor_axis) ** 2
                series_approximation = 1 + h / 4 + (h ** 2) / 64 + (h ** 3) / 256 + \
                                       25 * (h ** 4) / 16384 + 49 * (h ** 5) / 655536 + \
                                       441 * (h ** 6) / 1048576
                self.__perimeter = math.pi * (self.__semimajor_axis + self.__semiminor_axis) * series_approximation
                # Calculates points according to orientation.
                if orientation == 'Horizontal':
                    self.__focus1 = Point(center.x - linear_eccentricity, center.y)
                    self.__focus2 = Point(center.x + linear_eccentricity, center.y)
                    self.__vertex1 = Point(center.x - semimajor_axis, center.y)
                    self.__vertex2 = Point(center.x + semimajor_axis, center.y)
                    self.__covertex1 = Point(center.x, center.y - semiminor_axis)
                    self.__covertex2 = Point(center.x, center.y + semiminor_axis)
                elif orientation == 'Vertical':
                    self.__focus1 = Point(center.x, center.y - linear_eccentricity)
                    self.__focus2 = Point(center.x, center.y + linear_eccentricity)
                    self.__vertex1 = Point(center.x, center.y - semimajor_axis)
                    self.__vertex2 = Point(center.x, center.y + semimajor_axis)
                    self.__covertex1 = Point(center.x - semiminor_axis, center.y)
                    self.__covertex2 = Point(center.x + semiminor_axis, center.y)
                else:
                    raise (ValueError("ERR: Orientation is invalid."))
            else:
                raise (ValueError("ERR: Semi-major axis cannot be equal or smaller than semi-minor axis."))
        else:
            raise (ValueError("ERR: Semi-axes cannot be zero or negative."))

    # endregion

    # region METHODS

    # REMEMBER: Methods are functions inside the class that defines
    #           the behaviour of the objects.

    # Moves the ellipse offsetting its center a given horizontal
    # and vertical distance. It is necessary to recalculate some of
    # its properties.
    def translate(self, dx, dy):
        # Updates the data.
        self.__center.translate(dx, dy)
        linear_eccentricity = math.sqrt(self.__semimajor_axis ** 2 -
                                        self.__semiminor_axis ** 2)
        if self.__orientation == 'Horizontal':
            self.__focus1 = Point(self.__center.x - linear_eccentricity, self.__center.y)
            self.__focus2 = Point(self.__center.x + linear_eccentricity, self.__center.y)
            self.__vertex1 = Point(self.__center.x - self.__semimajor_axis, self.__center.y)
            self.__vertex2 = Point(self.__center.x + self.__semimajor_axis, self.__center.y)
            self.__covertex1 = Point(self.__center.x, self.__center.y - self.__semiminor_axis)
            self.__covertex2 = Point(self.__center.x, self.__center.y + self.__semiminor_axis)
        elif self.__orientation == 'Vertical':
            self.__focus1 = Point(self.__center.x, self.__center.y - linear_eccentricity)
            self.__focus2 = Point(self.__center.x, self.__center.y + linear_eccentricity)
            self.__vertex1 = Point(self.__center.x, self.__center.y - self.__semimajor_axis)
            self.__vertex2 = Point(self.__center.x, self.__center.y + self.__semimajor_axis)
            self.__covertex1 = Point(self.__center.x - self.__semiminor_axis, self.__center.y)
            self.__covertex2 = Point(self.__center.x + self.__semiminor_axis, self.__center.y)

    # Resizes the ellipse multiplying their axes by a factor. 
    # If factor > 1 the ellipse grows, if factor < 1 the ellipse
    # shrinks. It is necessary to recalculate some of its properties.
    def resize(self, factor):
        # Factor must be positive otherwise, the ellipse cannot be
        # resized and an error will be generated.
        if factor > 0:
            # Updates the data.
            self.__semimajor_axis *= factor
            self.__semiminor_axis *= factor
            linear_eccentricity = math.sqrt(self.__semimajor_axis ** 2 -
                                            self.__semiminor_axis ** 2)
            self.__eccentricity = linear_eccentricity / self.__semimajor_axis
            self.__area = math.pi * self.__semimajor_axis * self.__semiminor_axis
            # Calculates the approximation of perimeter
            h = (self.__semimajor_axis - self.__semiminor_axis) ** 2 / \
                (self.__semimajor_axis + self.__semiminor_axis) ** 2
            series_approximation = 1 + h / 4 + (h ** 2) / 64 + (h ** 3) / 256 + \
                                   25 * (h ** 4) / 16384 + 49 * (h ** 5) / 655536 + \
                                   441 * (h ** 6) / 1048576
            self.__perimeter = math.pi * (self.__semimajor_axis + self.__semiminor_axis) * series_approximation
            # Calculates points according to orientation.
            if self.__orientation == 'Horizontal':
                self.__focus1 = Point(self.__center.x - linear_eccentricity, self.__center.y)
                self.__focus2 = Point(self.__center.x + linear_eccentricity, self.__center.y)
                self.__vertex1 = Point(self.__center.x - self.__semimajor_axis, self.__center.y)
                self.__vertex2 = Point(self.__center.x + self.__semimajor_axis, self.__center.y)
                self.__covertex1 = Point(self.__center.x, self.__center.y - self.__semiminor_axis)
                self.__covertex2 = Point(self.__center.x, self.__center.y + self.__semiminor_axis)
            elif self.__orientation == 'Vertical':
                self.__focus1 = Point(self.__center.x, self.__center.y - linear_eccentricity)
                self.__focus2 = Point(self.__center.x, self.__center.y + linear_eccentricity)
                self.__vertex1 = Point(self.__center.x, self.__center.y - self.__semimajor_axis)
                self.__vertex2 = Point(self.__center.x, self.__center.y + self.__semimajor_axis)
                self.__covertex1 = Point(self.__center.x - self.__semiminor_axis, self.__center.y)
                self.__covertex2 = Point(self.__center.x + self.__semiminor_axis, self.__center.y)
        else:
            raise (ValueError("ERR: Factor cannot be zero or negative."))

    # endregion
