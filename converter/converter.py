# 本脚本大部分由 ChatGPT 提供。
# lang 转 result.json 可在 https://tt.nptr.cc 进行

import json

# 读取 JSON 文件
with open('converter//result.json', 'r', encoding='utf-8') as json_file:
    translations = json.load(json_file)

# 读取 .lang 文件
with open('converter//lang_file.lang', 'r', encoding='utf-8') as lang_file:
    lines = lang_file.readlines()

# 替换键值对
for i in range(len(lines)):
    line = lines[i]
    if '=' in line:
        key, value = line.split('=', 1)
        key = key.strip()
        if key in translations:
            # 使用 JSON 文件中的值替换 .lang 文件中的值
            # [:-1]作用是除去末尾的\r
            value = translations[key][:-1]
            lines[i] = f'{key}={value}\n'

# 写入更新后的 .lang 文件
with open('converter//lang_file_updated.lang', 'w', encoding='utf-8') as updated_lang_file:
    updated_lang_file.writelines(lines)
