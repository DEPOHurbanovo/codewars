# https://www.codewars.com/kata/5467e4d82edf8bbf40000155
def Descending_Order(num):
    """ So called 'cool' or 'pythonic' implementation"""
    return int("".join(sorted(str(num), reverse = True)))

def Descending_Order_Traditional(num):
    """ Simpler version, eariser to explain and understand"""
    list = []
    for char in str(num):
        list.append(char)
    list.sort(reverse = True)
    sorted_string = "".join(list)

    return int(sorted_string)
    
