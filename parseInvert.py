from utils import fileutil
from utils.commonUtil import listToexcel


def parseInvert(path):
    list = fileutil.readFiles(path);
    dictdoc = {}
    for tuple in list:
        dict = {}
        name = str(tuple[0]).split("/")[-1]
        data = tuple[1]
        countfull = data.count("fullcontext")
        countfullexp = data.count("fullcontext_exp")
        base = countfull-countfullexp
        dict.update({"fullcontext_base":base})
        dict.update({"fullcontext_exp":countfullexp})
        datasize = len(data.split("\n"))
        dict.update({"docsize":datasize})
        dict.update({"ratefullcontext":round(base/datasize,2)})
        dictdoc.update({name:dict})
    return dictdoc

def parseStore(path):
    list = fileutil.readFiles(path);
    dictdoc = {}
    for tuple in list:
        dict = {}
        name = str(tuple[0]).split("/")[-1].split("_")[0]
        data = tuple[1]
        docsize = len(data.split("\n"))
        distancefull = data.count("distance")
        distancefullexp = data.count("distance_exp")
        base = distancefull-distancefullexp
        dict.update({"distance_base":base})
        dict.update({"distance_exp":distancefullexp})
        dict.update({"ratedistance":round(base/docsize,2)})

        weightfull = data.count("weight")
        weightfullexp = data.count("weight_exp")
        baseweight = weightfull-weightfullexp
        dict.update({"weightfull_base":baseweight})
        dict.update({"weightfull_exp":weightfullexp})
        dict.update({"rateweight":round(baseweight/docsize,2)})
        dict.update({"docstoresize":docsize})
        dictdoc.update({name:dict})
    return dictdoc

if __name__ == '__main__':
    print("a")
    # list = []
    # dictInvert = parseInvert("/Users/gengbin/Documents/invert")
    # dictstore = parseStore("/Users/gengbin/Documents/store")
    # list.append(dictInvert)
    # list.append(dictstore)
    # lista = mergedict(dictInvert,dictstore)
    # listToexcel(lista,"./text.xlsx")



