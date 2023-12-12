def check_green(RGB) :
    if RGB[0] < 0 or RGB[1] < 0 or RGB[2] < 0 or RGB[0] > 255 or RGB[1] > 255 or RGB[2] > 255 :
        return 'Value Out of Range'
    elif RGB[1] - ((RGB[0] + RGB[2])/2) >= 30 :
        return 'Green'
    else :
        return 'Not Green'

if __name__ == '__main__':
    Red_Green_Blue = [int(i) for i in input("RGB: ").split(',')]
    result = check_green(Red_Green_Blue)
    print(result)
    
        
    
    