# coding:utf-8

import easyocr

def readimg(path):
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext(path)
    dataresult = []
    for data in result:
        dataresult.append(data[1])
        # print(data[1])
    return dataresult

if __name__ == '__main__':
    dataresult = readimg('./data/lt.jpg')
    # print(dataresult)
    for i in dataresult:
        print(i)