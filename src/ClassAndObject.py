class MyComplexNumber:

    def __init__(self, real=0, imag=0):
        print ("MyComplexNumber constructor executing...")
        self.real_part = real
        self.imag_real = imag

    def displayComplex(self):
        print ("{0}+{1}j".format(self.real_part, self.imag_real))


# Step 1
complex1 = MyComplexNumber(40, 50)
complex1.displayComplex()

# Step 2
complex2 = MyComplexNumber(60, 70)
complex2.new_attribute = 80
complex2.displayComplex()
print (complex2.real_part, complex2.imag_real, complex2.new_attribute)

# Step 3
# complex1.new_attribute

# Step 4
# del complex1.new_attribute

# Step 5
# del complex1
# complex1.displayComplex()

