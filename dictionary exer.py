#1.
items = [3,5,7,9,11,13]
remove = items.pop(4)
print(remove)
items.insert(2,remove)
items.append(remove)
print(items)


#2
first_set = {23,42,65,57,78,83,29}
second_set = {57,83,29,67,73,43,48}
difference = first_set.intersection(second_set)
if difference:
   third_set = first_set.difference(second_set)
   print(f"common elements ={difference}")
   print(f"unique value ={third_set}")
else:
   print("no common elements")


#3
set1={27,43,34}
set2={34,93,22,27,43,53,48}
if set1.issubset(set2):
   print("set1 is subset of set2")
   set1.clear()
elif set1.issuperset(set2):
   print("set1 and set2 are superset")
else:
   print("set1 and set2 doesnot have any relation")

#4
month = {"Jan":47,"Feb":52,"March":47,"April":44,"May":52,"June":53,"July":54,"Aug":44,"Sept":54}
unique_value = list(set(month.values()))
print(unique_value)

#5
sample_list = [87,45,41,65,94,41,99,94]
unique_tuple = tuple(set(sample_list))
print(unique_tuple)
print("mininum number: ",min(unique_tuple()))
print("maximun number: ",max(unique_tuple()))

#6
club_A={"ram","hari","shyam"}
club_B={"ram","gita","hari"}
common = club_A.intersection(club_B)
if common:
   print("common members:",common)
else:
   print("no overlapping members found between groups")


#7
reqired_task={"email","report","meeting"}
completed_task={"email","report"}
if reqired_task.issubset(completed_task):
   print("all task done")
else:
   print("some task pending")