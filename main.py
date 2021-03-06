from Point import Point
from Circle import Circle
from Ellipse import Ellipse
from RegularHeptagon import RegularHeptagon


def testing_class_point():
    print("***********************")
    print("***   CLASS Point   ***")
    print("***********************")
    print()
    print("1. Create the origin point")
    point_a = Point()
    print(f"   ({point_a.x},{point_a.y})")
    print()
    print("2. Create the point in -3.4 y 4.35")
    point_b = Point(-3.4, 4.35)
    print(f"   ({point_b.x},{point_b.y})")
    print()
    print("3. Calculate distance between them")
    print(f"   {point_a.distance_to(point_b)}")
    print()
    print("4. Move both points 1.4 right and 3.7 down")
    point_a.translate(1.4, -3.7)
    point_b.translate(1.4, -3.7)
    print(f"   ({point_a.x},{point_a.y})")
    print(f"   ({point_b.x},{point_b.y})")
    print()
    print("5. Calculate distance again")
    print(f"   {point_a.distance_to(point_b)}")
    print()
    print()


def testing_class_circle():
    print("************************")
    print("***   CLASS Circle   ***")
    print("************************")
    print()
    print("1. Create circle in (-3,-7.4) with 3.77 radius")
    center = Point(-3, -7.4)
    circle = Circle(center, 3.77)
    print()
    print("2. Print its information")
    print(f"   Center: ({circle.center.x},{circle.center.y})")
    print(f"   Radius: {circle.radius}")
    print(f"   Diameter: {circle.diameter}")
    print(f"   Area: {circle.area}")
    print(f"   Perimeter: {circle.perimeter}")
    print()
    print("3. Move its center to (3,3) and after move its center 1.4 right and 3.7 down")
    circle.translate(center=Point(3, 3))
    circle.translate(dx=1.4, dy=-3.7)
    print()
    print("4. Print its information")
    print(f"   Center: ({circle.center.x},{circle.center.y})")
    print(f"   Radius: {circle.radius}")
    print(f"   Diameter: {circle.diameter}")
    print(f"   Area: {circle.area}")
    print(f"   Perimeter: {circle.perimeter}")
    print()
    print("5. Resize its radius to 10")
    circle.resize(10)
    print()
    print("6. Print its information")
    print(f"   Center: ({circle.center.x},{circle.center.y})")
    print(f"   Radius: {circle.radius}")
    print(f"   Diameter: {circle.diameter}")
    print(f"   Area: {circle.area}")
    print(f"   Perimeter: {circle.perimeter}")
    print()
    print()


def testing_class_ellipse():
    print("*************************")
    print("***   CLASS Ellipse   ***")
    print("*************************")
    print()
    print("1. Create an horizontal ellipse with center in (7.5, -2.3),")
    print("   semi-major axis 3.5, and semi-minor axis 2")
    center = Point(7.5, -2.3)
    ellipse = Ellipse(center, 3.5, 2, "Horizontal")
    print()
    print("2. Print its information")
    print(f"   Center: ({ellipse.center.x},{ellipse.center.y})")
    print(f"   Semi-major axis: {ellipse.semimajor_axis}")
    print(f"   Semi-minor axis: {ellipse.semiminor_axis}")
    print(f"   Orientation: {ellipse.orientation}")
    print(f"   Eccentricity: {ellipse.eccentricity}")
    print(f"   Area: {ellipse.area}")
    print(f"   Perimeter: {ellipse.perimeter}")
    print(f"   Focus 1: ({ellipse.focus1.x},{ellipse.focus1.y})")
    print(f"   Focus 2: ({ellipse.focus2.x},{ellipse.focus2.y})")
    print(f"   Vertex 1: ({ellipse.vertex1.x},{ellipse.vertex1.y})")
    print(f"   Vertex 2: ({ellipse.vertex2.x},{ellipse.vertex2.y})")
    print(f"   Covertex 1: ({ellipse.covertex1.x},{ellipse.covertex1.y})")
    print(f"   Covertex 2: ({ellipse.covertex2.x},{ellipse.covertex2.y})")
    print()
    print("3. Move the ellipse 1.4 right and 3.7 down")
    ellipse.translate(1.4, -3.7)
    print()
    print("4. Print its information")
    print(f"   Center: ({ellipse.center.x},{ellipse.center.y})")
    print(f"   Semi-major axis: {ellipse.semimajor_axis}")
    print(f"   Semi-minor axis: {ellipse.semiminor_axis}")
    print(f"   Orientation: {ellipse.orientation}")
    print(f"   Eccentricity: {ellipse.eccentricity}")
    print(f"   Area: {ellipse.area}")
    print(f"   Perimeter: {ellipse.perimeter}")
    print(f"   Focus 1: ({ellipse.focus1.x},{ellipse.focus1.y})")
    print(f"   Focus 2: ({ellipse.focus2.x},{ellipse.focus2.y})")
    print(f"   Vertex 1: ({ellipse.vertex1.x},{ellipse.vertex1.y})")
    print(f"   Vertex 2: ({ellipse.vertex2.x},{ellipse.vertex2.y})")
    print(f"   Covertex 1: ({ellipse.covertex1.x},{ellipse.covertex1.y})")
    print(f"   Covertex 2: ({ellipse.covertex2.x},{ellipse.covertex2.y})")
    print()
    print("5. Resize the ellipse by 1.7 factor")
    ellipse.resize(1.7)
    print()
    print("6. Print its information")
    print(f"   Center: ({ellipse.center.x},{ellipse.center.y})")
    print(f"   Semi-major axis: {ellipse.semimajor_axis}")
    print(f"   Semi-minor axis: {ellipse.semiminor_axis}")
    print(f"   Orientation: {ellipse.orientation}")
    print(f"   Eccentricity: {ellipse.eccentricity}")
    print(f"   Area: {ellipse.area}")
    print(f"   Perimeter: {ellipse.perimeter}")
    print(f"   Focus 1: ({ellipse.focus1.x},{ellipse.focus1.y})")
    print(f"   Focus 2: ({ellipse.focus2.x},{ellipse.focus2.y})")
    print(f"   Vertex 1: ({ellipse.vertex1.x},{ellipse.vertex1.y})")
    print(f"   Vertex 2: ({ellipse.vertex2.x},{ellipse.vertex2.y})")
    print(f"   Covertex 1: ({ellipse.covertex1.x},{ellipse.covertex1.y})")
    print(f"   Covertex 2: ({ellipse.covertex2.x},{ellipse.covertex2.y})")
    print()
    print()


