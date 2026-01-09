# 类、对象（属性，是对象的特征）、方法；创建对象叫做实例化  示例代码
# 1. 定义类（用class关键字，类名首字母大写）
class Student:
    def __init__(self,name,student_id):# 为什么需要在两边加两个_?
        # 初始化方法（__init__）：创建对象时自动执行，给对象赋值属性
        self.name = name # self是什么意思？
        self.student_id = student_id

    # 定义方法（就是类里的函数，第一个参数必须是self）。为什么第一个参数必须是self？
    def study(self,course):
        print(f"{self.name}，学号：{self.student_id}，正在学习{course}")

# 2. 创建对象（实例化）：类名(参数)
stu1 = Student("张三",2023001)
stu2 = Student("李四",2023002)

# 3. 访问属性、调用方法
print(stu1.name)
stu2.study("python")

print("====================================================")
# 贴合AI学习场景的示例代码
class LLM:
    def __init__(self,model_name,temperature):
        self.model_name = model_name # 模型名
        self.temperature = temperature # 随机性参数 temperature是什么意思？

    def generate(self,prompt):
        print(f"使用{self.model_name}模型（temperature={self.temperature}）生成回复：{prompt}->生成内容")

gpt3 = LLM("GPT-3,5",0.7)
gpt3.generate("什么是AI应用开发")

print("=====================================================")
print("practice-1:")
class StudyRecord:
    def __init__(self,date,content):
        self.date = date
        self.content = content

    def show_record(self):
        print(f"日期：{self.date}，学习内容：{self.content}")

    def calculate_hours(self, minutes):
        hours = minutes / 60
        print(f"当天学习时长：{hours}小时")


record1 = StudyRecord("2026-01-07","python文件操作＋git分支合并")
record1.show_record()

print("practice-2:")
record1.calculate_hours(150)
















