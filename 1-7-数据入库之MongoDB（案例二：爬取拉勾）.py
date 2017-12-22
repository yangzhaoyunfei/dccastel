import requests
from pymongo import MongoClient
import time
from fake_useragent import UserAgent

client = MongoClient()
db = client.lagou
lagou = db.java  # 创建名为java集合

headers = {
    'Cookie': '',
    'Referer': '',
}  # 对应的headers信息


def get_job_info(page, kd):  # 获取数据
    for i in range(page):
        url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
        payload = {
            'first': 'true',
            'pn': i,
            'kd': kd,
        }

        ua = UserAgent()
        headers['User-Agent'] = ua.random  # 使用fake-Agent随机生成User-Agent，添加到headers
        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            job_json = response.json()['content']['positionResult']['result']  # 解析数据
            lagou.insert(job_json)  # 保存数据
        else:
            print('Something Wrong!')

        print('正在爬取' + str(i + 1) + '页的数据...')
        time.sleep(3)


if __name__ == '__main__':
    get_job_info(3, 'java')  # 爬取前3页的PHP职位信息
