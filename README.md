# donkeyOCR - 中文OCR软件
> 用pyside6和python3.9写的中文OCR软件
> Chinese OCR software using PySide6 and Python3.9pp

## 界面(UI)
![donkeyOCR](https://raw.githubusercontent.com/loresding/images/main/donkeyOCR-example.png)

可以通过`截图`、`上传图片`、`上传PDF`来上传图片进行OCR识别

## 贡献者(DONATE)
> 项目界面灵感来自于**PyDarcula**🔗 https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6

> 中文OCR模型来自于**CnOCR**🔗 https://github.com/breezedeus/cnocr

## 安装包下载(installer)

**百度网盘**🔗 https://pan.baidu.com/s/1icyQpq5_06JaovZqAQebfQ 

**提取码**：8t7r 

## 使用方法
解压后直接运行**donkeyOCR.exe**

## 运行或本地调试(Running or local debugging)
> 使用**pyton3.9**并安装相关依赖
```console
pip install -r requirements.txt
```

> **Linux and Windows**:
```console
python main.py
```

## 项目内文件说明(instruction from PyDarcula)

> **main.py**: application initialization file.

> **main.ui**: Qt Designer project.

> **resouces.qrc**: Qt Designer resoucers, add here your resources using Qt Designer. Use version 6 >

> **setup.py**: cx-Freeze setup to compile your application (configured for Windows).

> **themes/**: add here your themes (.qss).

> **modules/**: module for running PyDracula GUI.

> **modules/app_funtions.py**: add your application's functions here.
Up
> **modules/app_settings.py**: global variables to configure user interface.

> **modules/resources_rc.py**: "resource.qrc" file compiled for python using the command: ```pyside6-rcc resources.qrc -o resources_rc.py```.

> **modules/ui_functions.py**: add here only functions related to the user interface / GUI.

> **modules/ui_main.py**: file related to the user interface exported by Qt Designer. You can compile it manually using the command: ```pyside6-uic main.ui> ui_main.py ```.
After expoting in .py and change the line "import resources_rc" to "from. Resoucers_rc import *" to use as a module.

> **images/**: put all your images and icons here before converting to Python (resources_re.py) ```pyside6-rcc resources.qrc -o resources_rc.py```.