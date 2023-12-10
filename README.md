# nomi-ceu-zh_cn

基于[nomi-ceu](https://github.com/Nomi-CEu/Nomi-CEu) / [Nomifactory (GTCEu Port)](https://www.curseforge.com/minecraft/modpacks/nomi-ceu) 的机翻润色汉化，汉化内容包括：

- 普通版任务书（暂无专家版任务书汉化计划）
- 大部分整合包特色模组
- GTCEu 最新翻译（来自 https://paratranz.cn/projects/7760，依照CC BY-NC 4.0取得授权。）

该仓库任务书 1.6 之前汉化来自 IAmNotGEM，因上游仓库打包方式不同且未接收 pull requests，故建立此复刻仓库。

融合了 nomi-ceu 仓库最新发布的语言包，并向官方仓库提交 PR 被通过。

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
  ├─converter ------------ // 一个 lang 和 json 之间的互转脚本，没啥大用
  ├─merge ---------------- // 双语合并脚本及原始任务书汉化文件
  │ ├─merge.py ------------------ // 双语合并脚本
  │ └─original_zh_cn.lang ------- // 原始任务书汉化文件
  ├─scripts -------------- // 硬编码文本修复脚本
  │ └─Zero6sixFix.zs------------- // 修复脚本，置于 .minecraft/scripts 下
  ├─.gitignore ----------- // git 忽略文件
  ├─README.md ------------ // 自述文件
  ├─pack.mcmeta ---------- // 资源包自述文件
  └─packer.py ------------ // 打包脚本
```

# 翻译内容对照总结

目前方针：语言包内 en_us.lang 保存一份用于比对更新，官库 resources 文件夹内多的不保存。

下列未打钩的为需要持续监控的。

- [x] appliedenergistics2 | 模组文件自带汉化，存在极少部分汉化不全
- [ ] contenttweaker
- [x] cns | CraftingNetherStar 该模组有关物品自带两个，其中一个被硬编码，作者 CoT 还写了仨类似的物品用于合成
- [x] deepmoblearning | 个人完成该模组汉化，该模组仓库汉化 issue 暂未回应
- [x] gregtech
- [x] minecraft | 无汉化任务
- [ ] modpack
- [ ] multiblocktweaker
- [x] nuclearcraft | 无汉化任务
- [ ] questbook
- [x] toolbelt | [Minecraft 模组简体中文翻译项目](https://cfpa.site/)已翻译