# Первая буква в строке заглавная
stroka = "олдос Хаксли родился в 1894 году."
print(stroka)
stroka = "олдос Хаксли родился в 1894 году.".capitalize()
print(stroka)

# Из строки в список
stroka_1 = "Где это? Кто это? Когда это?"
print(stroka_1)
spisok_strok = stroka_1.split("?")
print(spisok_strok)

# Из списка в строку
lst = ["Рыжая", "лиса", "перепрыгнула", "через", "низкий", "забор", "." ]
print(lst)
new_list = " ".join(lst)
new_list = new_list[0:-2] + "."
print(new_list)

# Замена символов
bukva_o = "Ребенок - зеркало поступков родителей"
print(bukva_o)
bukva_o = bukva_o.replace("о", "0")
print(bukva_o)

# Поределение индекса в строке
slovo = "Хемингуэй"
print((slovo.index("у")))

# Кавычки

fraza = "Ma name \" Great \" Alexandr"
print(fraza)

# Конкатенация

Slozhenie_srok = "три" + "три" + "три"
print(Slozhenie_srok)
Umnozhenie_strok = "три" * 3
print(Umnozhenie_strok)

# Стрез строки

Srez = "И незачем так орать! Я и в первый разпрекрасно слышал."
Srez = Srez[0:20]
print(Srez)