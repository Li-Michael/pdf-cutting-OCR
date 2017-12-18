# -*- coding:utf-8 -*-
from wand.image import Image
from PIL import Image as PI
import PyPDF2
import PythonMagick
import pyocr
import pyocr.builders
import io
import sys

#改变Python的默认输出编码为utf-8，主要是因为win7系统不是默认编码，如果是macOS就不会有这样的问题
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#下面第一行，选择pyocr中的tesseract OCR
#第二行，选择languages列表中第二个，即eng
tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages()[1]

#存储图像和最终文本
#图像是因为pdf有很多页，会被切割成大量图片
req_image = []
finished_text = []

#调用Image函数，传入PDF文件参数
#实际上这里是用wand把PDF做成了jpeg
#wand很智能把所有pdf中细分页面都各自做成了jpeg
image_pdf = Image(filename="./test.pdf", resolution=300)
image_jpeg = image_pdf.convert("jpeg")

#image_jpeg实际上是一个列表对象，所有页面jpeg的集合
#拥有sequenceattribute，是一个列表
#被append的其实都是二进制图像对象
for img in image_jpeg.sequence:
    img_page = Image(image=img)
    #Image函数产生的对象，拥有make_blob方法
    #生成jpeg，装进之前的空列表里
    req_image.append(img_page.make_blob("jpeg"))

#这个是一个test，果然req_image里面就是带页数的
#wand确实如那个作者所说的，把完整pdf按照分页切开了
req_image = req_image[0:2]
print(req_image)
#由于生成的都是
#关于io.BytesIO:Buffered I/O implementation using an in-memory bytes buffer.
#转出来的都是二进制图像对象，遍历这个
#TextBuilder就是builders下的一个函数，无需参数，这里作为一个参数

for img in req_image:
    txt = tool.image_to_string(
        PI.open(io.BytesIO(img)),
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    finished_text.append(txt)
print(len(finished_text))

#这样就把一个个都写进去了，writelines存在编码问题，这个先测试一下，到时候再考虑编码问题
for count in range(len(finished_text)):
    if count == 0:
        with open("test.txt", "w", encoding="utf-8") as f:
            f.write(finished_text[count])
    else:
        with open("test.txt", "a", encoding="utf-8") as f:
            f.write("\n" + "\n" + "page" + finished_text[count])

