import docx
import pandas as pd
from tqdm import tqdm
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
while i<100:
    #print(f"{round(i/nu*100,1)}% |{'#'*int(i/nu*10)}{' '*int(10-(i/nu*10))}| {i}/{nu}",end="\r")
    w=" "
    while dr[i]!=' ' and i<nu-1 and dr:
        w=w+dr[i]
        i+=1
    print(w)
    print(w in bok["Слово"].values)
    if w not in bok["Слово"].values and w!=" ": 
        nr=pd.DataFrame([{'Слово':[w],'Частота встречи, раз':[1],'Частота встречи в %':[1]}])
        bok=pd.concat([bok,nr], ignore_index=True)
        print(nr)
        #bok.loc[len(bok)]={'Слово':w,'Частота встречи, раз':1,'Частота встречи в %':1}
    else:
        pass
    i+=1
    pass
#print(nu)
bok.drop(0,inplace=True)
print(bok)
#print(dr)
#h=input("Введите нужную букву или слово: ")
#print(dr.count(h))