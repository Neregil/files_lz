import docx
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

def ExtrText(path:str='lion.docx'):
    d=docx.Document('lion.docx')
    FullText=" ".join([p.text for p in d.paragraphs if p.text.strip()])
    return FullText

def WordStat(FullText):
    WorkStat=pd.DataFrame({
        'Слово':[''],
        'Частота встречи, раз':[''],
        'Частота встречи в %':[''],
    })
    WorkStat["Частота встречи, раз"] = (
        pd.to_numeric(WorkStat["Частота встречи, раз"], errors="coerce")
        .fillna(0)
        .astype(int)
    )
    TotalWords=-1
    TotalUniqueWords=0
    FullText=ExtrText()
    i=0
    FullTextLenght=len(FullText)
    while i<len(FullText):
        print(f"{round(i/FullTextLenght*100,1)}% |{'#'*int(i/FullTextLenght*10)}{' '*int(10-(i/FullTextLenght*10))}| {i}/{FullTextLenght}",end="\r")
        CurrentWord=""
        while i<FullTextLenght and not FullText[i].isspace():
            CurrentWord=CurrentWord+FullText[i]
            i+=1
        
        if CurrentWord!=" " and CurrentWord not in WorkStat["Слово"].values: 
            nr=pd.DataFrame([{'Слово':CurrentWord,'Частота встречи, раз':1,'Частота встречи в %':1}])
            WorkStat=pd.concat([WorkStat,nr], ignore_index=True)
            TotalWords+=1
            TotalUniqueWords+=1
        elif CurrentWord!=" ":
            idx=WorkStat[WorkStat["Слово"]==CurrentWord].index[0]
            WorkStat.at[idx,"Частота встречи, раз"]=int(WorkStat.at[idx,"Частота встречи, раз"])+1
            TotalWords+=1
        i+=1
    for i in range(1,TotalUniqueWords+1):
        WorkStat.iloc[i,2]=round(int(WorkStat.iloc[i,1])/TotalWords*100,6)
    #print(nu)
    WorkStat.drop(0,inplace=True)
    return WorkStat, TotalWords, TotalUniqueWords

def Letter_Stat(FullText):
    letter = [char.lower() for char in FullText if char.isalpha()] #Компактная запись для создания списка   если это буква добавляем букву в нижнем регистре
    LetterStat = Counter(letter)#Словарь, считает, сколько раз каждый элемент в ней встречается
    LetterStatLenght = len(letter)

    LetterDF= pd.DataFrame([
        {
            'Буква': letter,
            'Количество': count,
            'Частота в %': round(count / LetterStatLenght * 100, 6)
        }
        for letter, count in LetterStat.most_common()#Возвращает список кортежей, где каждый кортеж - это пара. По убыванию частоты
    ])
    return LetterDF

def Plate(LetterDF):
    plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans', 'sans-serif']#Была проблема с отображением кириллицы, поэтому добавил новые шрифты
    let = LetterDF['Буква']
    co = LetterDF['Количество']
    bars = plt.bar(let, co, color='lightgreen', edgecolor='black')
    plt.title('Статистика встречаемости букв в тексте', fontsize=14, fontweight='bold')
    plt.xlabel('Буквы', fontsize=12)
    plt.ylabel('Количество встреч', fontsize=12)
    plt.show()

def SaveTo(WorkStat,LetterDF,
           path_Words:str='lion.csv',
           path_Letters:str='LettersAndPeace.csv'):
    WorkStat.to_csv(path_Words,sep="|")
    LetterDF.to_csv(path_Letters,sep="|")

def main():
    full_text = ExtrText()
    work_stat, total_words, total_unique_words = WordStat(full_text)
    letter_df=Letter_Stat(full_text)

    print(letter_df)
    print(work_stat)
    print(total_words,total_unique_words)

    Plate(letter_df)
    SaveTo(work_stat,letter_df)

main()