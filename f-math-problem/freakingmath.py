from random import randint, choice
from calc import *
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1, 10)
    y = randint(1 ,10)
    er = randint(-1, 1)
    op = choice(["+", "-", "*", "/"])

    result = evaluate(x, y, op) + er
    return x, y, op, result

def check_answer(x, y, op, result, user_choice): 
    print(x,y,op,result,user_choice)
    if result == evaluate(x, y, op) and user_choice==True:
        return True
    elif result == evaluate(x, y, op) and user_choice==False:
        return False
    elif result != evaluate(x, y, op) and user_choice==False:
        return True
    elif result != evaluate(x, y, op) and user_choice==True:    
        return False
  