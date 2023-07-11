import pandas as pa
df=pa.read_csv("d:\\pylianxi\\text5.csv")
column=df["类型"]
f1 = open("d:\\pylianxi\\类型.txt",'w',encoding="utf-8")
f1.write(str(column))
f1.close()
# 使用指定的图片做词云模板制作词云图片，并保存词云图片
#需要的包有numpy、PIL.Image、 matplotlib.pyplot、wordcloud.WordCloud、jieba
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
#用指定的图案bear.jpg做词云
mypicture = np.array(Image.open("d:/pylianxi/path12.jpg"))  #打开图片文件12
text_file = open('d:/pylianxi/类型.txt',encoding='utf-8').read()  #打开文本文件
wordlist_jieba = jieba.cut(text_file, cut_all=True)   #利用jieba.cut()函数对文本内容进行分词
word_space = " ".join(wordlist_jieba)     #通过.join()函数用空格连接所有单词
#WordCloud(）生成词云 参数mask设置图案模板
my_wordcloud = WordCloud( font_path="‪C:\Windows\Fonts\simhei.ttf",background_color="white",mask=mypicture,width=300,height=2000,).generate(word_space)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
my_wordcloud.to_file('d:/pylianxi/dog.png')