class Test:
    def __init__(self):
        self.a = 1000  # Initialize 'a' in the constructor

    def m1(self):
        print(self.a)  # Access instance variable 'a'

    def m2(self):
        b = 2000       # Local variable
        print(self.a)  # Access instance variable 'a'
        print(b)       # Print local variable 'b'

# Create an object of the class
t = Test()

# Call the methods
t.m1()
t.m2()
