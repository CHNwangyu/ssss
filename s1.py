import requests
from lxml import etree

data = {
    "erectDate": "请输入关键字",
    "nothing": "2021-12-31",
    "pjname": "美元",

}


# response = requests.post(url, headers=headers, data=data)


class Get_Money(object):
    def __init__(self):
        self.flag = {'HKD': '港元 ', 'MOP': '澳门元 ', 'CNY': '人民币元 ', 'KPW': '圆 ', 'VND': '越南盾 ',
                     'JPY': '日圆 ', 'LAK': '基普 ', 'KHR': '瑞尔 ', 'PHP': '菲律宾比索 ', 'MYR': '马元 ',
                     'SGD': '新加坡元 ', 'THP': '泰铢 ', 'BUK': '缅元 ', 'LKR': '斯里兰卡卢比 ', 'MVR': '马尔代夫卢比 ',
                     'IDR': '盾 ', 'PRK': '巴基斯坦卢比 ', 'INR': '卢比 ', 'NPR': '尼泊尔卢比 ', 'AFA': '阿富汗尼 ',
                     'IRR': '伊朗里亚尔 ', 'IQD': '伊拉克第纳尔 ', 'SYP': '叙利亚镑 ', 'LBP': '黎巴嫩镑 ',
                     'JOD': '约旦第纳尔 ', 'SAR': '亚尔 ', 'KWD': '科威特第纳尔 ', 'BHD': '巴林第纳尔 ',
                     'QAR': '卡塔尔里亚尔 ', 'OMR': '阿曼里亚尔 ', 'YER': '也门里亚尔 ', 'YDD': '也门第纳尔 ',
                     'TRL': '土耳其镑 ', 'CYP': '塞浦路斯镑 ', 'EUR': '欧元 ', 'ISK': '冰岛克朗 ', 'DKK': '丹麦克朗 ',
                     'NOK': '挪威克朗 ', 'SEK': '瑞典克朗 ', 'FIM': '芬兰马克 ', 'SUR': '卢布 ', 'PLZ': '兹罗提 ',
                     'CSK': '捷克克朗 ', 'HUF': '福林 ', 'DEM': '马克 ', 'ATS': '奥地利先令 ', 'CHF': '瑞士法郎 ',
                     'NLG': '荷兰盾 ', 'BEF': '比利时法郎 ', 'LUF': '卢森堡法郎 ', 'GBP': '英镑 ', 'IEP': '爱尔兰镑 ',
                     'FRF': '法郎 ', 'ESP': '比塞塔 ', 'PTE**': '埃斯库多 ', 'ITL': '里拉 ', 'MTP': '马耳他镑 ',
                     'YUD': '南斯拉夫新第纳尔 ', 'ROL': '列伊 ', 'BGL': '列弗 ', 'ALL': '列克 ', 'GRD': '德拉马克 ',
                     'CAD': '加元 ', 'USD': '美元 ', 'MXP': '墨西哥比索 ', 'GTQ': '格查尔 ', 'SVC': '萨尔瓦多科朗 ',
                     'HNL': '伦皮拉 ', 'NIC': '科多巴 ', 'CRC': '哥斯达黎加科朗 ', 'PAB': '巴拿马巴波亚 ',
                     'CUP': '古巴比索 ', 'BSD': '巴哈马元 ', 'JMD': '牙买加元 ', 'HTG': '古德 ', 'DOP': '多米尼加比索 ',
                     'TTD': '特立尼达多巴哥元 ', 'BBD': '巴巴多斯元 ', 'COP': '哥伦比亚比索 ', 'VEB': '博利瓦 ',
                     'GYD': '圭亚那元 ', 'SRG': '苏里南盾 ', 'PES': '新索尔 ', 'ECS': '苏克雷 ', 'BRC': '新克鲁赛罗 ',
                     'BOP': '玻利维亚比索 ', 'CLP': '智利比索 ', 'ARP': '阿根廷比索 ', 'PYG': '巴拉圭瓜拉尼 ',
                     'UYP': '乌拉圭新比索 ', 'EGP': '埃及镑 ', 'LYD': '利比亚第纳尔 ', 'SDP': '苏丹镑 ',
                     'TND': '突尼斯第纳尔 ', 'DZD': '阿尔及利亚第纳尔 ', 'MAD': '摩洛哥迪拉姆 ', 'MRO': '乌吉亚 ',
                     'XOF': '非共体法郎 ', 'GMD': '法拉西 ', 'GWP': '几内亚比索 ', 'GNS': '几内亚西里 ', 'SLL': '利昂 ',
                     'LRD': '利比里亚元 ', 'GHC': '塞地 ', 'NGN': '奈拉 ', 'XAF': '中非金融合作法郎 ',
                     'GQE': '赤道几内亚埃奎勒 ', 'ZAR': '兰特 ', 'DJF': '吉布提法郎 ', 'SOS': '索马里先令 ',
                     'KES': '肯尼亚先令 ', 'UGS': '乌干达先令 ', 'TZS': '坦桑尼亚先令 ', 'RWF': '卢旺达法郎 ',
                     'BIF': '布隆迪法郎 ', 'ZRZ': '扎伊尔 ', 'ZMK': '赞比亚克瓦查 ', 'MCF': '马达加斯加法郎 ',
                     'SCR': '塞舌尔卢比 ', 'MUR': '毛里求斯卢比 ', 'ZWD': '津巴布韦元 ', 'KMF': '科摩罗法郎 ',
                     'AUD': '澳大利亚元 ', 'NZD': '新西兰元 ', 'FJD': '斐济元 '}
        self.url = "https://srh.bankofchina.com/search/whpj/search_cn.jsp"
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://srh.bankofchina.com",
            "Referer": "https://srh.bankofchina.com/search/whpj/search_cn.jsp",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
            "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Microsoft Edge\";v=\"122\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }

    def get_money(self, date, flag):
        data = {
            "nothing": f'{date}',
            "pjname": self.flag[flag.upper()].replace(' ',''),
        }
        response = requests.post(url=self.url, headers=self.headers, data=data)
        tree = etree.HTML(response.text)
        main_body = tree.xpath('//tr')
        if len(main_body) == 0:
            print('无数据')
            return 'no'
        num = len(main_body)
        for i in main_body[2:-2]:
            m1 = i.xpath('./td[1]/text()')[0]
            m2 = i.xpath('./td[2]/text()')[0]
            m3 = i.xpath('./td[3]/text()')[0]
            m4 = i.xpath('./td[4]/text()')[0]
            m5 = i.xpath('./td[5]/text()')[0]
            m6 = i.xpath('./td[6]/text()')[0]
            m7 = i.xpath('./td[7]/text()')[0]
            data_list = [m1,m2,m3,m4,m5,m6,m7]
            data_str = '|'.join(data_list).replace('\n','').replace('\t','')
            with open('result.txt',encoding='utf=8',mode='a')as f:
                print(data_str)
                f.write(data_str)
            # with open()
            # print(data_list)
        print(main_body[4].xpath('./td[4]/text()')[0])
        # for i in main_body[1:]:

    def parse_input_data(self):
        while True:
            print('===========================')
            print('请输入想要查询的日期  例如2021-12-31')
            in_date = input()
            if ('-' not in in_date):
                print('日期格式不对请重来')
                continue
            print('=========================')
            print(self.flag)
            print('=========================')
            print('请输入货币代号,上方是代号提示')
            in_m = input()
            try:
                print(f'您查询的信息为{in_date}的{self.flag[in_m.upper()]}的价格')
            except:
                print('找不到您输入的货币代号请重新选择')
                continue
            print('输入y确认，输入其他重写编写，输入q退出')
            y_n = input().lower()
            if y_n == 'y':
                self.get_money(date=in_date, flag=in_m)
            if y_n == 'q':
                break
            else:
                continue


if __name__ == '__main__':
    get = Get_Money()
    get.parse_input_data()
