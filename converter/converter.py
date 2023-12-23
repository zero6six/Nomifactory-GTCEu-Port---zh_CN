import json
import re

pattern = r'nomifactory\.quest\.(expert|normal)\.(line|db)\.\d+\.(title|desc)='

def generate_ParaTranz_json():
    '''使用 en_us.lang 与 zh_cn.lang 生成 ParaTranz.json 丢进 output 文件夹'''
    ParaTranzDict = []

    with open(r'assets\questbook\lang\en_us.lang', 'r', encoding='utf-8') as en_file:
        en_lines = en_file.readlines()

    with open(r'assets\questbook\lang\zh_cn.lang', 'r', encoding='utf-8') as zh_file:
        zh_lines = zh_file.readlines()
    
    for en_line in en_lines:
        match = re.match(pattern, en_line)
        if match:
            key = match.group()[:-1]
            value = en_line.split('=', 1)[1].strip()
            ParaTranzDict.append(dict(key=key, original=value))
    
    tempDict = []
    for zh_line in zh_lines:
        match = re.match(pattern, zh_line)
        if match:
            key = match.group()[:-1]
            value = zh_line.split('=', 1)[1].strip()
            tempDict.append(dict(key=key, translation=value))
    
    # 将 tempDict 转化为键为 key 键值，值为中文翻译 str 的字典，以便于快速查找
    tempDict = {item["key"]: item["translation"] for item in tempDict}
    
    # 遍历 ParaTranzDict 并添加 translation
    for item in ParaTranzDict:
        key = item["key"]
        item["translation"] = tempDict.get(key, "")  # 如果 key不存在于 ParaTranzDict 中，则默认为空字符串
    
    # 写入更新后的 .lang 文件
    with open(r'output\ParaTranz.json', 'w', encoding='utf-8') as ParaTranzFile:
        json.dump(ParaTranzDict, ParaTranzFile, ensure_ascii=False, indent=4)

def update_zh_lang():
    '''使用 json 内容替换 en_us.lang 并生成 zh_cn.lang'''
    with open(r'output\ParaTranz.json', 'r', encoding='utf-8') as ParaTranzFile:
        ParaTranzDict = json.load(ParaTranzFile)

    tempDict = {item["key"]: item["translation"] for item in ParaTranzDict}

    with open(r'assets\questbook\lang\en_us.lang', 'r', encoding='utf-8') as en_file:
        en_lines = en_file.readlines()

    for index_en_line in range(len(en_lines)):
        match = re.match(pattern, en_lines[index_en_line])
        if match:
            key = match.group()[:-1]
            updated_translation = tempDict.get(key, "")  # 如果 key不存在于 ParaTranzDict 中，则默认为空字符串
            en_lines[index_en_line]=f"{key}={updated_translation}\n"
    
    with open(r'assets\questbook\lang\zh_cn.lang', 'w', encoding='utf-8') as zh_file:
        zh_file.writelines(en_lines)

# generate_ParaTranz_json()
update_zh_lang()