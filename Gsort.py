def is_smaller_than(a : float, b: float)-> bool:
    """
    Compare two numbers and return True if the second is greater than the first.
    """
    return b > a

def Gsort(list: list)-> list:
    """
    Sort a list of numbers in ascending order using the Gsort algorithm.
    The Gsort algorithm is a proper version of the "Stalin" sort algorithm.
    It works by checking if the next number is greater than the current number.
    If it is, it continues to the next number.
    If it is not, it removes the rest of the numbers from the list.
    The algorithm is not stable, but it is simple and easy to understand.
    It refers to the "Stalin" sort algorithm, which is a joke algorithm that is not meant to be taken seriously.
    And to a quote from a math teacher at USMB, france, who said "I stop reading after the first error". 
    
    DO NOT TAKE THIS ALGORITHM SERIOUSLY.
    """
    res =[]
    for i in range(len(list)):
        if i == len(list) - 1:
            res.append(list[i])
            break
        if is_smaller_than(list[i], list[i+1]):
            res.append(list[i])
        else:
            res.append(list[i])
            break  
    return res