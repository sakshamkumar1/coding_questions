'''
print("My name is {} and I am an {}.".format('Saksham', 'engineer'))
name = 'Saksham'
age = 27
profession = 'engineer'
print(f"My name is {name} and I am {age} years old.")
'''
def division(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print('Division not defined.')

division(3, 0)rotate