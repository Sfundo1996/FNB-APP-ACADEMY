#my way 
length1 = int(input("Please enter the length : "))
width1 = int(input("Please enter width : "))

area1 = length1 * width1 

print("area is ", area1)

#their way of calculating length
import calculator
length = float(input("Enter the length of the rectangle"))
width = float(input("Enter the width of the rectangle"))

area = calculator.area(length, width)
parimeter = calculator.parimeter(length, width)

print("The area of the rectangle is :", area)
print("The perimeter of the rectangle is:", parimeter)