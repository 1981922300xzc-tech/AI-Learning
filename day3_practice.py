def filter_pass_score(scores):
#这样命名是因为函数名英语意思是筛选数字吗
    pass_list = []
    for score in scores:
        if score > 60:
            pass_list.append(score)
        return pass_list

# 调用两次，处理不同列表
math_scores = [55, 78, 90, 45, 88]
english_scores = [66, 50, 72]
print(filter_pass_score(math_scores))  # [78,90,88]
print(filter_pass_score(english_scores))

print("==================================================")
print("practice-1:")
def print_study_plan():
    print("1.学Python函数")
    print("2.练Git分支")
    print("3.整理笔记")
# 这里如果写成1行，Python代码里怎么换行？

print_study_plan()

print("==================================================")
print("practice-2:")

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

a = factorial(5)
b = factorial(3)
print(f"5的阶乘是{a}，3的阶乘是{b}。")








