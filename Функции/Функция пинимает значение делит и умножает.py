def delenie_2 (x=int):
    # принимает число и дели его на 2   
    x = x / 2
    
    return x

def umnozhenie_4(x=int):
    # принимает число и умножает его на 4
    x = x * 4
    
    return x

per1 = int(input('Please, input first var '))

print(delenie_2(per1))
per2 = delenie_2(per1)

print (umnozhenie_4(per2))
