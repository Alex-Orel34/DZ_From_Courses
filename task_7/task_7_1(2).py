from typing import NoReturn


def Get_sm(n):
    return n * 2.54
def Get_dm(n): 
    return n / 2.54
def Get_km(n):
    return n / 1.6
def Get_ml(n):
    return n * 1.6
def Get_kg(n):
    return n * 0.45
def Get_fn(n):
    return n / 0.45
def Get_gr(n):
    return n * 28.3
def Get_un(n):
    return n / 28.3
def Get_l(n):
    return n * 4.5
def Get_gl(n):
    return n / 4.5
def Get_l_from_pint(n):
    return n *  0.56
def Get_pint(n):
    return n / 0.56

while True:
    Number_of_confertation=int(input('Put number of convertation :'))
    if Number_of_confertation == 0:
        break
    n=int(input('Put your digit :'))
    if Number_of_confertation == 1:
        print(Get_sm(n))
    if Number_of_confertation == 2:
        print(Get_dm(n))
    if Number_of_confertation == 3:
        print(Get_km(n))
    if Number_of_confertation == 4:
        print(Get_ml(n))
    if Number_of_confertation == 5:
        print(Get_kg(n))
    if Number_of_confertation == 6:
        print(Get_fn(n))
    if Number_of_confertation == 7:
        print(Get_gr(n))
    if Number_of_confertation == 8:
        print(Get_un(n))
    if Number_of_confertation == 9:
        print(Get_l(n))
    if Number_of_confertation == 10:
        print(Get_gl(n))
    if Number_of_confertation == 11:
        print(Get_l_from_pint(n))
    if Number_of_confertation == 12:
        print(Get_pint(n))
