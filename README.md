# nomi-ceu-zh_cn

基于[nomi-ceu](https://github.com/tracer4b/nomi-ceu) / [Nomifactory (GTCEu Port)](https://www.curseforge.com/minecraft/modpacks/nomi-ceu) 的深度汉化，汉化内容包括：

- 任务书
- 部分mod物品

该仓库 1.6 之前汉化来自 IAmNotGEM，因上游仓库打包方式不同且未接收 pull requests，故建立此复刻仓库。

# 仓库内脚本文件

## ~~parse.sh~~

~~一个辅助查看语言文件的颜色效果的脚本~~

名为 Minecraft .lang Colorizer 的 VSCode 拓展实现了这一功能。

## converter.py

使用 converter 目录下 result.json 的键值对替换 lang_file.lang 的键值对并生成 lang_file_updated.lang。

将 lang 文件转换为 result.json 可以在[此处](https://tt.nptr.cc)进行。

## packer.py

自动把当前目录下的 assets 文件夹与 pack.mcmeta 打包成 temp 目录下的压缩包。

## mergy.py

将任务书英文 lang 文件中所有 nomifactory.quest.db.xxx.desc 的值追加在中文 lang 文件内，实现双语任务但保证原语言文件纯净。

# 汉化贡献

任务书 lang 文件已转换为 json 文件发布在 [crowdin](https://crowdin.com/project/nomi-ceu-zhcn) 上，欢迎各位前去贡献。