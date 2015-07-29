# coding:utf-8
import scrapy
from scrapy.http import Request
from ..items import oneItem
from .. import common

gamelist = set()
itemlist = set()
totalprice = 0.0
totalpage = 1
totalrecord = 0
class oneSpider(scrapy.spiders.Spider):
    #5173
    name = "one"
    allowed_domains = ["dlc2c.5173.com"]
    start_urls = [
        "http://dlc2c.5173.com/main/index.aspx"
    ]

    def parse_nextitem(self, response):
        global itemlist,totalprice,totalpage,totalrecord
        gameitem = response.meta['item']
        for sel in response.xpath('//div[@class="goodslist"]'):
            item = oneItem()
            item['title'] = sel.xpath('//ul/li/h1/a/text()').extract()
            item['link'] = sel.xpath('//ul/li/h1/a/@href').extract()
            item['price'] = sel.xpath('//div[@class="price"]/text()').re('\d*\.\d\d')
            itemlist.add(item)

            for itemprice in item['price']:
                if len(itemprice)>0:
                    totalprice += float(itemprice)

        for sel in response.xpath('//div[@class="pagetab"]'):
            totalpage = int(sel.xpath('//span[@id="lblTotalPages"]/text()').extract()[0])
            totalrecord = int(sel.xpath('//span[@id="totalRecords"]/text()').extract()[0])

        print str(gameitem['title'][0])+u'__条数:'+str(len(itemlist))+u'_总金额:'+str(totalprice)+u'_总条数:'+str(totalrecord)+u'_总页数:'+str(totalpage)

    def parse_item(self, response):
        global itemlist,totalprice,totalpage,totalrecord
        gameitem = response.meta['item']

        for sel in response.xpath('//div[@class="goodslist"]'):
            item = oneItem()
            item['title'] = sel.xpath('//ul/li/h1/a/text()').extract()
            item['link'] = sel.xpath('//ul/li/h1/a/@href').extract()
            item['price'] = sel.xpath('//div[@class="price"]/text()').re('\d*\.\d\d')
            itemlist.add(item)

            for itemprice in item['price']:
                if len(itemprice)>0:
                    totalprice += float(itemprice)

        for sel in response.xpath('//div[@class="pagetab"]'):
            totalpage = int(sel.xpath('//span[@id="lblTotalPages"]/text()').extract()[0])
            totalrecord = int(sel.xpath('//span[@id="totalRecords"]/text()').extract()[0])

        for pageindex in xrange(2,totalpage):
            if len(gameitem['title'])>0:
                yield Request('http://dlc2c.5173.com/main/'+str(gameitem['link'][0])+'&page='+str(pageindex), meta={'item':gameitem}, callback=self.parse_nextitem)

        print str(gameitem['title'][0])+u'__条数:'+str(len(itemlist))+u'_总金额:'+str(totalprice)+u'_总条数:'+str(totalrecord)+u'_总页数:'+str(totalpage)

    def parse(self, response):
        global gamelist,totalprice,totalpage,totalrecord
        for sel in response.xpath('//div[@class="homeGameListBox"]/ul/li'):

            item = oneItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            gamelist.add(item)
        #gamelist = common.delrepeat(gamelist)

        for index,gameitem in enumerate(gamelist):
            if len(gameitem['title'])>0:
                print '项目名称_'+str(index+1)+':'+gameitem['title'][0]+':'+gameitem['link'][0]
                yield Request('http://dlc2c.5173.com/main/'+gameitem['link'][0], meta={'item':gameitem}, callback=self.parse_item)
            
        '''
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        '''