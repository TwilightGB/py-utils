import re
def read():
    doclist=[]
    with open("./data/1", "r") as f:  # 打开文件
        for line in f.readlines():
            line = line.strip('\n')  #去掉列表中每一个元素的换行符
            key = re.findall('\{field=(.*)\,value',line)
            value = re.findall('value=(.*)\}',line)
            docdict = {key[0]:value[0]}
            doclist.append(docdict)
    print(doclist)
    result = []
    keys = set()
    for x in doclist:
        a = list(x)[0]
        result.append(a)
        aa=a
        if str(a).startswith("weight"):
            aa="weight"
        elif str(a).startswith("distance"):
            aa= "distance"
        elif str(a).startswith("infopara"):
            aa= "infopara"
        keys.add(aa)
    countiInfop = [x for x in result if str(x).startswith("infoparam")]
    countWeight = [x for x in result if str(x).startswith("weight")]
    countdistance = [x for x in result if str(x).startswith("distance")]
    countfeature = [x for x in result if str(x).startswith("feature")]

    print(keys)
    print(len(keys))
    print(len(countiInfop))
    print(len(countWeight))
    print(len(countdistance))
    print(len(countfeature))
    return doclist


if __name__ == '__main__':
    read()