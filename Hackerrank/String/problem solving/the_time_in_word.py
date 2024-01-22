if __name__ == '__main__':
    dict_time = {
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        15:"quarter",
        20:"twenty",
        30:"half"
    }
    
    h = int(input().strip())
    m = int(input().strip())
    
    if m == 0:
        print("{} o' clock".format(dict_time[h]))
        
    elif m > 0 and m < 30:
        min = 'minute' if m == 1 else 'minutes'
        if m > 0 and m <= 13 :
            print("{} {} past {}".format(dict_time[m], min, dict_time[h]))
        elif m >= 14 and m <= 19:
            if m == 15:
                print("{} {} past {}".format(dict_time[m], min, dict_time[h]))
            else:
                modulo_m = m % 10
                print("{}teen {} past {}".format(dict_time[modulo_m], min, dict_time[h]))
        else:
            if m == 20:
                print("{} {} past {}".format(dict_time[m], min, dict_time[h]))
            else:
                modulo_m = m % 20
                print("twenty {} {} past {}".format(dict_time[modulo_m], min, dict_time[h]))
                
    elif m == 30:
        print("{} past {}".format(dict_time[m], dict_time[h]))
    
    elif m > 30 and m < 59:
        mudolo_m = 30 - (m % 30)
        min = 'minute' if mudolo_m == 1 else 'minutes'
        if mudolo_m > 0 and mudolo_m <= 13 :
            print("{} {} to {}".format(dict_time[mudolo_m], min, dict_time[h+1]))
        elif mudolo_m >= 14 and mudolo_m <= 19:
            if mudolo_m == 15:
                print("{} {} to {}".format(dict_time[mudolo_m], min, dict_time[h+1]))
            else:
                new_modulo_m = mudolo_m % 10
                print("{}teen {} to {}".format(dict_time[new_modulo_m], min, dict_time[h+1]))
        else:
            if mudolo_m == 20:
                print("{} {} to {}".format(dict_time[mudolo_m], min, dict_time[h+1]))
            else:
                new_modulo_m = mudolo_m % 20
                print("twenty {} {} to {}".format(dict_time[new_modulo_m], min, dict_time[h]))

