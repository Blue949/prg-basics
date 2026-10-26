###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

def triangle_area(a,b,c):
    x = (a + b + c) / 2
    pole = (x*(x-a)*(x-b)*(x-c)) ** 0.5
    print(pole)
    return pole

print(f'The area of ​​a triangle with sides {a},{b},{c} is {triangle_area(a,b,c)}')

