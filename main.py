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

def check_number(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'

if __name__ == '__main__':
    n = [int(i) for i in input().split()]

    height = n[0]
    width = n[1]

    for i in range(1,height,2):
        mark = '.|.'
        print((mark * i).center(width,'-'))
    
    print(('WELCOME').center(width,'-'))
    
    for i in range(height-2,0,-2):
         mark = '.|.'
         print((mark * i).center(width, '-'))