import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image  # 需要安装Pillow库来处理图像

# 1. 读取CSV文件并选择前500条数据
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
df = pd.read_csv(path + 'data_1.csv')

df = df.head(500)  # 获取前500条数据作为模拟用户浏览记录

# 2. 分析用户喜好
# 假设我们要分析用户对价格的偏好
price_preference = df['price'].astype(str).value_counts().to_dict()

# 3. 准备形状图片
mask = np.array(Image.open(path + 'test.png'))  # 替换成你的人形状图片路径，确保是白色主体的PNG图片

# 4. 词云绘制
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    mask=mask,
    contour_width=1,  # 增加轮廓线
    contour_color='black'  # 轮廓线颜色
).generate_from_frequencies(price_preference)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('用户价格偏好词云 - 人形状')
plt.show()