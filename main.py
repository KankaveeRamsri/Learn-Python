# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = [float(x) for x in line]
#         student_marks[name] = scores
#     query_name = input()
    
#     for key, value in student_marks.items():
#         if key == query_name :
#             values = sum(value) / len(value)
#             print('{:.2f}'.format(values))

print("------------------------------------")

if __name__ == '__main__':
    first_multiple_input = [int(i) for i in input().split()]
    n = first_multiple_input[0]
    k = first_multiple_input[1]
    
    bill = [int(i) for i in input().split()[:n]]
    
    b = int(input())
    
    bill_anna = (sum(bill) - bill[k]) / 2
    
    if bill_anna == b:
        print("Bon Appetit")
    else:
        print(int(b-bill_anna))    
    
    