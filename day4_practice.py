print("practice-1:")
file_path = r"D:\桌面\AI应用开发学习记录\Python\score_log.txt"
# 或者每个都写：path = "D:\\桌面\\AI应用开发学习记录\\Python\\score_log.txt"
# 打开文件
f = open(file_path,"w",encoding="utf-8")
# 写入、保存内容
f.write("数学：85\n英语：92.5")
f.close()

# 打开文件，读取、打印内容
f = open(file_path,"r",encoding="utf-8")
content = f.read()
print(content)
f.close()

print("============================================")
print("practice-2:")

with open(file_path,"a",encoding="utf-8") as f:
    f.write("\n平均分：88.75")

with open(file_path,"r", encoding="utf-8") as f:
    content = f.read()
    print(content)






