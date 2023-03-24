"""
核心功能函数集合,包括pdf文件获取图片、ocr函数
作者: LoresDing
时间: 2023/03/21
"""
import os
import re
import fitz
import shutil
from cnocr import CnOcr

def chinese_ocr(path, model_name, root):
    """
    利用cnocr从图片识别文字
    """
    ocr = CnOcr(model_name=model_name, root=root)
    filenames = sorted(os.listdir(path))
    for index, filename in enumerate(filenames):
        image_path = os.path.join(path, filename)
        lines = ocr.ocr(image_path)
        lines = "\n".join([line[0] for line in lines])
        yield index, lines
 

def get_images_from_pdf(path, save_path):
    """
    从pdf获取图片
    """
    # 删除现有的图片
    shutil.rmtree(save_path)
    os.makedirs(save_path)
    #使用正则表达式来查找图片
    re_xobject = r"/Type(?= */XObject)"
    re_image = r"/Subtype(?= */Image)"
    #打开pdf
    doc = fitz.open(path)
    #图片计数
    count = 0
    xref_length = doc.xref_length()

    #遍历每一个对象
    for i in range(1, xref_length):
        #定义对象字符串
        text = doc.xref_object(i)
        is_xobject = re.search(re_xobject, text)
        #使用正则表达式查看是否是图片
        is_image = re.search(re_image, text)
        #如果不是对象也不是图片，则continue
        if not is_xobject or not is_image: continue
        count += 1
        #根据索引生成图像
        pix = fitz.Pixmap(doc, i)
        #根据pdf的路径生成图片的名称
        new_name = "img{}.png".format(count)

        #如果pix.n<5，可以直接存为png
        if pix.n < 5:
            pix.save(os.path.join(save_path, new_name))
        #否则先转换CMYK
        else:
            pix0 = fitz.Pixmap(fitz.csRGB,pix)
            pix0.save(os.path.join(save_path, new_name))
            pix0 = None
        #释放资源
        pix = None