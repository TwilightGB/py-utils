from utils import fileutil
import numpy as np
import matplotlib.pyplot as plt

from utils.commonUtil import listTocsv, listToexcel

'''
标记点
‘.’：点(point marker)
‘,’：像素点(pixel marker)
‘o’：圆形(circle marker)
‘v’：朝下三角形(triangle_down marker)
‘^’：朝上三角形(triangle_up marker)
‘<‘：朝左三角形(triangle_left marker)
‘>’：朝右三角形(triangle_right marker)
‘1’：(tri_down marker)
‘2’：(tri_up marker)
‘3’：(tri_left marker)
‘4’：(tri_right marker)
‘s’：正方形(square marker)
‘p’：五边星(pentagon marker)
‘*’：星型(star marker)
‘h’：1号六角形(hexagon1 marker)
‘H’：2号六角形(hexagon2 marker)
‘+’：+号标记(plus marker)
‘x’：x号标记(x marker)
‘D’：菱形(diamond marker)
‘d’：小型菱形(thin_diamond marker)
‘|’：垂直线形(vline marker)
‘_’：水平线形(hline marker)
'''
'''
颜色缩写：
‘b’：蓝色(blue)
‘g’：绿色(green)
‘r’：红色(red)
‘c’：青色(cyan)
‘m’：品红(magenta)
‘y’：黄色(yellow)
‘k’：黑色(black)
‘w’：白色(white)
'''
'''
线型：
‘-‘：实线(solid line style)
‘–‘：虚线(dashed line style)
‘-.’：点划线(dash-dot line style)
‘:’：点线(dotted line style)
'''

'''
图例位置：
'best'         : 0, (only implemented for axes legends)(自适应方式)
'upper right'  : 1,
'upper left'   : 2,
'lower left'   : 3,
'lower right'  : 4,
'right'        : 5,
'center left'  : 6,
'center right' : 7,
'lower center' : 8,
'upper center' : 9,
'center'       : 10
'''

def businessflow(listdata):
    fc = []
    zp = []
    esc = []
    hy = []
    xaxis = list(range(24))
    for data in listdata:
        dataarray = data.split(" ")
        fc.append(float(dataarray[0])*4 / 20000)
        zp.append(float(dataarray[2])*4 / 20000)
        esc.append(float(dataarray[4])*4 / 20000)
        hy.append(float(dataarray[6])*4 / 20000)
    lfc = plt.plot(xaxis, fc, 'r--', label='fc')
    lzp = plt.plot(xaxis, zp, 'g--', label='zp')
    lesc = plt.plot(xaxis, esc, 'b--', label='esc')
    lhy = plt.plot(xaxis, hy, 'k--', label='hy')
    plt.plot(xaxis, fc, 'ro-', xaxis, zp, 'g+-', xaxis, esc, 'b^-', xaxis, hy, 'g^')
    plt.title('hour flow business ')
    plt.xlabel('hour')
    plt.ylabel('num (w)')
    plt.legend()
    plt.show()


def sourcenums(listdata):
    dsp = []
    BUDGET = []
    IMC = []
    PMC = []
    FEATURE = []
    xaxis = list(range(24))
    for data in listdata:
        dataarray = data.split(" ")
        dsp.append(float(dataarray[0])*4 / 20000)
        BUDGET.append(float(dataarray[8])*4 / 20000)
        IMC.append(float(dataarray[10])*4 / 20000)
        PMC.append(float(dataarray[12])*4 / 20000)
        FEATURE.append(float(dataarray[14])*4 / 20000)
    lfc = plt.plot(xaxis, dsp, 'r--', label='dsp(1)')
    lzp = plt.plot(xaxis, BUDGET, 'g--', label='BUDGET(2)')
    lesc = plt.plot(xaxis, IMC, 'b--', label='IMC(4)')
    lhy = plt.plot(xaxis, PMC, 'y--', label='PMC(5)')
    lfc = plt.plot(xaxis, FEATURE, 'k--', label='FEATURE(6)')
    plt.plot(xaxis, dsp, 'ro-', xaxis, BUDGET, 'g+-', xaxis, IMC, 'b^-', xaxis, PMC, 'y^', xaxis, FEATURE, 'ko-')
    plt.title('hour flow resource ')
    plt.xlabel('hour')
    plt.ylabel('num (w)')
    plt.legend()
    plt.show()


