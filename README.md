### 2026.1.6

一、今日 Python+Git 核心操作极简清单

Python 部分（变量 / 数据类型）

变量定义：变量名 = 内容（如name = "许子澄"）

核心数据类型：int（整数）、float（浮点数）、str（字符串）、bool（布尔值）

类型操作：

查看类型：type(变量名)

类型转换：str(变量)（转字符串）、float(变量)（转浮点数）

输出方式：

字符串拼接："内容" + 变量

f-string（简洁版）：f"内容{变量}"

Git 部分（仓库创建）

配置用户信息（仅需 1 次）：

git config --global user.name "你的GitHub用户名"

git config --global user.email "你的GitHub邮箱"

创建仓库：

mkdir AI-Learning（创建文件夹）

cd AI-Learning（进入文件夹）

git init（初始化 Git 仓库）

验证仓库：git status（显示 “On branch main” 即成功）

二、今日知识点复盘

Python 变量是存储数据的 “标签”，命名需遵守 “字母 / 数字 / 下划线” 规则，核心数据类型可通过type()查看、通过str()/float()转换；

Git 仓库是被 Git 管理的代码文件夹，创建需先配置用户信息，再初始化文件夹；

代码文件可直接放入 Git 仓库文件夹，后续 Git 会记录这些文件的修改。

