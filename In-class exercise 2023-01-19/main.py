#Read two things from the keyboard
#convert to ints and add
#print the result
#(What happens if the input is “abc” and “xyz”?)
#add error handling so it doesn't crash on bad data "Exception Handling"
alpha = input()
beta = input()
omega = None
try:
    omega = int(alpha)+int(beta)
except:
    print("Please enter numeric data")
print(omega)
