Headers:
    URL: https://www.lagou.com/jobs/positionAjax.json?px=default
         &gx={}&gj=&xl={}&jd={}&hy={}&isSchoolJob=1&city={}&district={}&bizArea={}#filterBox
    POST:

    Request Headers:
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
        Accept: application/json, text/javascript, */*; q=0.01
        Accept-Encoding: gzip, deflate, br
        Accept-Language: zh-CN,zh;q=0.9
        Connection: keep-alive
        Host: www.lagou.com
        Origin: https://www.lagou.com
        Referer: https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?px=default&gx=%E5%AE%9E%E4%B9%A0&gj=&xl=%E6%9C%AC%E7%A7%91&jd=%E4%B8%8D%E9%9C%80%E8%A6%81%E8%9E%8D%E8%B5%84&hy=%E7%A7%BB%E5%8A%A8%E4%BA%92%E8%81%94%E7%BD%91&isSchoolJob=1&city=%E5%8C%97%E4%BA%AC&district=%E6%9C%9D%E9%98%B3%E5%8C%BA&bizArea=%E6%9C%9B%E4%BA%AC
            {
                list_{}:  urllib.quote(kd.encode('utf-8')),
                &gx={}:   urllib.quote(gx.encode('utf-8')),
                &gj=&xl={}:     urllib.quote(xl.encode('utf-8')),
                &jd={}:   urllib.quote(jd.encode('utf-8')),
                &hy={}:   urllib.quote(hy.encode('utf-8')),
                &isSchoolJob=1
                &city={}    urllib.quote(city.encode('utf-8')),
                &district={}    urllib.quote(district.encode('utf-8')),
                &bizArea={}     urllib.quote(bizArea.encode('utf-8')),
            }

    Cookie:{
        Cookie: user_trace_token=20180215110702-ac0267f8-0ed5-46d6-918b-391459c58537;
        _ga=GA1.2.71597998.1518664046; LGUID=20180215110703-4c403271-11fd-11e8-b06b-5254005c3644;
        index_location_city=%E5%85%A8%E5%9B%BD;
        JSESSIONID=ABAAABAACBHABBID4AE8F00FF3FA00DFF31395907175C6F;
        _gid=GA1.2.560310547.1524398895;
        Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1524227534,1524398895;
        LGSID=20180422200751-c7ab2fcc-4625-11e8-9455-525400f775ce; PRE_UTM=; PRE_HOST=;
        PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F;
        TG-TRACK-CODE=search_code; _gat=1;
        Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1524400164;
        LGRID=20180422202900-bc65f598-4628-11e8-9456-525400f775ce;
        SEARCH_ID=c55fe207864c4457b5d663b06442e820
    }

    Query String Parameters:
        xl: 本科         #学历要求
        jd: 不需要融资   #融资阶段
        hy: 移动互联网   #行业领域
        px: default
        gx: 全职      #工作性质（应届：全职， 实习：实习）
        city: 北京    #工作地点
        district: 朝阳区   #工作地点的城区
        bizArea: 望京     #工作地点的商区
        needAddtionalResult: false
        isSchoolJob: 1

    Form Data:
        first: true
        pn: 1       #页码
        kd: python爬虫    #所搜职位

JSON
    import json
    url = URL: https://www.lagou.com/jobs/positionAjax.json?px=default
         &gx={}&gj=&xl={}&jd={}&hy={}&isSchoolJob=1&city={}&district={}&bizArea={}#filterBox
    page = requests.post(url=url, cookies=cookies, headers=headers, data=data)
    page.encoding = 'utf-8'
    result = page.json()
    jobs = result['content']['positionResult']['result']
    for job in jobs:
		companyShortName = job['companyShortName'] #公司简称
		companyLabelList = job['companyLabelList'] #福利待遇
		companyFullName = job['companyFullName'] #公司全名
		companySize = job['companySize'] #公司规模
		createTime = job['createTime'] # 发布时间
		district = job['district'] #所在地区
		education = job['education'] #学历要求
		financeStage = job['financeStage'] #上市否
		firstType = job['firstType'] #类型
		secondType = job['secondType'] #类型
		formatCreateTime = job['formatCreateTime'] #发布时间
		industryField = job['industryField'] #公司属性
		jobNature = job['jobNature'] #全职
		positionAdvantage = job['positionAdvantage'] #工作福利
		positionId = job['positionId'] #主页ID，下一页链接id
		positionLables = job['positionLables'] #工种
		positionName = job['positionName'] #职位名称
		publisherId = job['publisherId'] #发布人ID
        salary = job['salary'] #薪资
		workYear = job['workYear'] #工作年限



