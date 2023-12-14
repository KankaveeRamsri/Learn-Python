if __name__ == "__main__" :
    s = input()
    mydict = {
        "alnum" : any(_.isalnum() for _ in s),
        "alpha" : any(_.isalpha() for _ in s),
        "digit" : any(_.isdigit() for _ in s),
        "lower" : any(_.islower() for _ in s),
        "upper" : any(_.isupper() for _ in s)
    }
    
    for i in mydict.values():
        print(i)
    