# nomi-ceu-zh_cn

基于[nomi-ceu](https://github.com/Nomi-CEu/Nomi-CEu) / [Nomifactory (GTCEu Port)](https://www.curseforge.com/minecraft/modpacks/nomi-ceu) 的机翻润色汉化，汉化内容包括：

- 全部任务书
- 大部分整合包特色模组

该仓库任务书 1.6 之前汉化来自 IAmNotGEM，因上游仓库打包方式不同且未接收 pull requests，故建立此复刻仓库。

随着[官方语言仓库](https://github.com/Nomi-CEu/Nomi-CEu-Translations)的完善，本仓库将逐渐不在本仓库进行。官方仓库将会提供基于整合包版本的标准语言包和翻译更新一次上传一次的构建语言包。相关资源可在以下链接找到：[标准语言包](https://github.com/Nomi-CEu/Nomi-CEu/releases) 和[更新构建语言包](https://nightly.link/Nomi-CEu/Nomi-CEu-Translations/workflows/pushbuildpack/main?preview)。

要贡献汉化，你可以在 nomi-ceu discord 频道 nomi-ceu-general 子频道的子区 NFu Translations 了解相关信息。

# 食用方法

1. 下载 [nomi-ceu](https://github.com/Nomi-CEu/Nomi-CEu/releases)（文件名为 nomi-ceu-[版本号]-client.zip）并安装。
2. 使用代理启动一次游戏或删除 serializationisbad 模组，以解决游戏因该模组部分文件无法下载导致的崩溃。
3. 下载[本汉化包](https://github.com/zero6six/nomi-ceu-zh_cn/releases)和[Minecraft 模组简体中文翻译项目资源包](https://cfpa.site/)。
4. 将 [Zero6sixFix.zs](https://github.com/zero6six/nomi-ceu-zh_cn/tree/master/scripts/Zero6sixFix.zs) 下载并放入 .minecraft/scripts 路径以修复被硬编码的文本。
5. 将这两个资源包置入 resourcepacks 文件夹并加载。 

# 仓库结构

```text
nomi-ceu-zh_cn
  ├─assets --------------- // 打包前的汉化文件及原文
  ├─converter ------------ // 任务书语言文件转码成 ParaTranz json 文件以及回转
  ├─scripts -------------- // 硬编码文本修复脚本
  │ └─Zero6sixFix.zs------------- // 修复脚本，置于 .minecraft/scripts 下
  ├─.gitignore ----------- // git 忽略文件
  ├─pack.mcmeta ---------- // 资源包自述文件
  ├─pack.png ------------- // 资源包图片
  ├─packer.py ------------ // 打包脚本
  └─README.md ------------ // 自述文件
```

# 整合包版本升级方法

1. 复制 `minecraft/saves`
2. 复制 `minecraft/journeymap`
3. 复制 `minecraft/hei_bookmarks.ini` （HEI 书签）
4. 复制 `minecraft/config/simplyjetpacks` 目录和 `simplyjetpacks.cfg` （喷气背包相关设置，比如 HUD）
5. 确认 `minecraft/options.txt` 中的键位等信息正常。
6. 进行 [食用方法](#食用方法)
7. 使用 `/bq_admin default load` 将存档内任务同步成整合包任务。
