@REM pyinstaller -D -n donkeyOCR -i donkeywork.png .\main.py
pyinstaller  -D  -n donkeyOCR -i .\app\donkey.png --noconsole .\app\main.py

@REM cnocr模型文件和label文件
xcopy .\app\core\models dist\donkeyOCR\app\core\models /s/e/i/y

@REM 拷贝platform文件
xcopy .\app\platforms dist\donkeyOCR\platforms /s/e/i/y 

md .\dist\donkeyOCR\cnocr
copy .\app\core\models\label_cn.txt .\dist\donkeyOCR\cnocr\label_cn.txt

@REM 拷贝安装文件
copy install.bat dist\donkeyOCR