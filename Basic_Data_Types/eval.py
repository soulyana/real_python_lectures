#calculator example
calc = input('Give me some maths to do: ')
print(eval(calc, {'pow': pow})) #safer to avoid executing unwanted code
