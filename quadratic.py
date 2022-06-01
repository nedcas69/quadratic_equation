print('Решаем уравнение a•x²+b•x+c=0') 
#берем у пользователя значения
s = input('Введите значение a: ')
n = input('Введите значение b: ')
v = input('Введите значение c: ')
#Подключаем re
import re
# производим выборку цифр с помощью регулярных значений, она возврашает массив цифр  
a = re.findall(r'\d+', s)
b = re.findall(r'\d+', n)
c = re.findall(r'\d+', v)
#массив цифр переводим в строку
a = ''.join(a)
b = ''.join(b)
c = ''.join(c)
# если значение строк не пустая переводим значения в float и решаем задачу
if  a.strip() == 0  or  b.strip() == 0 or  c.strip() == 0:
    a = float(a)
    b = float(b)
    c = float(c)
    discriminant = b**2 - 4*a*c
    print('Дискриминант = ' + str(discriminant))

    if a == 0:
        if b == 0:
            if c == 0:
                print('x любое значение!')
            else:
                print('Решений нет!') 
        else:
            x = -c/b
            print('x = ' + str(x))

    else:    
        if discriminant < 0:
            print('Корней нет!')
        elif discriminant == 0:
            x = -b / (2 * a)
            print('x = ' + str(x))
        else:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
            print('x₁ = ' + str(x1))
            print('x₂ = ' + str(x2))
else:
    #если в значениях нету цифр то печатаем значения как есть.
    print(str(s) + '•x²+' + str(n) + '•x+' + str(v) + '=0')