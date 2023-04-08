def lang_to_json() -> None:
    lang_file = open(lang_file_path, 'r')
    json_file = open(json_file_path, 'w')
    note_number = 0

    json_file.write('{\n')

    for i in lang_file:
        i = i.replace('"', r'\"')
        if i.startswith('#') or i == '\n':
            note_number+=1
            json_file.write(rf'    "//{note_number}":"'+i.rstrip()+'",\n')
        else:
            text = i.rstrip().split('=')
            json_file.write(f'    "{text[0]}":"{text[1]}",\n')

    lang_file.close()
    json_file.close()

    # 截断最后一个多余的","，使用"a+b"参数在末尾二进制方式追加打开并向前移动 3 个字节(b',\r\n')，截断后补上"b'\r\n}'"。
    with open(json_file_path, 'a+b') as file:
        file.seek(-3,1)
        file.truncate()
        file.write(b'\r\n}')

def json_to_lang() -> None:
    json_file = open(json_file_path, 'r')
    lang_file = open(lang_file_path, 'w')

    for i in json_file:
        i = i.rstrip()
        if i.startswith(('{','}')):
            continue
        elif i.startswith(r'    "//'):
            colon_index=i.find(':')
            lang_file.write(i[colon_index+3:-2]+'\n')
        else:
            colon_index=i.find(':')
            lang_file.write(i[5:colon_index-1]+'='+i[colon_index+3:-2]+'\n')

# lang_file_path = r"C:\Users\zero6six\Desktop\en_us.lang"
# json_file_path = r"C:\Users\zero6six\Desktop\en_us.json"

# lang_file_path = r"C:\Users\zero6six\Desktop\zh_cn.lang"
# json_file_path = r"C:\Users\zero6six\Desktop\zh_cn.json"

# json_to_lang()
# lang_to_json()