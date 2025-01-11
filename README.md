# nomi-ceu-zh_cn

基于[nomi-ceu](https://github.com/Nomi-CEu/Nomi-CEu) / [Nomifactory (GTCEu Port)](https://www.curseforge.com/minecraft/modpacks/nomi-ceu) 官方语言包修改的汉化，遵循 LGPL-3.0 license 取得许可。

该仓库任务书 1.6 之前汉化来自 IAmNotGEM，因上游仓库打包方式不同且未接收 pull requests，故建立此复刻仓库。

~~鉴于官方翻译已经非常完善，你现在可以使用[官方构建的语言包](https://nightly.link/Nomi-CEu/Nomi-CEu-Translations/workflows/pushbuildpack/main?preview)，请注意，由于该语言包是实时更新的，可能与整合包版本不完全兼容。你也可以选择在本仓库下载适配特定整合包版本的语言包。本仓库的语言包已根据 LGPL-3.0 许可证修改，以更好地满足中国玩家的需求。~~

**本仓库继续维护的可能性不大，但本人仍会不时通过官方渠道提交翻译，若要下载官方语言包请前往[这里](https://nightly.link/Nomi-CEu/Nomi-CEu-Translations/workflows/pushbuildpack/main?preview)。**

语言包的建立与维护有赖于整合包作者和译者们的共同努力，你可以在[这里](https://weblate.pantsu.moe/user/?q=translates:zh_Hans%20contributes:nomi-ceu-translations)查看官方语言包中文部分的译者（使用 Weblate 作为翻译平台之后的）。

要贡献汉化，你可以在 [nomi-ceu discord 频道](https://discord.com/invite/zwQzqP8b6q) nomi-ceu-general 子频道的子区 NFu Translations 了解相关信息。

# 食用方法

1. 下载 [nomi-ceu](https://github.com/Nomi-CEu/Nomi-CEu/releases)（文件名为 nomi-ceu-[版本号]-client.zip）并安装。
2. 使用代理启动一次游戏或删除 serializationisbad 模组，以解决游戏因该模组部分文件无法下载导致的崩溃。
3. 下载[本汉化包](https://github.com/zero6six/nomi-ceu-zh_cn/releases)和[Minecraft 模组简体中文翻译项目资源包](https://cfpa.site/)。
4. 将这两个资源包置入 resourcepacks 文件夹并加载。 

# 仓库结构

```text
nomi-ceu-zh_cn
  ├─converter ------------ // 任务书语言文件转码成 ParaTranz json 文件以及回转
  ├─scripts -------------- // 硬编码文本修复脚本
  │ └─Zero6sixFix.zs------------- // 修复脚本（1.7-alpha-3 及之后版本中过时），置于 .minecraft/scripts 下
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
