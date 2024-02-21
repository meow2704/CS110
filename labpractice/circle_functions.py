import math
print("hello")
def calculate_Area(radius):
    area = math.pi * radius**2
    return area

def calculate_Circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def main():
    radius = float(input("Enter the radius of the circle: "))
    
    area = calculate_Area(radius)
    circumference = calculate_Circumference(radius)
    
    print(f"The area of the circle is: {area}")
    print(f"The circumference of the circle is: {circumference}")

main()