x = "Sfundo Glen Cele is winning over 2 million in the next 24 hours"
try:
    print(x)
except NameError :
    print("Variable x not defined")
finally :
    print("Everything went wrong")
    
    x = -1
    
    if x < 0:
        raise Exception("Sorry no numbers less then zero")
