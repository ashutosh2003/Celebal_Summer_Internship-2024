##Author-Ashutosh Sahoo , Assignment of Week1
##Lower Triangular
print('Lower Triangular:\n')
def lower_triangular(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()
lower_triangular(5)


##Upper Triangular
print('Upper Triangular:\n')
def upper_triangular(n):
    for i in range(n):
        for j in range(n):
            if j < i:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()
upper_triangular(5)

##Pyramid
print('Pyramid:\n')
def pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for j in range(2 * i + 1):
            print("*", end=" ")
        print()
pyramid(5)