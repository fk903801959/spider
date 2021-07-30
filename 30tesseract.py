import pytesseract
from PIL import Image

# 加载文件
img = Image.open('yzm.png')

# 识别文字(将图片中的文字内容提取成字符串的形式)
str = pytesseract.image_to_string(img)
print(str)