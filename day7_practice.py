# 1.定义 StudyRecord 类
class StudyRecord:
    def __init__(self,date,content,minutes,score):
        self.date = date         # 日期
        self.content = content   # 学习内容
        self.minutes = minutes   # 时长（分钟）
        self.score = score       # 掌握程度（1-5星）

# 2.创建列表，存储多个学习记录对象
records = []
record1 = StudyRecord("2026-01-27","Python列表字典进阶",90,1)
records.append(record1)
record2 = StudyRecord("2026-01-28","Git分支管理",60,1)
records.append(record2)
record3 = StudyRecord("2026-01-26","Python面向对象",90,1)
records.append(record3)

# 3. 实现功能
# ① 筛选掌握程度≥4星的记录
high_score_records = [r for r in records if r.score >=4 ]
print("掌握程度≥4星的记录：")
for r in high_score_records:
    print(f"{r.date} | {r.content} | {r.score}")

# ② 计算总时长、平均时长
total_minutes = sum(r.minutes for r in records)
avg_minutes = total_minutes / len(records)
print(f"\n总学习时长：{total_minutes}分钟")
print(f"平均时长：{avg_minutes:.1f}分钟")

# ③ 保存到本地文件
file_path = r"D:\桌面\AI应用开发学习记录\Python\study_records.txt"
with open(file_path,"w",encoding="utf-8") as f:
    f.write("AI学习记录清单\n")
    f.write("===============================\n")
    for r in records:
        f.write(f"{r.date} | {r.content} | {r.minutes}分钟 | {r.score}星\n")
print("\n学习记录已保存到 study_records.txt")









