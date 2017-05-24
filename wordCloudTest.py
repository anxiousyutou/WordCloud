#-*- coding:utf-8 -*-
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import matplotlib.pyplot as plt
from scipy.misc import imread
import os

# 获取当前工作目录
working_path = os.getcwd()
RESOURCES_FOLDER = 'resources'
# 拼接背景图片，文本，字体目录
picture_path = os.path.join(working_path, RESOURCES_FOLDER, 'June.jpg')
text_path = os.path.join(working_path, RESOURCES_FOLDER, 'enough.txt')
font_path = os.path.join(working_path, RESOURCES_FOLDER, 'cat.ttf')
# 读取文本
text_from_file_with_path = open(text_path).read()
# 使用jieba分词
wordlist_after_jieba = jieba.cut(text_from_file_with_path, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
# 读取背景图片
background_image = imread(picture_path)
my_wordcloud = WordCloud(
	background_color = "white", # 背景颜色
	font_path = font_path,  # 字体
	mask = background_image, # 背景图片
	max_words = 100 # 最大字数
	).generate(wl_space_split)

'''
# 绘制随机颜色的词云
plt.imshow(my_wordcloud)
plt.axis("off")
my_wordcloud.to_file(os.path.join(working_path, 'result', '2.png'))
'''

# 从背景图片生成颜色值
image_color = ImageColorGenerator(background_image)
# 绘制背景颜色为背景图片颜色的词云
plt.figure()
plt.imshow(my_wordcloud.recolor(color_func = image_color))
# 去掉轴线
plt.axis("off")
# 保存图片
my_wordcloud.to_file(os.path.join(working_path, 'result', '1.png'))
# 显示图片
plt.show()