def add(a,b):
    return a+b
def div(a,b):
    return a/b
def multiply(a,b):
    return a*b
def substract(a,b):
    return a-b
if __name__=="__main__":
    a=float(input("Give the first value: "))
    operation=input("Give the operation: ")
    b=float(input("Give the second value: "))
    match operation:
        case "+":
            print(add(a,b))
        case "-":
            print(substract(a,b))
        case "/":
            try:
                x=div(a,b)
                print(x)
            except ZeroDivisionError:
                print("Error! Can't divide by Zero")
            
        case "*":
            print(multiply(a,b))
    
