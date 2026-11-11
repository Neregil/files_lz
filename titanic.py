import pandas as pd
import matplotlib.pyplot as plt
import csv

td=pd.read_parquet('titanic.parquet', engine='fastparquet')# Читаю паркер с раскодировкой
tv=open('titanic.csv', 'w')
wr=csv.writer(tv, delimiter='|')
wr.writerows(td.values)   # Записываем данные
wr.writerow(td.columns)  # Записываем названия столбцов
print(td)
tv.close()

# Считаем процент выживших и невыживших по каждому классу
s=pd.crosstab(  #делаем таблицу для matplotlib с классом и выживаемостью
    td['Pclass'],
    td['Survived'],
    normalize='index'  #позволяет узнать долю каждого результата относительно общего количества
) * 100

#делаем гистограмму
c=['первый класс','второй класс','третий класс']
plt.bar(c,s[0],bottom=s[1],color="#FF0B0F")   # bottom указывает с какой высоты начинать строить тех кто не выжил
plt.bar(c,s[1],color="#0009FF")
plt.title('Выжиживаемость пасажиров Титаника')
plt.ylabel('Проценты, синим цветом выжившие')
plt.show()