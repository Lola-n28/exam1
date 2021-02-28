# Дана строка нечетной длины больше 7 символов, вернуть строку, состоящую из трех средних символов данной строки 
# Пример:
# some_string = "Adverts"
# Output: "ver"

some_string = "Adverts"

if len(some_string)%2==1:
    print(some_string[2:5])
elif len(some_string)%2==0:
    print(some_string[0:2]+some_string[-2:])


