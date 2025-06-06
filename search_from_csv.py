import os
import csv

# === 第一步：读取 CSV 文件的第一列 ===
csv_path = 'standard.csv'  # 替换为你的实际文件名
lines_to_search = []

with open(csv_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row and row[0].strip():  # 确保第一列不为空
            lines_to_search.append(row[0].strip())

# === 第二步：递归查找所有 .py 文件 ===
all_py_files = []
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.py') and file != 'search_from_csv.py':
            all_py_files.append(os.path.join(root, file))

# === 第三步：搜索每一行内容是否出现在 .py 文件中 ===
for line in lines_to_search:
    print(f"\n🔍 正在查找内容：{line}")
    found = False
    for py_file in all_py_files:
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if line in content:
                    print(f"✅ 在文件中找到匹配：{py_file}")
                    found = True
        except Exception as e:
            print(f"⚠️ 无法读取文件 {py_file}：{e}")
    if not found:
        print("❌ 没有找到匹配内容。")
