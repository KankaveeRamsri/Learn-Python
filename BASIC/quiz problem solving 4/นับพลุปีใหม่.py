scores = dict()
color_codes = "RGBWYPCOMU"
while (data := input("Enter color code: ")).upper() != "END":
    is_new_key = False

    last_digit_index = 0
    last_key_index = 0
    key_name = []
    value = []

    for i, c in enumerate(data):
        if c.isdigit():
            value.append(c)
            if i + 1 < len(data) and data[i + 1].isdigit():
                is_new_key = False
            else:
                is_new_key = True
        else:
            ckey = c.upper()
            if ckey not in color_codes:
                ckey = "U"
            if ckey not in key_name:
                key_name.append(ckey)

        # print(key_name)
        # print(value)
        if is_new_key:
            is_new_key = False
            key = "".join(sorted(key_name))

            if "U" in key or len(key) == 0:
                key = "U"

            if key not in scores:
                scores[key] = 0
            val = int("".join(value))
            scores[key] += val
            value = []
            key_name = []

            print(f"{key:<5} -> {scores[key]:>10}")

print("\nFireworks Statistic")
for key in sorted(scores.keys()):
    print(f"{key:<5} -> {scores[key]:>10}")

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
    
#     print("{}\n{}\n{}".format(a+b,a-b,a*b))