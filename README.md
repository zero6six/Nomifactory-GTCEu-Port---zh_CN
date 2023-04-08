# Nomifactory-GTCEu-Port---zh_CN

基于[nomi-ceu](https://github.com/tracer4b/nomi-ceu) / [Nomifactory (GTCEu Port)](https://www.curseforge.com/minecraft/modpacks/nomi-ceu) 的深度汉化，汉化内容包括：

- 任务书
- 部分mod物品

# parse.sh

一个辅助查看语言文件的颜色效果的脚本

## 使用方法

```shell
sh parse.sh lang文件地址 开始的行数 结束的行数
```

例如查询 zh_cn.lang 1-100 行的效果

```shell
sh parse.sh zh_cn.lang 1 100
```

![img.png](mdresource/img.png)

---

由于上游仓库较长时间没有更新且未接受 pull requests，故本人 zero6six 移至该复刻仓库更新。

# nomi-ceu-zh_cn

该仓库内主要存储官方资源包形式的汉化资源，相关内容版权由对应作者所有，感谢每位贡献者对汉化做出的努力。

## converter.py

一个在 lang 文件与  json 文件间相互转换的 Python 脚本。该脚本内最后几行注释可按需更改。欢迎各位大佬改进该脚本。

## 汉化贡献

任务书 lang 文件已转换为 json 文件发布在 [crowdin](https://crowdin.com/project/nomi-ceu-zhcn) 上，欢迎各位前去贡献。