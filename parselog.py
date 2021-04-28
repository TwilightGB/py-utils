import json
from itertools import groupby
from operator import itemgetter

from utils import fileutil
from utils.commonUtil import listToexcel, listTocsv

#  awk '$2>"09:30:00" && $2<"10:30:00"' lego_featureincjob.log |grep gengbin| grep -v "{}"  >gengbin.log
#  awk '{print $2","$3,$NF}' gengbin.log >log.log

def parse(path):
    filelist = fileutil.readFile(path)
    lista = []
    entityids = set()
    for datai in filelist:
        time = str(datai).split(" ")[0]
        data = str(datai).split(" ")[1]
        key = data.split("|")[0]
        entityids.add(key)
        value = data.split("|")[1]
        json_dict = json.loads(value)
        dicta = {}

        for k,v in json_dict.items():
            for ka,va in v.items():
                dicta.update({"entityid":key})
                dicta.update({"time":time})
                valueone = ",".join(va)
                dicta.update({ka:valueone})
        lista.append(dicta)
        # for i in lista:
        #     stra = i.get("entityid")
        #     if not str(stra).isdigit():
        #         print(i)

    print(len(entityids))
    return lista


def sort_gorup(lista):
    global aglist
    lista.sort(key=itemgetter('entityid'))
    lstg = groupby(lista, itemgetter('entityid'))
    aglist = []
    for key, group in lstg:
        for g in group:  # group是一个迭代器，包含了所有的分组列表
            aglist.append(g)


if __name__ == '__main__':
    # lista = parse("/Users/gengbin/Documents/zpparse.log")
    # sort_gorup(lista)
    # listTocsv(aglist,"./zp.csv")

    #   倒排信息
    # filelist = fileutil.readFile("/Users/gengbin/Documents/1369811164917149696")
    # exp = [expdata for expdata in filelist if str(expdata).startswith('_fullcontext')&str(expdata).__contains__('exp')]
    # noexp = [n for n in filelist if str(n).find('fullcontext')>0& n.find('exp')==0]
    # print(exp)
    # print(noexp)
    # setexp = set()
    # setnoexp = set()
    # for x in exp:
    #     setexp.add(x.split('_')[-1])
    # for y in noexp:
    #     setnoexp.add(y.split('_')[-1])
    # print(len(setexp))
    # print(len(setnoexp))
    # print(setexp)
    # print(setnoexp)

    #正排信息
    filelist = fileutil.readFile("/Users/gengbin/Documents/1379991557712650240")
    expweight = [w for w in filelist if str(w).startswith('{field=weight')&str(w).__contains__('exp')]
    noexpweight = [n for n in filelist if str(n).startswith('{field=weight')& ('exp' not in n)]
    setw = set()
    setnw = set()
    for x in expweight:
        setw.add(x.split(',')[0].split('=')[1][10:])
    for y in noexpweight:
        setnw.add(y.split(',')[0].split('=')[1][6:])
    setwsort = sorted(list(set(setw)))
    setnwsort = sorted(list(set(setnw)))
    print(expweight)
    print(noexpweight)
    print(setwsort)
    print(setnwsort)
    print(setw -setnw)
    print(len(expweight))
    print(len(noexpweight))
