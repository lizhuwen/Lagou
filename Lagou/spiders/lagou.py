# -*- coding: utf-8 -*-
from scrapy import Spider, Request, FormRequest
import json
from Lagou.items import LagouItem
import uuid
import time

class LagouSpider(Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = [
        'http://www.lagou.com'
    ]

    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&px=default&needAddtionalResult=false&isSchoolJob=0'
    data = {
        'first': 'false',
        'pn': '1',
        'kd': 'Python'
    }
    kds = ['Python','Java']
    # cookies = {
    #     'Cookie': '_ga=GA1.2.2082882450.1518874102;'
    #                 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1518874102;'
    #                 'user_trace_token=' + str(uuid.uuid4())+';'
    #                 'LGUID=' + str(uuid.uuid4())+';'
    #                 'index_location_city=%E6%B7%B1%E5%9C%B3;'
    #                 'JSESSIONID=' + str(uuid.uuid4())+';'
    #                 'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1519270516;'
    #                 'LGRID=' + str(uuid.uuid4())+';'
    #                 '_gid=' + str(uuid.uuid4())+';'
    #                 'TG-TRACK-CODE=index_navigation;'
    #                 'SEARCH_ID=' + str(uuid.uuid4())+';'
    #                 'LGSID=' + str(uuid.uuid4())+';'
    # }

    def get_cookies(self):
        cookies = {
            'Cookie': '_ga=GA1.2.2082882450.1518874102;'
                        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1518874102;'
                        'user_trace_token=' + str(uuid.uuid4())+';'
                        'LGUID=' + str(uuid.uuid4())+';'
                        'index_location_city=%E6%B7%B1%E5%9C%B3;'
                        'JSESSIONID=' + str(uuid.uuid4())+';'
                        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1519270516;'
                        'LGRID=' + str(uuid.uuid4())+';'
                        '_gid=' + str(uuid.uuid4())+';'
                        'TG-TRACK-CODE=index_navigation;'
                        'SEARCH_ID=' + str(uuid.uuid4())+';'
                        'LGSID=' + str(uuid.uuid4())+';'
        }
        return cookies

    def start_requests(self):
        for x in range(1, 30):
            self.data['pn'] = str(x)
            # for y in self.kds:
            #     self.data['kd'] = y
            yield FormRequest(url=self.url, formdata=self.data, cookies=self.get_cookies(), callback=self.Lagouparse)


    def Lagouparse(self, response):
        #print(response.body)
        result = json.loads(response.body)['content']['positionResult']['result']
        #计算总页，取消30页限制
        totalPageCount = json.loads(response.body)['content']['positionResult']['totalCount'] /15 + 1
        #print(self.totalPageCount)
        for job in result:
            item = LagouItem()

            print('----------\n')
            item['companyShortName'] = job['companyShortName']  # 公司简称
            item['companyLabelList'] = job['companyLabelList']  # 福利待遇
            item['companyFullName'] = job['companyFullName']  # 公司全名
            item['companySize'] = job['companySize']  # 公司规模
            item['createTime'] = job['createTime']  # 发布时间
            item['district'] = job['district']  # 所在地区
            item['education'] = job['education']  # 学历要求
            item['financeStage'] = job['financeStage']  # 上市否
            item['firstType'] = job['firstType']  # 类型
            item['secondType'] = job['secondType']  # 类型
            item['formatCreateTime'] = job['formatCreateTime']  # 发布时间
            item['industryField'] = job['industryField']  # 公司属性
            item['jobNature'] = job['jobNature']  # 全职
            item['positionAdvantage'] = job['positionAdvantage']  # 工作福利
            item['positionId'] = job['positionId']  # 主页ID，下一页链接id
            item['positionLables'] = job['positionLables']  # 工种
            item['positionName'] = job['positionName']  # 职位名称
            item['publisherId'] = job['publisherId']  # 发布人ID
            item['salary'] = job['salary']  # 薪资
            item['workYear'] = job['workYear']  # 工作年限

            # print('公司全名：%s' % job['companyFullName'])
            # print('公司简称：%s' % job['companyShortName'])
            # print('职位名称：%s' % job['positionName'])
            # print('工作年限：%s' % job['workYear'])
            # print('学历要求：%s' % job['education'])
            # print('薪资：%s' % job['salary'])
            # print('所在地区：%s' % job['district'])
            # print('发布时间：%s' % job['formatCreateTime'])
            yield item
        # if self.curpage <= self.totalPageCount:
        #     #判断当前页面还没有到达了30页，递归
        #     self.curpage += 1
        #     print(self.curpage, self.kd)
        #     yield FormRequest(url=self.url, formdata={'pn': str(self.curpage), 'kd': self.kd},
        #                   cookies=self.get_cookies(), callback=self.Lagouparse)
        # elif self.cur < len(self.kds)-1:
        #     #如果已经30页了，爬取下一个关键词kd，并且将页码与总数重置归原始数值，kd下标cur加1，递归
        #     self.curpage = 1
        #     self.totalPageCount = 0
        #     self.cur += 1
        #     self.kd = self.kds[self.cur]
        #     yield FormRequest(url=self.url, formdata={'pn': str(self.curpage), 'kd': self.kd},
        #                       cookies=self.cookies, callback=self.parse)


