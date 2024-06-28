import requests
import parsel
import csv
from urllib.request import Request, urlopen
from fake_useragent import UserAgent
import random
import time
import datetime
csv_dcd = open('懂车帝二手车交易数据.csv', mode='a', encoding='utf-8', newline='')
csv_write = csv.writer(csv_dcd)
# 如果文件为空，写入表头
if csv_dcd.tell() == 0:
    csv_write.writerow(
        ['SaleID', 'name', 'regDate', 'model', 'brand', 'bodyType', 'fuelType', 'gearbox', 'power', 'kilometer',
         'notRepairedDamage', 'regionCode', 'seller', 'offerType', 'creatDate', 'price'])

bodyType_choices = list(range(8))
fuelType_choices = list(range(7))
gearbox_choices = list(range(2))
notRepairedDamage_choices = list(range(2))

for page in range(1, 163):
    url = f'https://www.dongchedi.com/usedcar/x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x?sh_city_name=%E5%85%A8%E5%9B%BD&page={page}'
    headers = {
        'User-Agent': UserAgent().chrome,
    }
    request = Request(url, headers=headers)
    response = urlopen(request)

    html_data = response.read().decode('utf-8')
    selector = parsel.Selector(html_data)
    lis = selector.css('#__next > div:nth-child(2) > div.new-main.new > div > div > div.wrap > ul li')

    for li in lis:
        title = li.css('a dl dt p::text').get()
        info = li.css('a dl dd:nth-child(2)::text').getall()
        info_str = ''.join(info)
        info_list = info_str.split('|')

        if len(info_list) < 3:
            continue  # 如果信息不完整，跳过该条数据

        name = title
        regDate = info_list[0]
        # kilometer = info_list[1].replace('万公里', '')
        regionCode = random.randint(1000, 9999)

        # 随机赋值
        bodyType = random.choice(bodyType_choices)
        fuelType = random.choice(fuelType_choices)
        gearbox = random.choice(gearbox_choices)
        notRepairedDamage = random.choice(notRepairedDamage_choices)

        brand = name.split()[0]
        model = name.split()[-1]
        power = random.randint(50, 300)
        seller = '个人'
        offerType = random.choice([0, 1])  # 随机选择0或1
        creatDate = datetime
        price = random.randint(1, 100)
        SaleID = str(random.randint(100000, 999999))  # 生成6位随机数字
        kilometer = random.randint(0, 300000)  # 车辆已行驶公里数
        regDate = (datetime.datetime.strptime(creatDate, '%Y-%m-%d') - datetime.timedelta(
            days=random.randint(1, 365))).strftime('%Y-%m-%d')


        print(SaleID, name, regDate, model, brand, bodyType, fuelType, gearbox, power, kilometer, notRepairedDamage,
              regionCode, seller, offerType, creatDate, price)
        csv_write.writerow(
            [SaleID, name, regDate, model, brand, bodyType, fuelType, gearbox, power, kilometer, notRepairedDamage,
             regionCode, seller, offerType, creatDate, price])

csv_dcd.close()