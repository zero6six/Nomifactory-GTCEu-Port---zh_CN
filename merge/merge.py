# 本脚本大部分由 ChatGPT 提供。第一个文件遍历一行，第二个文件遍历一遍，太烂了！But it works.

import re

pattern = r'nomifactory\.quest\.normal\.db\.\d+.desc='

def merge_lang_files(file1, file2):
    # 读取file1
    with open(file1, 'r', encoding='utf-8') as f1:
        lang1 = f1.readlines()

    # 读取file2
    with open(file2, 'r', encoding='utf-8') as f2:
        lang2 = f2.readlines()

    # 创建新的lang文件
    new_lang = []

    # 遍历file2的每一行
    # lang1 为英文 lang2 为中文
    for line2 in lang2:
        # 检查是否为目标键
        match = re.match(pattern, line2)
        if match:
            # 获取键名
            key = match.group()[:-1]

            # 遍历file1的每一行
            for line1 in lang1:
                # 检查是否为目标键
                if line1.startswith(key):
                    # 获取键值
                    value1 = line1.split('=')[1].strip()

                    # 在值之前添加%n%n%n%n
                    new_value = '§r%n%n%n%n' + value1

                    # 追加到file2的对应键的值之前
                    line2 = line2.rstrip('\n') + new_value + '\n'

                    # 结束内部循环
                    break

        # 将处理后的行添加到新lang文件中
        new_lang.append(line2)

    # 将新lang文件保存为新文件
    new_file = 'output//merge_zh_cn.lang'
    with open(new_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lang)

    print(f"合并完成，保存为 {new_file}")



# 调用函数进行合并
file1 = 'assets//questbook//lang//en_us.lang'
file2 = 'merge//original_zh_cn.lang'
merge_lang_files(file1, file2)
