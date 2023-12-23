import os
import zipfile

# 本脚本大部分由 ChatGPT 提供。

def merge_lang_files():
    import re
    pattern = r'nomifactory\.quest\.(expert|normal)\.db\.\d+\.desc='
    
    # 读取file1
    with open('assets//questbook//lang//en_us.lang', 'r', encoding='utf-8') as f1:
        lang1 = f1.readlines()

    # 读取file2
    with open('assets//questbook//lang//zh_cn.lang', 'r', encoding='utf-8') as f2:
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
                    value1 = line1.split('=', 1)[1].strip()

                    # 在值之前添加%n%n%n%n
                    new_value = '§r%n%n%n%n' + value1

                    # 追加到file2的对应键的值之前
                    line2 = line2.rstrip('\n') + new_value + '\n'

                    # 结束内部循环
                    break

        # 将处理后的行添加到新lang文件中
        new_lang.append(line2)

    # 将新lang文件保存为新文件
    new_file = 'output//tempQB.lang'
    with open(new_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lang)

def create_resource_pack():
    # 当前工作目录路径
    workspace_path = os.getcwd()

    # 压缩包保存路径和名称
    output_path = "output//"
    output_name = input("请输入资源包文件名(带.zip) ")

    # 创建一个新的 ZIP 文件
    zip_file = zipfile.ZipFile(os.path.join(output_path, output_name), "w", zipfile.ZIP_DEFLATED)

    # 添加 assets 文件夹到压缩包
    assets_path = os.path.join(workspace_path, "assets")
    for root, _, files in os.walk(assets_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(r"questbook\lang\zh_cn.lang") and whetherBilingual:
                merge_lang_files()
                zip_file.write('output//tempQB.lang', os.path.relpath(file_path, workspace_path))
                os.remove('output//tempQB.lang')
            else:
                zip_file.write(file_path, os.path.relpath(file_path, workspace_path))

    # 添加 pack.mcmeta 文件到压缩包
    pack_mcmeta_path = os.path.join(workspace_path, "pack.mcmeta")
    zip_file.write(pack_mcmeta_path, "pack.mcmeta")

    # 添加 pack.png 文件到压缩包
    pack_mcmeta_path = os.path.join(workspace_path, "pack.png")
    zip_file.write(pack_mcmeta_path, "pack.png")

    # 关闭压缩包
    zip_file.close()

    print("资源包已创建：", os.path.join(output_path, output_name))

whetherBilingual = True
# 运行创建资源包的函数
create_resource_pack()
