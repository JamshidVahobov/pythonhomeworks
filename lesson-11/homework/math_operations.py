def add(a, b):
    if str(a).isdigit() and str(b).isdigit():
        return int(a) + int(b)
    else:
        return "Both inputs must be numbers!"

    
def substract(a, b):
    if str(a).isdigit() and str(b).isdigit():
        return int(a) - int(b)
    else:
        return "Both inputs must be numbers!"
    
def multiply(a, b):
    if str(a).isdigit() and str(b).isdigit():
        return int(a)*int(b)
    else:
        return "Both inputs must be numbers!"

def divide(a, b):
    if str(a).isdigit() and str(b).isdigit() and not b == 0:
        return int(a)/int(b)
    else:
        return "Both inputs must be numbers!and b cannot be equal to 0"
