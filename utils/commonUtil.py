
import pandas as pd

#列表转化为excel
def listToexcel(lista,path):
    pf = pd.DataFrame(lista)
    pf.to_excel(path, encoding='utf-8', index=False)


#字典合并
def mergedict(dicta,dictb):
    lista = []
    for k, v in dicta.items():
        newdict = dictb.get(k)
        newdict.update({"docid": k})
        dictnew = dict(newdict, **v)  # 合并字典
        lista.append(dictnew)
    return lista