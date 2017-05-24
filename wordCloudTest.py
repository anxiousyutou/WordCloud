from wordcloud import WordCloud, ImageColorGenerator
import jieba
import matplotlib.pyplot as plt
from scipy.misc import imread

text_from_file_with_apath = open('F:\\0FileOfYutou\\enough.txt').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

background_image = imread("F:\\0FileOfYutou\\tree4.jpg")
#background_image = plt.imread("F:\\0FileOfYutou\\June.jpg")
image_color = ImageColorGenerator(background_image)
my_wordcloud = WordCloud(
	background_color = "white",
	font_path = "F:\\0FileOfYutou\\cat.ttf",
	mask = background_image,
	max_words = 100
	).generate(wl_space_split) 

'''
plt.imshow(my_wordcloud)
plt.axis("off")
'''

plt.figure()
plt.imshow(my_wordcloud.recolor(color_func = image_color))
plt.axis("off")

'''
plt.figure()
plt.imshow(background_image, cmap=plt.cm.gray)
plt.axis("off")
'''
plt.show()