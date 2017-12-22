from pymongo import MongoClient
import requests

client = MongoClient()
db = client.lagou  # 创建一个lagou数据库
my_set = db.job  # 创建job集合

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false&isSchoolJob=0'
payload = {
    'first': 'true',
    'pn': '1',
    'kd': '{}'format(kd),
}

headers = {
    'Cookie': 'user_trace_token=20171210195058-6356f9ff-dda0-11e7-8dc4-525400f775ce; LGUID=20171210195058-6356fe14-dda0-11e7-8dc4-525400f775ce; _ga=GA1.2.2037944954.1512906660; _gid=GA1.2.1585272669.1513682022; ab_test_random_num=0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; index_location_city=%E4%B8%8A%E6%B5%B7; hasDeliver=36; LGSID=20171222112023-0c1efd07-e6c7-11e7-a4eb-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; JSESSIONID=ABAAABAAADEAAFIA9E31557E7F70602314FF28DC7D6139A; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513830884,1513831709,1513912821,1513913767; _putrc=BB71D504DD84954D; login=true; unick=%E5%94%90%E5%BF%A0%E7%BB%B4; TG-TRACK-CODE=search_code; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513913857; LGRID=20171222113739-759436ab-e6c9-11e7-a4f0-525400f775ce; SEARCH_ID=802b2fecfe27437582eb70c78d4d10f0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',
}  # 填入对应的headers信息

response = requests.post(url, data=payload, headers=headers)  # 使用POST方法请求数据，加上payload和headers信息
print(response.json())  # 把对应的数据保存到MOngoDB
