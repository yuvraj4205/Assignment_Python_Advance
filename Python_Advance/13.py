''' Write a Python class named Rectangle constructed by a length and 
width and a method which will compute the area of a rectangle'''

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.area=self.length*self.width

rect=Rectangle(5,3)
print("Length:",rect.length)
print("Width:",rect.width)
print("Area:",rect.area)