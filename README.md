# pdf-cutting-OCR
An rough way to do the pdf cutting &amp; OCR with Wand, PIL and pyocr(tesseract OCR Python API)


####PDF逐页转成图片，甚至读进数据库####
这是一个办法，用的是PyPDF2，PythonMagick
http://blog.csdn.net/sweeper_freedoman/article/details/53000145

PythonMagick在Python3下的安装比较麻烦
（大意是在这里下载了一个PythonMagick的whl，然后用本地pip install的方式解决）
http://blog.csdn.net/sweeper_freedoman/article/details/52994690


！！！！有一个只识别第一页的问题，这个是个问题！！！！！
这里涉及到一个安装wand并用wand的问题，因为要用到ImageMagick，存在一些问题
里面用到的是wand，PIL，pyocr组合的解决方案
**pyocr的github
https://github.com/openpaperwork/pyocr
第一个链接是英文原版的链接
https://pythontips.com/2016/02/25/ocr-on-pdf-files-using-python/
第二个链接是中文翻译版的链接
https://python.freelycode.com/contribution/detail/344
****上面这个链接也存在一些问题，主要是在某些代码的写法上，下面这个链接进行了一些补充修正
http://blog.topspeedsnail.com/archives/3571
主要问题出在下图这个位置，由于pyocr支持两种OCR，所以第一个tool选择了用tesseract OCR
第二个tool.get_available_languages()获得了支持的语言列表



这是wand的主页，这个里面应该能找到需要的对应版本，然后试着找找对应版本，版本号对API影响很大
http://docs.wand-py.org/en/0.4.4/

****warning：在下载wand依赖的必须的imagemagick的时候，必须是dll.exe版本，这样的话才能选择添加C++/C的libraries，然后才能在Python里面被调用，而且暂时只有6系列的能被支持
http://www.imagemagick.org/download/binaries/

****warning：ghostscript是必装的，因为没有这个imagemagick并没有办法读取pdf，会缺文件，导致无法读取pdf，毕竟本质是二进制图片文件，缺了这个少了二进制图片矩阵*****
https://ghostscript.com/download/gsdnld.html


