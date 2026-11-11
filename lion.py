import docx
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
#from tqdm import tqdm
d=docx.Document('lion.docx')
#print(d.paragraphs[0].text)
dr=" ".join([p.text for p in d.paragraphs if p.text.strip()])
bok=pd.DataFrame({
    'Слово':[''],
    'Частота встречи, раз':[''],
    'Частота встречи в %':[''],
})
nu=len(dr)
i=0
bok["Частота встречи, раз"] = (
    pd.to_numeric(bok["Частота встречи, раз"], errors="coerce")
    .fillna(0)
    .astype(int)
)
sl=0
wd=-1
wd1=0
nu=nu/1000
while i<nu:
    print(f"{round(i/nu*100,1)}% |{'#'*int(i/nu*10)}{' '*int(10-(i/nu*10))}| {i}/{nu}",end="\r")
    w=""
    while i<nu and not dr[i].isspace():
        w=w+dr[i]
        i+=1
    
    #print(w)
    #print(w in bok["Слово"].values)
    if w!=" " and w not in bok["Слово"].values: 
        nr=pd.DataFrame([{'Слово':w,'Частота встречи, раз':1,'Частота встречи в %':1}])
        bok=pd.concat([bok,nr], ignore_index=True)
        #bok.loc[len(bok)]={'Слово':w,'Частота встречи, раз':1,'Частота встречи в %':1}
        wd+=1
        wd1+=1
    elif w!=" ":
        idx=bok[bok["Слово"]==w].index[0]
        bok.at[idx,"Частота встречи, раз"]=int(bok.at[idx,"Частота встречи, раз"])+1
        wd+=1
    i+=1
    pass
for i in range(1,wd1+1):
    bok.iloc[i,2]=round(int(bok.iloc[i,1])/wd*100,6)
#print(nu)
bok.drop(0,inplace=True)



l = [ch.lower() for ch in dr if ch.isalpha()] #Компактная запись для создания списка   если это буква добавляем букву в нижнем регистре
cs = Counter(l)#Словарь, считает, сколько раз каждый элемент в ней встречается
tl = len(l)

bokl= pd.DataFrame([
    {
        'Буква': l,
        'Количество': c,
        'Частота в %': round(c / tl * 100, 6)
    }
    for l, c in cs.most_common()#Возвращает список кортежей, где каждый кортеж - это пара. По убыванию частоты
])
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans', 'sans-serif']#Была проблема с отображением кириллицы, поэтому добавил новые шрифты
let = bokl['Буква']
co = bokl['Количество']
bars = plt.bar(let, co, color='lightgreen', edgecolor='black')
plt.title('Статистика встречаемости букв в тексте', fontsize=14, fontweight='bold')
plt.xlabel('Буквы', fontsize=12)
plt.ylabel('Количество встреч', fontsize=12)

print(bokl)
print(bok)
print(wd,wd1)
bok.to_csv('lion.csv',sep="|")
bokl.to_csv('LettersAndPeace.csv',sep="|")
plt.show()
#print(dr)
#h=input("Введите нужную букву или слово: ")
#print(dr.count(h))