# coding: utf-8
def which_is_larger(number1, number2):
    if number1 > number2:
        print(number1, 'is larger')
        return True
    elif number2 > number1:
        print(number2, 'is larger')
        return number2
    elif number1 == number2:
        print(number1, 'is equal to', number2)
        return (number1, number2)
        
        
# coding: utf-8
def compare_strings(string1, string2, strict=True):
    """compare if two strngs are equal to each other or not
    returns True if they are equal
    returns False if not
    """
    if isinstance(string1, str) and isinstance(string2, str):
        pass
    else:
        print('this function takes only strings')
        return None
    #all fine
    if strict:
        if string1.lower() == string2.lower():
            return True
        else:
            return False
    else:
        #nonstrict
        if string1 == string2:
            return True
        else:
            return False
            
    

if __name__ == '__main__':
    print('you lanuched me') 
