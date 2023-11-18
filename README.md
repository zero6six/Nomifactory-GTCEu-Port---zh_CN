# nomi-ceu-zh_cn

基于[nomi-ceu](https://github.com/Nomi-CEu/Nomi-CEu) / [Nomifactory (GTCEu Port)](https://www.curseforge.com/minecraft/modpacks/nomi-ceu) 的个人自用机翻润色汉化，汉化内容包括：

- 普通版任务书
- 官方语言包内的大部分模组
- GTCEu 最新翻译（来自 https://paratranz.cn/projects/7760，依照CC BY-NC 4.0取得授权。）

该仓库任务书 1.6 之前汉化来自 IAmNotGEM，因上游仓库打包方式不同且未接收 pull requests，故建立此复刻仓库。

融合了 nomi-ceu 仓库最新发布的语言包。

# 食用方法

1. 下载 [nomi-ceu](https://github.com/Nomi-CEu/Nomi-CEu/releases) 并安装。
2. 使用代理启动一次游戏或删除 serializationisbad 模组，以解决游戏因该模组部分文件无法下载导致的崩溃。
3. 下载[本汉化包](https://github.com/zero6six/nomi-ceu-zh_cn/releases)和[Minecraft 模组简体中文翻译项目资源包](https://cfpa.site/)。
4. 将这两个资源包置入 resourcepacks 文件夹并加载。 

# 仓库内脚本文件

## ~~parse.sh~~

~~一个辅助查看语言文件的颜色效果的脚本~~

名为 Minecraft .lang Colorizer 的 VSCode 拓展实现了这一功能。

## converter.py

使用 converter 目录下 result.json 的键值对替换 lang_file.lang 的键值对并生成 lang_file_updated.lang。

将 lang 文件转换为 result.json 可以在[此处](https://tt.nptr.cc)进行。

## packer.py

自动把当前目录下的 assets 文件夹与 pack.mcmeta 打包成 temp 目录下的压缩包。

## merge.py

将任务书英文 lang 文件中所有 nomifactory.quest.db.xxx.desc 的值追加在中文 lang 文件内，输出到 output 文件夹实现双语任务但保证原语言文件纯净。

# 经验分享

[Minecraft 模组简体中文翻译项目](https://cfpa.site/)已翻译的内容有：

- toolbelt | 工具皮带

模组文件自带汉化的有：

- AE2 Unofficial Extended Life | 应用能源非官方延续版(存在极少部分汉化不全)