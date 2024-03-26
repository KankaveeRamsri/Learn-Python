if __name__ == '__main__':
    time_dict = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty', 21: 'twenty-one', 22: 'twenty-two',
    23: 'twenty-three', 24: 'twenty-four', 25: 'twenty-five', 26: 'twenty-six',
    27: 'twenty-seven', 28: 'twenty-eight', 29: 'twenty-nine', 30: 'half'
    }
    
    hour = int(input())
    minute = int(input())
    
    if minute == 0:
        print(f"{time_dict[hour]} o' clock")
    elif minute == 15:
        print(f"{time_dict[minute]} past {time_dict[hour]}")
    elif minute == 30:
        print(f"{time_dict[minute]} past {time_dict[hour]}")
    elif minute == 45:
        print(f"{time_dict[minute]} to {time_dict[hour + 1]}")
    elif minute == 1:
        print(f"{time_dict[minute]} minute past {time_dict[hour]}")
    elif minute < 30:
        print(f"{time_dict[minute]} minutes past {time_dict[hour]}")
    elif minute == 59:
        print(f"{time_dict[60 - minute]} minute to {time_dict[hour + 1]}")
    else:
        print(f"{time_dict[60 - minute]} minutes to {time_dict[hour + 1]}")
    