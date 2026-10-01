side_1 = float(input("Enter the first side: "))
side_2 = float(input("Enter the second side: "))
side_3 = float(input("Enter the third side: "))

if (
    side_1 + side_2 > side_3
    and side_1 + side_3 > side_2
    and side_2 + side_3 > side_1
):
    if side_1 == side_2 == side_3:
        print("The triangle is equilateral.")
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("These sides cannot form a triangle.")