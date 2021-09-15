string = input()   # Task 1.1
cnt = 0
for i in string:
    cnt += 1
print("String length is", cnt)

##############################

string = input().lower()   # Task 1.2
symbol_dict = {}
for ch in string:
    symbol_dict.update({ch : string.count(ch)})
print(symbol_dict)

##############################

collect = sorted(set(input().split(",")))   # Task 1.3
print(collect)

##############################

num = int(input("Put the number in - "))   # Task 1.3
divisors = set()
for digit in range(1, num+1):
    if num % digit == 0:
        divisors.add(digit)
print(sorted(divisors))

##############################

base_dict = {5: "a", 3: "b", 4: "c", 2: "d", 1: "e"}   # Task 1.4
print(sorted(base_dict.items()))

##############################

in_list = [{"V":"S001"},   # Task 1.5
           {"V": "S002"}, 
           {"VI": "S001"}, 
           {"VI": "S005"}, 
           {"VII":"S005"}, 
           {"V":"S009"},
           {"VIII":"S007"}]
out_set = set()        
for item in in_list:
    for value in item.values():
        out_set.add(value)
print(out_set)

##############################

in_tuple = tuple(map(int, (input().split(","))))   # Task 1.6
new_int = ""
for item in in_tuple:
    new_int += str(item)
new_int = int(new_int)
print(new_int)

##############################

a, b, c, d = 2, 4, 3, 7   # Task 1.6
for i in range(c, d+1):
    print("\t", i, end = "")
print()
for j in range(a, b+1):
    print(j, end = "\t")
    for k in range(c, d+1):
        print(j * k, end = "\t")
    print()