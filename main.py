from collections import defaultdict


err_dict = defaultdict(list)

logfile = open('log.txt', 'r')
Lines = logfile.readlines()
  
dict_ranking = {}

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    eater_id = line.split(", ")[0]
    food_id = line.split(", ")[1].strip('\n')
    if food_id in err_dict[eater_id]:
        print("ERROR - same person eats same food again")
        exit()
    err_dict[eater_id].append(food_id)

    if food_id in dict_ranking:
        dict_ranking[food_id] = dict_ranking[food_id]+1
    else:
        dict_ranking[food_id] = 1

print(dict_ranking)
print(err_dict)

final = dict(sorted(dict_ranking.items(), key=lambda item: item[1], reverse=True))
print(final)

itr = 1
for key in final:
    if itr == 4:
        break

    print("\n Food item at rank", itr, "is: ", key)
    itr = itr + 1