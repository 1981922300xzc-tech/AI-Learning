# 模块 1：列表 (list) 进阶高频操作（重中之重，实战第一高频）
# list.sort()
scores = [85,92,78,90,66]
scores.sort()  # 应该是内置库函数，升序排序
print(scores)
scores.sort(reverse=True)
print(scores)

# sorted(list)
scores = [85,92,78,90,66]
new_scores = sorted(scores) # 生成一个新列表，并排好序，不修改原来的列表
print(scores)
print(new_scores)

# list.index(值)
names = ["Python","Git","AI","Python"]
print(names.index("AI"))

# list.count(值)
print(names.count("Python"))

# list.extend(列表) 把另一个列表的「所有元素」追加到当前列表末尾
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

# 列表推导式，用一行代码，完成「遍历列表 + 条件筛选 + 生成新列表」，替代繁琐的 for+if，循环实战中 90% 的列表处理都用这个！
# 基础语法：新列表 = [要保留的内容 for 变量 in 原列表 if 筛选条件]
scores = [85,59,92,78,55,90]
pass_scores = [s for s in scores if s > 60]
print(pass_scores)

new_scores = [s+5 for s in scores if s > 60]
# 先挑选出符合的s 然后再做 最前面的s+5
print(new_scores)

print("=======================================================")
# 模块 2：字典 (dict) 进阶高频操作（实战第二高频，存键值对数据必用）
# dict.keys() 提取字典中「所有的键」，返回可遍历的列表
student = {"name":"张三","score":90,"course":"Python"}
print(student.keys()) # 输出：dict_keys(['name', 'score', 'course'])

# dict.values() 提取字典中「所有的值」，返回可遍历的列表
print(student.values())

# dict.items()
print(student.items())
for k,v in student.items():
    print(f"键：{k}，值：{v}")

# dict.get(键，默认值) 根据键取值，如果键不存在，返回「默认值」
student = {"name":"张三","score":90}
# print(student["course"])  # 报错：KeyError（键不存在）
print(student.get("course"))
print(student.get("course", "未选课"))  # 不报错，输出：未选课

# 字典推导式（一行生成字典，进阶用法）
# 语法：新字典 = {新键:新值 for k,v in 原字典.items() if 筛选条件}
student = {"name":"张三","math":85,"english":78,"python":92}
good_score = {k:v for k,v in student.items() if isinstance(v,int) and v>80 }






print("=======================================================")
print("practice-1")

scores = [75, 88, 92, 63, 55, 88, 95, 79, 66]
total_score = sum(scores)
average_score = total_score / len(scores)
max_score = max(scores)
min_score = min(scores)
print(f"总分为{total_score}，平均分为{average_score}，最高分为{max_score}，最低分为{min_score}")

new_scores = [s for s in scores if s>60 ]
print(f"及格的分数有{new_scores}")

new_scores.sort(reverse=True)
print(f"降序排序：{new_scores}")

print(f"分数88出现的次数为{scores.count(88)}")


print("=======================================================")
print("practice-2")

stu_info = {"name":"李四","math":82,"english":90,"python":78,"age":20}
print(stu_info.items())

for k,v in stu_info.items():
    if k != "name" and k != "age":
        print(f"科目：{k}，分数：{v}")

print(stu_info.get("chinese","未考"))

good_score = {k:v for k,v in stu_info.items() if isinstance(v,int) and v>80 }
print(good_score) # good_score.items() 是可迭代对象，直接打印即可，不用 .items()
















