preobr = input('Введите число для преобразования ')
# Функция принимает строку и преобразовывает е в тип Float с исключениями
def preobrazovanie (x):
    try:
         x = float(x)
         return x
    except(ValueError):
        print('input error')
    


print(preobrazovanie(preobr))