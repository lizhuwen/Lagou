# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    companyShortName = scrapy.Field() # 公司简称
    companyLabelList = scrapy.Field()  # 福利待遇
    companyFullName = scrapy.Field()  # 公司全名
    companySize = scrapy.Field()  # 公司规模
    createTime = scrapy.Field()  # 发布时间
    district = scrapy.Field()  # 所在地区
    education = scrapy.Field()  # 学历要求
    financeStage = scrapy.Field()  # 上市否
    firstType = scrapy.Field()  # 类型
    secondType = scrapy.Field()  # 类型
    formatCreateTime = scrapy.Field()  # 发布时间
    industryField = scrapy.Field()  # 公司属性
    jobNature = scrapy.Field()  # 全职
    positionAdvantage = scrapy.Field()  # 工作福利
    positionId = scrapy.Field()  # 主页ID，下一页链接id
    positionLables = scrapy.Field()  # 工种
    positionName = scrapy.Field()  # 职位名称
    publisherId = scrapy.Field()  # 发布人ID
    salary = scrapy.Field()  # 薪资
    workYear = scrapy.Field()  # 工作年限
