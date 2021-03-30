import collections

result_dict = collections.OrderedDict()

while True:
    try:
        path, code_line = input().split(" ")
        path = path.split("\\")[-1]
        if len(path) > 16:
            path = path[len(path) - 16:]
        key = (path, code_line)
        if key not in result_dict.keys():
            result_dict[key] = 1
        else:
            result_dict[key] += 1
    except:
        break
# sub_result_dict = collections.OrderedDict()
# for i in range(len(result_dict.items())-8,len(result_dict)):
#     sub_result_dict.
first = len(result_dict.items()) - 8
i = 0
for key, num in result_dict.items():
    if i >= first:
        path, code_line = key[0], key[1]
        print(path + " " + str(code_line) + " " + str(num))
    else:
        i += 1
