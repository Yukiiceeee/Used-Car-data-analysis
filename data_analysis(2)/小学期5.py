import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image  # Ensure you have Pillow installed to handle images

# 1. Read CSV file and select first 500 rows
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
df = pd.read_csv(path + 'data_1.csv')
df = df.head(500)  # Take the first 500 rows as simulated user browsing records

# 2. Analyze user preferences
price_preference = df['price'].astype(str).value_counts().to_dict()

# 3. Prepare shape image (mask)
mask = np.array(Image.open('picturetwo.png'))  # Replace with the path to your silhouette shape image
mask = np.where(mask == 0, 255, 0)  # Convert non-white areas to black for the mask

# 4. WordCloud creation
wordcloud = WordCloud(width=800, height=400, background_color='white', mask=mask).generate_from_frequencies(price_preference)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('用户价格偏好词云 - 人形状')
plt.show()