import pandas as pd
import matplotlib.pyplot as plt
import csv

def ReadParq(path:str='titanic.parquet'):
    TitanicParq=pd.read_parquet('titanic.parquet', engine='fastparquet')# Читаю паркер с раскодировкой
    return TitanicParq

def CreateCSV(TitanicParq):
    TitanicWrite=open('titanic.csv', 'w')
    Writer=csv.writer(TitanicWrite, delimiter='|')
    Writer.writerows(TitanicParq.values)   # Записываем данные
    Writer.writerow(TitanicParq.columns)  # Записываем названия столбцов
    TitanicWrite.close()

def CreatePandas(TitanicParq):
    # Считаем процент выживших и невыживших по каждому классу
    SurvivorsTab=pd.crosstab(  #делаем таблицу для matplotlib с классом и выживаемостью
        TitanicParq['Pclass'],
        TitanicParq['Survived'],
        normalize='index'  #позволяет узнать долю каждого результата относительно общего количества
    ) * 100
    return SurvivorsTab

def CreatePlate(SurvivorsTab):
    #делаем гистограмму
    Plate=['первый класс','второй класс','третий класс']
    plt.bar(Plate,SurvivorsTab[0],bottom=SurvivorsTab[1],color="#F00B0F")   # bottom указывает с какой высоты начинать строить тех кто не выжил
    plt.bar(Plate,SurvivorsTab[1],color="#0009FF")
    plt.title('Выжиживаемость пасажиров Титаника')
    plt.ylabel('Проценты, синим цветом выжившие')

def main():
    tit_prq=ReadParq()
    CreateCSV(tit_prq)
    surv_tab=CreatePandas(tit_prq)
    CreatePlate(surv_tab)
    
    print(tit_prq)
    plt.show()

main()