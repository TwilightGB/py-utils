import os

#读取目录
def readFiles(path):
    files= os.listdir(path) #得到文件夹下的所有文件名称
    s = []
    for file in files: #遍历文件夹
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            if file.startswith("."):
                continue
            filename = path+"/"+file
            f = open(filename)
            iter_f = iter(f)
            str = ""
            for line in iter_f: #遍历文件，一行行遍历，读取文本
                str = str + line
            tuple=(filename,str)
            s.append(tuple) #每个文件的文本存到list中
    return s

#读取文件
def readFile(path):
    filelist = []
    with open(path, "r") as f:
        for line in f.readlines():
            filelist.append(line)
    return filelist


def readFiles_a(path):
    files= os.listdir(path) #得到文件夹下的所有文件名称
    sets = set()
    for file in files: #遍历文件夹
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            if file.startswith("."):
                continue
            filename = path+"/"+file
            f = open(filename)
            iter_f = iter(f)
            for line in iter_f: #遍历文件，一行行遍历，读取文本
                sets.add(line)
    return sets

#集合写入文件
def writeFile(filepath,collection):
    with open(filepath, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        for data in collection:
            f.write(data)


if __name__ == '__main__':
    filelist = readFile("/Users/gengbin/Documents/store/143147_store")
    setkey = set()
    for data in filelist:
        if(str(data).startswith("distance")):
            setkey.add("distance\n")
        elif(str(data).startswith("weight")):
            setkey.add("weight\n")
        else:setkey.add(data.split(":")[0]+"\n")
    writeFile("./store.log",sorted(setkey))