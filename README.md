# nomi-ceu-zh_cn

基于[nomi-ceu](https://github.com/Nomi-CEu/Nomi-CEu) / [Nomifactory (GTCEu Port)](https://www.curseforge.com/minecraft/modpacks/nomi-ceu) 的机翻润色汉化，汉化内容包括：

- 全部任务书
- 大部分整合包特色模组

该仓库任务书 1.6 之前汉化来自 IAmNotGEM，因上游仓库打包方式不同且未接收 pull requests，故建立此复刻仓库。

随着[官方语言仓库](https://github.com/Nomi-CEu/Nomi-CEu-Translations)的完善，我们将不再保存所有模组的语言文件。**但您仍可使用我们按版本发布的汉化包**。此外，我们提供官方仓库未包含的资源，如双语任务书和特定版本物品的汉化脚本。官方仓库则提供基于整合包版本的标准语言包和翻译更新一次上传一次的构建语言包。相关资源可在以下链接找到：[标准语言包](https://github.com/Nomi-CEu/Nomi-CEu/releases) 和[更新构建语言包](https://nightly.link/Nomi-CEu/Nomi-CEu-Translations/workflows/pushbuildpack/main?preview)。

要贡献汉化，你可以直接向本仓库提交 Pull Request 或在 [ParaTranz](https://paratranz.cn/projects/8990) 为任务书翻译做出贡献。

# 食用方法

1. 下载 [nomi-ceu](https://github.com/Nomi-CEu/Nomi-CEu/releases) 并安装。
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

# 翻译内容对照总结

以下内容为翻译任务的总结与备忘。

下列未打钩的为需要持续监控并进行更新的。

- [x] appliedenergistics2 | 模组文件自带汉化，存在极少部分汉化不全
- [ ] contenttweaker
- [x] deepmoblearning | 个人完成该模组汉化，该模组仓库汉化 issue 暂未回应
- [x] gregtech
- [ ] modpack
- [ ] multiblocktweaker
- [ ] questbook
- [x] toolbelt | [Minecraft 模组简体中文翻译项目](https://cfpa.site/)已翻译

下列文件是为了重命名物品而设置的（有的重命名就离谱）。

- actuallyadditions | 铁制外壳 -> 铝制外壳
- advancedrocketry
    - Fueling **s**tation -> Fueling **S**tation
    - 透镜 -> 轨道镭射钻透镜
- armorplus | 煤炭胸甲 -> 碳板胸甲
- cns | 下界之星碎片 -> 下界之星北角，契合 CoT 添加的下界之星东南西角
- armorplus | 煤炭胸甲 -> 碳板胸甲
- ~~draconicevolution | DE 龙块和觉醒龙锭/块早已被 GTCEu 的对应物取代，故移除。~~
- enderio
     - 修改一系列导管名字以契合合成材料
     - Dark Helm -> Dark Steel Helmet
- extendedcrafting
     - 终极奇点 -> 万象之尘等等
     - Ender Star -> End**est** Star
- gcym | 搅拌机外壳 -> 反应安全外壳
- nuclearcraft | Thorium-232 -> **Prepared** Thorium-232
- simplyjetpacks | 铁护甲板 -> 锻铁护甲板
- thermalexpansion
     - 将热力能量框架改为采掘机合成材料
     - Machine Casing -> Thermal Machine Casing
- thermalfoundation | 修改英语蕴魔秘银粉