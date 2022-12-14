### Dates ###

from datetime import datetime

now = datetime.now() #fecha en base a este momento justo

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023, 1 , 1)# para definir un año se necesita el año el mes y el dia

print_date(year_2023)

from datetime import time #sirve para representar tiempo

current_time = time(21,6,0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date #sirve para representar fecha

current_date = date.today() #aqui utilizamos la fecha del dia de hoy pero podriamos darle argumentos

print(current_date.year)
print(current_date.month)
print(current_date.day)


current_date = date(2022,10,11) #Aqui pasamos los argumentos

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.today())# nos da la fecha de hoy


current_date = date(current_date.year , current_date.month , current_date.day )

#current_date = date(current_date.year + 1 , current_date.month + 1, current_date.day + 1) #modificamos la fecha

print(current_date)


######

diff = year_2023 - now #datetime -- diferencia de date time
print(diff)

diff = year_2023.date() - current_date
print(diff)


from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, 100, weeks=10) #el timedelta es para espacion de tiempo
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)