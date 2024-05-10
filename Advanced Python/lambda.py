calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
print(calc(20))

print("---------------------------------")

filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums(): {}".format(filter_nums("Geek101")))

do_exclaim = lambda s: s + '!'
print("do_exclaim(): {}".format(do_exclaim("I am tired")))

find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum(): {}".format(find_sum(101)))

print("---------------------------------")

def cube(y):
    print(f"Finding cube of number : {y}")
    return y * y * y 

lambda_cube = lambda num : num ** 3

print("invoking function defined with def keyword:")
print(cube(30))

print("invoking lambda function : {}".format(lambda_cube(30)))

print("---------------------------------")

l = ["1", "2", "9", "0", "-1", "-2"]
print("Sorted numerically :",sorted(l, key=lambda x: int(x)))

print("Filtered positive even numbers : {}".format(list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0),l))))

print("Operation on each item using lambda and map() :",list(map(lambda x: str(int(x) + 10), l)))

print("---------------------------------")

my_list = [1, 2, 3, 4, 5]

new_list = list(filter(lambda x : x % 2 != 0,my_list))

print(new_list)

print("---------------------------------")



