import os
import zipfile

# 本脚本大部分由 ChatGPT 提供。

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
            zip_file.write(file_path, os.path.relpath(file_path, workspace_path))

    # 添加 pack.mcmeta 文件到压缩包
    pack_mcmeta_path = os.path.join(workspace_path, "pack.mcmeta")
    zip_file.write(pack_mcmeta_path, "pack.mcmeta")

    # 关闭压缩包
    zip_file.close()

    print("资源包已创建：", os.path.join(output_path, output_name))

# 运行创建资源包的函数
create_resource_pack()
