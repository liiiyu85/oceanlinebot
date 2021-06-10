#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import requests

#  海上警戒爬蟲
def wave_alert(locat):
    html = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-B0070-001?Authorization=CWB-94A7BBAA-5768-4A65-9C82-E2AA5F45015E&downloadType=WEB&format=JSON')
    html.encoding = 'UTF-8'
    value = eval(html.text)
    locations = value['cwbdata']['resources']['resource']['data']['seaSurfaceObs']
    locations_lst = []
    for location in locations:
        location_reverse = location['location']['locationName'][::-1] # 去掉浮標兩個字
        location_reverse = location_reverse[2:]
        location_name = location_reverse[::-1]
        locations_lst.append(location_name) #地點
        locations_lst.append(
            location['location']['stationObsTimes'] \
                    ['stationObsTime']['weatherElements']['warningStatus']
        )  # 警示狀態
    if locat in locations_lst:
        pos = locations_lst.index(locat)
        return locations_lst[pos + 1]

#  紫外線警戒爬蟲
def uv_alert(locat):
    html = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0005-001?Authorization=CWB-94A7BBAA-5768-4A65-9C82-E2AA5F45015E&downloadType=WEB&format=JSON')
    html.encoding = 'UTF-8'
    data = eval(html.text)
    lst = data['cwbopendata']['dataset']['weatherElement']['location']
    uv = []
    m = {'467480': '嘉義', '467490': '臺中', '467350': '澎湖', '467270': '彰化', '467110': '金門',
        '467650': '南投', '467660': '台東', '467080': '宜蘭', '467620': '蘭嶼', '467050': '桃園',
        '466940': '基隆', '467610': '三仙台', '466920': '台北', '467590': '屏東', '466910': '陽明山',
        '467570': '新竹', '467410': '台南', '467550': '玉山', '467440': '高雄', '467990': '馬祖',
        '466990': '花蓮'
        }

    for dic in lst:
        uv.append(dic['locationCode']) 
        if float(dic['value']) < 3:
            uv.append('低量級')
        elif float(dic['value']) >= 3 and float(dic['value']) < 6:
            uv.append('中量級')
        elif float(dic['value']) >= 6 and float(dic['value']) < 8:    
            uv.append('高量級')
        elif float(dic['value']) >= 8 and float(dic['value']) < 11:
            uv.append('過量級')
        elif float(dic['value']) >= 11:
            uv.append('危險級')

    for i in range(len(uv)):
        if uv[i] in m:
            uv[i]  = m[uv[i]]
    
    if locat in uv:
        pos = uv.index(locat)
        return uv[pos + 1] 
    