def testing_class_regular_heptagon():
    print("*********************************")
    print("***   CLASS RegularHeptagon   ***")
    print("*********************************")
    print()
    print("1. Create an heptagon with center in (1,1) and first vertex in (1,6)")
    center = Point(1, 1)
    vertex = Point(1, 6)
    heptagon = RegularHeptagon(center, vertex)
    print()
    print("2. Print its information")
    print(f"   Center: ({heptagon.center.x},{heptagon.center.y})")
    print(f"   Radius: {heptagon.radius}")
    print(f"   Apothem: {heptagon.apothem}")
    print(f"   Side: {heptagon.side}")
    print(f"   Perimeter: {heptagon.perimeter}")
    print(f"   Area: {heptagon.area}")
    print("   Vertices:")
    for i in range(7):
        print(f"      Vertex {i + 1}: ({heptagon[i].x},{heptagon[i].y})")
    print()
    print("3. Move the heptagon 1.4 right and 3.7 down")
    heptagon.translate(1.4, -3.7)
    print()
    print("4. Print its information")
    print(f"   Center: ({heptagon.center.x},{heptagon.center.y})")
    print(f"   Radius: {heptagon.radius}")
    print(f"   Apothem: {heptagon.apothem}")
    print(f"   Side: {heptagon.side}")
    print(f"   Perimeter: {heptagon.perimeter}")
    print(f"   Area: {heptagon.area}")
    print("   Vertices:")
    for i in range(7):
        print(f"      Vertex {i + 1}: ({heptagon[i].x},{heptagon[i].y})")
    print()
    print("5. Resize the heptagon to have 7.7 radius")
    heptagon.resize(7.7)
    print()
    print("6. Print its information")
    print(f"   Center: ({heptagon.center.x},{heptagon.center.y})")
    print(f"   Radius: {heptagon.radius}")
    print(f"   Apothem: {heptagon.apothem}")
    print(f"   Side: {heptagon.side}")
    print(f"   Perimeter: {heptagon.perimeter}")
    print(f"   Area: {heptagon.area}")
    print("   Vertices:")
    for i in range(7):
        print(f"      Vertex {i + 1}: ({heptagon[i].x},{heptagon[i].y})")
    print()
    print("7. Rotate the heptagon 37 degrees counterclockwise")
    heptagon.rotate(37)
    print()
    print("8. Print its information")
    print(f"   Center: ({heptagon.center.x},{heptagon.center.y})")
    print(f"   Radius: {heptagon.radius}")
    print(f"   Apothem: {heptagon.apothem}")
    print(f"   Side: {heptagon.side}")
    print(f"   Perimeter: {heptagon.perimeter}")
    print(f"   Area: {heptagon.area}")
    print("   Vertices:")
    for i in range(7):
        print(f"      Vertex {i + 1}: ({heptagon[i].x},{heptagon[i].y})")
    print()
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testing_class_point()
    testing_class_circle()
    testing_class_ellipse()
    testing_class_regular_heptagon()

    print('ALL DONE!')