def bingv2(lista,businessline):
    labels = [u'dsp(1)',u'BUDGET(2)',u'IMC(4)',u'PMC(5)',u'FEATURE(6)'] #定义标签
    colors = ['darkseagreen','sandybrown','cornflowerblue','moccasin','tan'] #每块颜色定义
    rangea=[1,2,4,5,6]
    if businessline=='fc':
        labels.append(u'HUG_HOUSE(6)')
        colors.append('lightslategray')
        rangea.append(8)
    elif businessline =='zp':
        labels.append(u'CONTEXT_FILTER(11)')
        colors.append('lightslategray')
        rangea.append(11)
    elif businessline=='esc':
        labels.append(u'DISCOUNT(12)')
        colors.append('lightslategray')
        rangea.append(12)
    elif businessline=='hy':
        print()

    dict = {}
    for flowcount in lista:
        array = str(flowcount).strip().split(" ")
        if array!='' and array[1]!='' :
            if int(array[1]) in rangea:
                dict.update({int(array[1]):array[0]})
    sizes = []
    sizes.append(dict.get(1))
    sizes.append(dict.get(2))
    sizes.append(dict.get(4))
    sizes.append(dict.get(5))
    sizes.append(dict.get(6))
    if businessline=='fc':
        sizes.append(dict.get(8))
    elif businessline =='zp':
        sizes.append(dict.get(11))
    elif businessline=='esc':
        sizes.append(dict.get(12))
    elif businessline=='hy':
        print()
    if businessline=='hy':
        explode = (0,0,0,0,0)
    else:
        explode = (0,0,0,0,0,0) #将某一块分割出来，值越大分割出的间隙越大
    patches,text1,text2 = plt.pie(sizes,
                                  explode=explode,
                                  labels=labels,
                                  colors=colors,
                                  autopct = '%3.2f%%', #数值保留固定小数位
                                  shadow = False, #无阴影设置
                                  startangle =90, #逆时针起始角度设置
                                  pctdistance = 0.6) #数值距圆心半径倍数距离
    #patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
    # x，y轴刻度设置一致，保证饼图为圆形
    plt.axis('equal')
    plt.legend(loc='best')
    # plt.savefig('flow.png', dpi=600)
    plt.show()

def bingbusiness(dataa):
    plt.figure(figsize=(7,9)) #调节图形大小
    labels = [u'fc',u'zp',u'esc',u'hy'] #定义标签
    sizes = [] #每块值
    for idata in dataa:
        array = str(idata).strip().split(" ")
        sizes.append(array[0])
    colors = ['darkseagreen','tan','cornflowerblue','moccasin'] #每块颜色定义
    explode = (0,0,0,0) #将某一块分割出来，值越大分割出的间隙越大
    patches,text1,text2 = plt.pie(sizes,
                                  explode=explode,
                                  labels=labels,
                                  colors=colors,
                                  autopct = '%3.2f%%', #数值保留固定小数位
                                  shadow = False, #无阴影设置
                                  startangle =90, #逆时针起始角度设置
                                  pctdistance = 0.6) #数值距圆心半径倍数距离
    #patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
    # x，y轴刻度设置一致，保证饼图为圆形
    plt.axis('equal')
    plt.legend(loc='best')
    # plt.savefig('flow.png', dpi=600)
    plt.show()

if __name__ == "__main__":
    # listdata = fileutil.readFile("/Users/gengbin/Documents/zhour.log")
    # listdatb=[]
    # for dataa in listdata:
    #     dicta = {}
    #     data = str(dataa).split(" ")
    #     dicta.update({data[1]:float(data[0])*2/10000})
    #     dicta.update({data[3]:float(data[2])*2/10000})
    #     dicta.update({data[5]:float(data[4])*2/10000})
    #     dicta.update({data[7]:float(data[6])*2/10000})
    #     listdatb.append(dicta)
    # listToexcel(listdatb,'../data/hourbusiness1.xlsx')
    # listdatb = fileutil.readFile("/Users/gengbin/Documents/zhoursource.log")
    # businessflow(listdata)
    # sourcenums(listdatb)
    dataa = fileutil.readFile("../data/data.log")
    # bingv2(dataa,'hy')
    bingbusiness(dataa)