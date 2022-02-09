import math
from Point import Point

#    ----------------------------------------------------------------
#    |                        RegularHeptagon                       |
#    |--------------------------------------------------------------|
#    | center: Point                                                |
#    | radius: numeric                                              |
#    | apothem: numeric                                             |
#    | side: numeric                                                |
#    | vertices: Point (collection)                                 |
#    | area: numeric                                                |
#    | perimeter: numeric                                           |
#    |--------------------------------------------------------------|
#    | <<constructor> RegularHeptagon(center: Point, vertex: Point) |
#    | translate(dx: numeric, dy: numeric)                          |
#    | resize(radius: numeric)                                      |
#    | rotate(angle: numeric)                                       |
#    ----------------------------------------------------------------


class RegularHeptagon:

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
    def apothem(self):
        return self.__apothem

    @property
    def side(self):
        return self.__side

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter

    def __getitem__(self, item):
        return self.__vertices[item]

    # endregion

    # region CONSTRUCTORS

    # REMEMBER: Constructors are special functions whose name is
    #           always the same of the class. Its responsibility
    #           is to establish an initial VALID state of the object.
    #           In Python there is only 1 constructor, if we need
    #           other variants, we use default values.

    # Builds a heptagon from its center and first vertex, calculating
    # other vertices counterclockwise.
    def __init__(self, center, vertex):
        # Center and vertex cannot be the same point.
        if not (center.x == vertex.x and center.y == vertex.y):
            # Stores the center.
            self.__center = center
            # Calculates radius (distance from center to vertex).
            self.__radius = center.distance_to(vertex)
            # Calculates vertices.
            self.__vertices = []
            self.__vertices.append(vertex)
            angle = math.pi * 2 / 7
            for i in range(1, 7):
                x = math.cos(i * angle) * (vertex.x - center.x) - \
                    math.sin(i * angle) * (vertex.y - center.y) + center.x
                y = math.sin(i * angle) * (vertex.x - center.x) + \
                    math.cos(i * angle) * (vertex.y - center.y) + center.y
                self.__vertices.append(Point(x, y))
            # Calculates apothem (radius multiplied by the cosine of PI/7).
            self.__apothem = self.__radius * math.cos(math.pi / 7)
            # Calculates side (distance between 2 consecutive vertices).
            self.__side = self.__vertices[0].distance_to(self.__vertices[1])
            # Calculates perimeter (side length multiplied by seven).
            self.__perimeter = self.__side * 7
            # Calculates area (half the product of its perimeter and its apothem).
            self.__area = self.__perimeter * self.__apothem / 2
        else:
            raise ValueError("ERR: Center and vertex cannot be the same point.")

    # endregion

    # region METHODS

    # REMEMBER: Methods are functions inside the class that defines
    #           the behaviour of the objects.

    # Moves the heptagon offsetting its center and vertices a given
    # horizontal and vertical distance. All other properties remains
    # the same.
    def translate(self, dx, dy):
        self.__center.translate(dx, dy)
        for vertex in self.__vertices:
            vertex.translate(dx, dy)

    # Resizes the heptagon based on its circumscribed radius. Some
    # of its properties must be recalculated.
    def resize(self, radius):
        # The radius must be positive.
        if radius > 0:
            # Stores the radius.
            self.__radius = radius
            # Calculates the slope of the segment from center
            # to first vertex, and then the new vertex in that
            # direction from center.
            dx = self.__vertices[0].x - self.__center.x
            dy = self.__vertices[0].y - self.__center.y
            if dx != 0:
                slope = dy / dx
                theta = math.atan(slope)
            elif dy > 0:
                theta = math.pi / 2
            else:
                theta = 3 * math.pi / 2
            x = self.__center.x + radius * math.cos(theta)
            y = self.__center.y + radius * math.sin(theta)
            # Calculates the new vertices.
            vertex = Point(x, y)
            self.__vertices[0] = vertex
            angle = math.pi * 2 / 7
            for i in range(1, 7):
                x = math.cos(i * angle) * (vertex.x - self.__center.x) - \
                    math.sin(i * angle) * (vertex.y - self.__center.y) + self.__center.x
                y = math.sin(i * angle) * (vertex.x - self.__center.x) + \
                    math.cos(i * angle) * (vertex.y - self.__center.y) + self.__center.y
                self.__vertices[i] = Point(x, y)
            # Calculates apothem (radius multiplied by the cosine of PI/7).
            self.__apothem = self.__radius * math.cos(math.pi / 7)
            # Calculates side (distance between 2 consecutive vertices).
            self.__side = self.__vertices[0].distance_to(self.__vertices[1])
            # Calculates perimeter (side length multiplied by seven).
            self.__perimeter = self.__side * 7
            # Calculates area (half the product of its perimeter and its apothem).
            self.__area = self.__perimeter * self.__apothem / 2
        else:
            raise ValueError("ERR: Radius cannot be zero or negative.")

    # Rotates the heptagon around its center (the parameters is in degrees).
    def rotate(self, angle):
        theta = math.radians(angle)
        for i in range(7):
            x = math.cos(theta) * (self.__vertices[i].x - self.__center.x) - \
                math.sin(theta) * (self.__vertices[i].y - self.__center.y) + \
                self.__center.x
            y = math.sin(theta) * (self.__vertices[i].x - self.__center.x) + \
                math.cos(theta) * (self.__vertices[i].y - self.__center.y) + \
                self.__center.y
            self.__vertices[i] = Point(x, y)

    # endregion
