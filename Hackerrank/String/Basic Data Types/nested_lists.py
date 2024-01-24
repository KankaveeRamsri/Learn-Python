if __name__ == "__main__":
    NameList = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        NameList.append([name,score])
    
    
    DictName = dict(NameList)
    NameDict = dict(sorted(DictName.items()))
    
    discard_key = [key for key,values in NameDict.items() if values == min(NameDict.values())]
    for key in discard_key:
        del NameDict[key]
    
    minimum_score = min(NameDict.values())
    for key, values in NameDict.items():
        if values == minimum_score:
            print(key)
    
    