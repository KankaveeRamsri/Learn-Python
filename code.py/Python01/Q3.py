import random
import time

#BasicSearch
print('-'*30)
print("      ( Basic Search )         ")
lower = -100
upper = 100
data_num = []
position_max_number = []
position_min_number = []
for n in range(100,1100,100):
    print("--------- (n = {}) ---------".format(n))
    for i in range(0,n):
        rand_num = random.randint(lower,upper)
        data_num.append(rand_num)
    for i in range(0,n):
        if data_num[i] == max(data_num) :
            position_max_number.append(i) 
        if data_num[i] == min(data_num) :
            position_min_number.append(i)
    print('-'*30)

    avg_time_max = []
    for i in range(0,10) :
        startTime = time.perf_counter_ns()
        val = max(data_num)
        endTime = time.perf_counter_ns()
        avg_time_max.append(endTime - startTime)
    print("Process time to find maximum number #{} : {}".format(n,sum(avg_time_max) / 10))

    avg_time_min = []
    for i in range(0,10) :
        startTime = time.perf_counter_ns()
        val2 = min(data_num)
        endTime = time.perf_counter_ns()
        avg_time_min.append(endTime - startTime)
    print("Process time to find minimum number #{} : {}".format(n,sum(avg_time_min) / 10))
    print('-'*30)


#BinaryTreeSearch
print("    ( Binary Tree Search )     ")
class BST : 
    def __init__(self,key) :
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data) :
        if self.key is None :
            self.key == data
            return
        if self.key == data :
            return
        if self.key > data :
            if self.lchild :  
                self.lchild.insert(data)
            else :
                self.lchild = BST(data)
        else :
             if self.rchild :  
                self.rchild.insert(data)
             else :
                self.rchild = BST(data)
    
    def search(self,data) :
        if self.key == data :
            print("Node is found!")
            return
        if data < self.key :
            if self.lchild:
                self.lchild.search(data)
            else :
                print("Node is not present in tree!")
        else :
            if self.rchild:
                self.rchild.search(data)
            else :
                print("Node is not present in tree!")
    
    def preorder(self) :
        print(self.key,end = ' ')      
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self) :
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end= ' ')
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self) :
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end = ' ')
    
    def delete(self,data) :
        if self.key is None :
            print("Tree is empty!")
            return
        if data < self.key :
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else :
                print("Given Node is Not present in the tree!")
        elif data > self.key :
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else :
                print("Given Node is Not present in the tree!")
        else : 
            if self.lchild is None :
                temp = self.rchild 
                self = None   
                return temp  
            if self.rchild is None :
                temp = self.lchild 
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self
    
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        return current.key
    
    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        return current.key

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        
        if self.rchild is None and self.lchild is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        
        if self.rchild is None:
            lines, n, p, x = self.lchild._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        
        if self.lchild is None:
            lines, n, p, x = self.rchild._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self.lchild._display_aux()
        right, m, q, y = self.rchild._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    

lower = -100
upper = 100
data_num = []
for n in range(100,1100,100) :
    for i in range(0,n):
        rand_num = random.randint(lower,upper)
        data_num.append(rand_num)
    
    root = BST(data_num[0])
    for i in data_num[1:] : 
        root.insert(i)
    
    print('-' * 30)


    result_1 = root.min_node()
    print("node with smallest key #{} is {}".format(n,result_1))
    result_2 = root.max_node()
    print("node with maximum key #{} is {}".format(n,result_2))


    print('-' * 30)


    avg_time_max = []
    for i in range(0,10) :
        startTime = time.perf_counter_ns()
        val = root.max_node()
        endTime = time.perf_counter_ns()
        avg_time_max.append(endTime - startTime)
    print("Process time to find maximum number #{} : {}".format(n,sum(avg_time_max) / 10))

    avg_time_min = []
    for i in range(0,10) :
        startTime = time.perf_counter_ns()
        val2 = root.min_node()
        endTime = time.perf_counter_ns()
        avg_time_min.append(endTime - startTime)
    print("Process time to find minimum number #{} : {}".format(n,sum(avg_time_min) / 10))

    print('-' * 30)
