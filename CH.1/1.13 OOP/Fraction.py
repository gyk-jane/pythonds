# https://runestone.academy/runestone/books/published/pythonds3/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html

class Fraction:
    """Provides the framework to define the methods."""
    def __init__(self, top, bottom):
        """Constructor definition

        In Python, the constructor method is always called __init__. self is a special param that will always be used as a reference back to the object itself and must always be the first formal paramater. 

        Creating an instance of the Fraction object, you invoke the constructor:
            >>> my_fraction = Fraction(3,5)
        """
        self.num = top
        self.den = bottom

    def show(self):
        """Prints the fraction
        
        This is needed because consider what happens when we try to print a Fraction object like so:
            >>> print(my_fraction)
            <__main__.Fraction object at ######
        The fraction object does not know how to respond to this request.
        
        Calling the show() method should do the trick
            >>> my_fraction = Fraction(3, 5)
            >>> my_fraction.show()
        """
        print(f"{self.num}/{self.den}")

    def __str__(self):
        """Prints the fraction
        
        In Python, all classes have a set of standard methods that are provided, but may not work properly. __str__ is one of them. Obviously, __str__ won't work as we've seen above since the __str__ method returns the instance address string. Below is a better implementation which overrides the default __str__ behavior.
        """
        return f"{self.num}/{self.den}"

    def __add__(self, otherFraction):
        """Overrides the add function
        
        Param
            - otherFraction: Represents the other Fraction object to be added together with self
        """
        newNum = (self.num * otherFraction.den) + (self.den * otherFraction.num)
        newDen = self.den * otherFraction.den
        return Fraction(newNum, newDen)

    def __eq__(self, otherFraction):
        """Create deep equality-equality by putting the two fractions in common terms and comparing the numerators.
        
        Deep equality is equality by the same value, while shallow equality is equality by the same reference. Suppose we have instances of the Fraction class, f1 and f2. If f1 and f2 have shallow equality, both objects are pointing towards one Fraction instance. If f2 and f2 have deep equality, both objects are individually pointing towards their own Fraction objects (both which are duplicates of each other). So with a deep equality, you have two duplicate instances of the Fraction class, while in a shallow equality, you have one instance of the Fraction class.

        Param 
            - otherFraction: Represents the other Fraction object to be compared with self
        Returns
            - True or false
        """
        firstNum = self.num * otherFraction.den
        secondNum = otherFraction.num * self.den
        
        return firstNum == secondNum

    def __mul__(self, otherFraction):
        """Multiplies two fractions"""

        newNum = self.num * otherFraction.num
        newDen = self.den * otherFraction.den

        return Fraction(newNum, newDen)

    def __truediv__(self, otherFraction):
        """Divides two fractions"""
        
        newNum = self.num * otherFraction.den
        newDen = self.den * otherFraction.num

        return Fraction(newNum, newDen)

    def __sub__(self, otherFraction):
        """Subtracts two fractions"""

        newNum = (self.num * otherFraction.den) - (self.den * otherFraction.num)
        newDen = self.den * otherFraction.den

        return Fraction(newNum, newDen)

    def __lt__(self, otherFraction):
        """Less-than operator"""

        newNum = (self.num * otherFraction.den) - (self.den * otherFraction.num)
        
        return newNum < 0

    def __gt__(self, otherFraction):
        """Greater-than operator"""

        newNum = (self.num * otherFraction.den) - (self.den * otherFraction.num)

        return newNum > 0

f1 = Fraction(1,4)
f2 = Fraction(1,2)
print(f1+f2)
print(f1*f2)
print(f1/f2)
print(f1-f2)
print(f1 > f2)
print(f1 < f2)