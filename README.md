# Pynput Auto Clicker

基于 [`pynput`](https://pypi.org/project/pynput/) 的 Windows 前台物理键鼠模拟自动化脚本。

## 功能特性

* 🖱️ 模拟鼠标左键点击，间隔 **1 秒**
* 🖱️ 模拟鼠标右键点击，间隔 **1 秒**
* ⌨️ 模拟空格键按下，间隔 **2 秒**
* 🛑 **全局安全退出**：任何时候按下 `F12` 键即可安全终止脚本

## 使用方法

### 1. 安装依赖

```bash
pip install pynput
```

### 2. 以管理员身份运行

以**管理员身份**打开 Windows 终端或 IDE。

### 3. 运行脚本

```bash
python main.py
```

### 4. 安全退出

脚本运行期间，按下：

```text
F12
```

即可立即终止脚本。

## 运行环境

* **操作系统：** Windows
* **Python：** 3.x
* **主要依赖：** pynput
