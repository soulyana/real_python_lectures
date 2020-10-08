a = 1
b = 'global'
c = 'another global'

def function(): 
    a = 2
    b = 'local'
    print(a, b)
    print(vars()) #what variables are available at this scope
    print(c)

print(a, b)
function()
print(a,b)
#print(globals())
