# 幻影坦克图片生成器
Mirage-Tank 是一个由 python 编写的命令行工具。使用它可以轻松地制作“幻影坦克”图片。

## 什么是幻影坦克？
幻影坦克是早年流行在互联网上的一种双层图片，这种图片分为内外两层，在未点击的情况下是一张图片，点击打开后又是一张图片，隐蔽性很好。~~常常用来涩涩。~~

## 准备
- 本工具及本工具运行所需的环境
- 一张图片作为表层
- 一张图片作为底层
- 一台可以运行 python 脚本的计算机

## 开始
1. 首先你需要先把该项目下载下来，这是当然的

2. 假设你的表层图片名叫`top.png`，底层图片名叫`bottom.png`。

   在一般情况下，表层图片在成品**未点开**时显示，底层图片在成品**点开后**显示。

3. 打开你电脑系统的命令行
   1. Windows：使用快捷键`win+R`打开`运行`窗口，在`运行`窗口内输入`cmd`后点击确定。

4. 确保你的计算机中有 python 环境
   1. 检查方式: 在命令行中输入`python --version`，按下回车执行，检查是否正确输出python版本，例如：

      ```shell
      (default) C:\Windows\system32>python --version
      Python 3.10.4
      ```

5. 找到你表层图片和底层图片所在的路径

   1. 例如你的`top.png`文件在`D`盘的`picture`文件夹中的`tmp`文件夹中，你的`top.png`文件路径就是：

      ```shell
      D:\picture\tmp\top.png
      ```

      但鉴于转义这个麻烦的问题，你最好这样表示你的路径：

      ```shell
      D:/picture/tmp/top.png
      ```

6. 找到你下载该项目的路径，并且在命令行中进入它

   1. 假设你把该项目下载到了`D:\mirage`，则你需要在命令行中输入：

      ```shell
      cd /d "D:/mirage"
      ```

      按回车提交后，你会看到命令行中新的一行开头有所变化——它变成了你刚刚输入的路径：

      ```shell
      C:\Users\Kl1nge5>cd /d "D:/mirage"
      
      D:\mirage>
      ```

7. 鼓励一下自己，虽然上面的步骤很复杂，很困难，很麻烦，但是就快大功告成了

8. 假设现在你的表层图片路径为`D:/top.png`，底层图片路径为`D:/bottom.png`，你想把最终生成的幻影坦克保存在`D:/out.png`。你只需要在命令行中输入：

   ```shell
   python mirage.py -t "D:/top.png" -b "D:/top.png" -o "D:/out.png"
   ```

   按下回车提交后，等待片刻，看到`生成成功!`的提示后，即可去收获你的成果了。

## 示例

本仓库还贴心地准备了示例。

1. 下载该仓库

2. 打开命令行来到下载地址

3. 输入：

   ```shell
   python mirage.py -t "example/top.png" -b "example/bottom.png" -o "example/out.png"
   ```

4. 稍等片刻，等待完成提示。

5. 进入`example`文件夹，用浏览器打开`test.html`网页，即可查看成品效果。

## 更多

通过`-s`参数可以使程序不打印控制台信息，静默处理。

例如：

```shell
python mirage.py -t "example/top.png" -b "example/bottom.png" -o "example/out.png" -s
```

## Q&A

Q：幻影坦克的原理是什么？

A：请自行百度。

Q：为什么教程这么啰嗦？

A：这样能显得 README 很长😇

Q：为什么我把图片发出去后就没有效果了？

A：请勾选原图发送，接收方也需要下载原图。

Q：为什么我的程序报错了？

A：请检查文件路径是否正确输入。

Q：为什么处理速度这么慢？

A：可能这就是python吧。
