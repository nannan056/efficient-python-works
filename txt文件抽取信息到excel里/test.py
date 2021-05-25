import pandas as pd
with open("my.txt","r",encoding="utf-8") as f:
    data=f.read()
    # print(data)

line_num=147
t1=['' for row in range(line_num)]
t2=['' for row in range(line_num)]
data_split=data
for i in range(line_num):
    data_split=data_split.split('tables/',1)[1]
    tmp=data_split.split('\n',1)[0]
    if tmp[-1]!='量':
        t1[i]=tmp
    else:
        t2[i]='是'
        t1[i]=tmp.split()[0]
df={'a':t1,'b':t2}
df=pd.DataFrame(df)
df.to_excel('df.xlsx')

