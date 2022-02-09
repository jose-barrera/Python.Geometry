import math

#    ----------------------------------------------------------
#    |                          Circle                        |
#    |--------------------------------------------------------|
#    | center: Point                                          |
#    | radius: numeric                                        |
#    | diameter: numeric                                      |
#    | area: numeric                                          |
#    | perimeter: numeric                                     |
#    |--------------------------------------------------------|
#    | <<constructor> Circle(center: Point, radius: numeric)  |
#    | translate(dx: numeric, dy: numeric)                    |
#    | translate(center: Point)                               |
#    | resize(radius: numeric)                                |
#    ----------------------------------------------------------


class Circle:

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
    def radius(self):
        return self.__radius

    @property
    def diameter(self):
        return self.__diameter

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

    def __init__(self, center, radius):
        # Radius must be a positive value, if not,
        # object cannot be created and an error
        # will be generated.
        if radius > 0:
            # Stores the data received.
            self.__center = center
            self.__radius = radius
            # Diameter, area, and perimeter
            # are calculated from radius.
            self.__diameter = radius * 2
            self.__area = math.pi * radius * radius
            self.__perimeter = math.pi * 2 * radius
        else:
            raise ValueError("ERR: Radius cannot be zero or negative.")

    # endregion
    
    # region METHODS
    
    # REMEMBER: Methods are functions inside the class that defines
    #           the behaviour of the objects.

    # Moves the circle offsetting its center a given horizontal
    # and vertical distance. Or moves the circle changing its
    # center directly. The action depends on the argument. All
    # other properties remains the same.
    def translate(self, center=None, dx=None, dy=None):
        if center is None and dx is not None and dy is not None:
            self.__center.translate(dx, dy)
        elif center is not None and dx is None and dy is None:
            self.__center = center
        else:
            raise ValueError("ERR: Arguments are incorrect.")

    # Changes the size of circle by setting a new radius.
    def resize(self, radius):
        # Radius must be a positive value, if not,
        # object cannot be created and an error
        # will be generated.
        if radius > 0:
            # Stores the data received.
            self.__radius = radius
            # Diameter, area, and perimeter
            # are calculated from radius.
            self.__diameter = radius * 2
            self.__area = math.pi * radius * radius
            self.__perimeter = math.pi * 2 * radius
        else:
            raise ValueError("ERR: Radius cannot be zero or negative.")

    # endregion
