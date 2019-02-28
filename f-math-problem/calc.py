def evaluate(x, y, op):
        
    result = 0

    if op == "+":
        result = x+y
    elif op == "-":
        result = x-y
    elif op == "x":
        result = x*y
    elif op == "/":
        result = x/y
    return result                 
# x = int(input("Nhap so x: "))
# y = int(input("Nhap so y: "))
# pt = (input("Nhap phep tinh(+, -, x, /): "))


# r = evaluate(x, y, pt)
# print(r)