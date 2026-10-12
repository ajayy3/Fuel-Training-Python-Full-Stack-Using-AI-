# fruits={"apple","banana","mango"}
# nums=[10,20,30,40,50]
# mixed=[1,"Ai",3.5,True]
# empty=[]

# print(len(fruits))
# print(nums[3])
# -----------------------------------------------------------------------------------------------------------------
# slicing
# num=[1,2,3,4,5]
# print(num[1:4])
# print(num[:2])
# print(num[-2:])
# print(num[:-2])
# print(num[::-1])
# ------------------------------------------------------------------------------------------------------
# fruits =["apple","banana"]
# fruits[0]="grapes"
# fruits.append("mango")
# fruits.insert(1,"kiwi")
# fruits.extend(["pear","fig"])
# print(fruits)
# -------------------------------------------------------------------------------------------------------
# Removing items

# items=[1,2,3,4,5]
# items.pop()
# items.pop(0)
# print(items)
# del items[0]
# print(items)
# --------------------------------------
# sorting and seraching

# marks=[46,45,48,47]
# marks.sort()
# print(marks)
# marks.sort(reverse=True)
# print(marks)
# marks.reverse()

# print(33 in marks)
# print(marks.count(45))
# ---------------------------------------------------------------------------
# looping through a list

# names=["ajay","vijay","neha"]

# for name in names:
#     print(name)
# for i, name in enumerate(name):
#     print(i,name)
# -------------------------------------------------------------------------
# nums=[4,9,2,7]
# print(sum(nums))
# print(min(nums))
# print(max(nums))
# print(sorted(nums))
# ----------------------------------------------------------------------------
# squares=[x*x for x in range(1, 6)]
# print(squ)
# --------------------------------------------------------------------------
# tuples

# colors=("red","yellow","blue")
# print(colors[0])
# print(len(colors))
# ------------------------------------------------------------------------------------
# a= (5)
# b=(10,)
# print(type(a))
# print(type(b))
# ------------------------------------------------------------------------------------
# student= ("riya","22","chh sambhaji nagar")
# name,age,city=student
# print(name)
# print(city)
# ------------------------------------------------------------------------------------
# t=(1,2,2,3,2)
# print(t.count(2))
# print(t.index(3))
# ------------------------------------------------------------------------------------
# student={
#     "name":"riya",
#     "age":22,
#     "city":"chh sambhaji nagar"
# }
# print(student)
# print(student.get("age"))
# print(student.get("phone"))
# print(student.get("phone","NA"))
# ----------------------------------------------------------------------------------------------
# d={"a": 1, "b": 2, "c": 3}

# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))
# -----------------------------------------------------------------------------------------------
# marks={"math":80,"science": 92}
# for subject,score in marks.items():
#     print(f"{subject}: {score}")
# ---------------------------------------------------------------------------------------------
# word_list=["ai","py","ai","ai","py"]
# count={}
# for w in word_list:
#     count[w]=count.get(w,0) + 1
# print(count)
# -----------------------------------------------------------
# student={
#     "AI": {"name":"riya","marks":85},
#     "A2":{"name":"ajay","marks":65}

# }
# print(student["AI"]["name"])
# ---------------------------------------------------------------------------------------------------------
# SETS
# nums={1,2,3,3,3,2,2,}
# print(nums)

# empty=set()
# -----------------------------------------------------------------------------------------------------
# s={1,2,3}
# s.add(4)
# s.remove(2)
# s.discard(10)
# print(s)
# ----------------------------------------------------------------------------------------------------
# set operation
# a=int(input("Enter First"))
# b=int(input("Enter second values"))

# print(a |b)
# print(a&b)
# print(a-b)
# print(a^b)
# ----------------------------------------------------------------------------------------------------
# data=[5,1,5,2,1,3]
# unique=list(set(data))
# print(len(unique))
# ------------------------------------------------------------------------------------------------------
# type  |  brackets  | ordered  |  changeable  | duplicates
# list  |  []        |  Yes     |  Yes         | Allowed
# tuple |  ()        | Yes      |  NO          | Allowed
# dict  |  {k:v}     | Yes      |  Yes         | Keys Unique
# set   |  {}        | NO       |  Yes         | Not Allowed
# ------------------------------------------------------------------------------------------------
# files

# with open("notes.txt","w") as f:
#     f.write("Hello Python\n")
#     f.write("files hamdling is easy\n")
# ---------------------------------------------------------------------------------------------
# with open("notes.txt","r") as f:
#     content = f.read()
# print(content)
# -------------------------------------------------------------------------------------------------
# with open("notes.txt") as f:
#     for line in f:
#         print(line.strip())
# with open("notes.txt") as f:
#     lines=f.readlines()
# print(len(lines))
# ----------------------------------------------------------------------------------------------
# try:
#     with open("books.txt") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("file not found")
# -------------------------------------------------------------------------------------------------
# names=str(input("enter whatever You want:"))
# with open("notes.txt","w") as f:
#     for n in names:
#         f.write(n+"\n")
# ------------------------------------------------------------------------------------------------
# 1 question solution:

# numbers = [12, 5, 8, 20, 3]

# print("List:", numbers)
# print("Sum:", sum(numbers))
# print("Largest:", max(numbers))
# print("Smallest:", min(numbers))
# print("Average:", sum(numbers) / len(numbers))
# --------------------------------------------------------------------------------------------------
# 2 Question solution:

# numbers = [12, 5, 8, 20, 3]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print("Even numbers:", even_numbers)
# ------------------------------------------------------------------------------------------------
# 3 Question solution:

# reverse=[1,3,4,6,9,3]
# reverse.reverse()
# print("Reversed list:", reverse)
# slice=reverse[::-1]
# print("Sliced list:", slice)
# loop=[]
# for i in range(len(reverse)-1,-1,-1):
#     loop.append(reverse[i])
# print("Looped list:", loop)
# ------------------------------------------------------------------------------------------------
# 4 Question solution:

# duplicate_list = [1, 2, 3, 2, 4, 1, 5]
# unique_list = list(set(duplicate_list))
# print("Unique list:", unique_list)
# ------------------------------------------------------------------------------------------------
# 5 Question solution:
 
# swap first and last elements of a list
# list = [1, 2, 3, 4, 5]
# list[0], list[-1] = list[-1], list[0]
# print("Swapped list:", list)
# ------------------------------------------------------------------------------------------------
# 6 Question solution:

# dictionary = {
#     "name": "John",
#     "marks": 95,
#     "name": "Alice",
#     "marks": 88
#     "name": "Bob",
#     "marks": 92
# }
# print("Dictionary:", dictionary)
# ------------------------------------------------------------------------------------------------
#  7 Question solution:

# elements1 = [1, 2, 3, 4, 5]
# elements2 = [5, 7, 8, 9, 10]
# common_elements = list(set(elements1) & set(elements2))
# print("Common elements:", common_elements)
# ------------------------------------------------------------------------------------------------
# 8 Question solution:

# write5 names in a file and read and print them with line numbers
# names = ["Alice", "Bob", "Charlie", "David", "Eve"]   
# with open("names.txt", "w") as f:
#     for i, name in enumerate(names, start=1):
#         f.write(f"{i}. {name}\n")
# with open("names.txt", "r") as f:
#     for line in f:
#         print(line.strip())
# ------------------------------------------------------------------------------------------------ 