@REM pyinstaller -D -n donkeyOCR -i donkeywork.png .\main.py
pyinstaller  -D  -n donkeyOCR -i donkey.png --noconsole .\main.py

@REM cnocr模型文件和label文件
xcopy cnocr dist\donkeyOCR\cnocr /s/e/i/y

@REM 拷贝platform文件
xcopy platforms dist\donkeyOCR\platforms /s/e/i/y 

@REM 拷贝安装文件
copy install.bat dist\donkeyOCR