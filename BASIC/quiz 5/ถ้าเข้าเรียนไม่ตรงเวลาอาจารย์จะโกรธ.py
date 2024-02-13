def make_decision(threshhold, times):
    early = [int(i) for i in times if int(i) < 0 ]
    on_time = [int(i) for i in times if int(i) == 0]
    late = [int(i) for i in times if int(i) > 0]
    
    if len(early) + len(on_time) >= threshhold:
        print("Decision: NO")
    else:
        print("Decision: YES")
    
    

if __name__ == "__main__":
    threshhold = int(input("Threshhold Number: "))
    times = input("Time: ").split()
    
    make_decision(threshhold,times)
    
    