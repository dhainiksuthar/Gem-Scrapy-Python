import scrapy
from itemloaders import ItemLoader
from ..items import GemItem

class gemPortal(scrapy.Spider):
    name = 'gemPortal'
    # start_urls = ['https://mkp.gem.gov.in/computers-0806nb/search']

    def start_requests(self):
        urls = [
            'https://mkp.gem.gov.in/computers-desktop-computer/search',
            # 'https://mkp.gem.gov.in/computers-0806nb/search',
            'https://mkp.gem.gov.in/duplicating-machines-0901mfm/search',
            'https://mkp.gem.gov.in/25101500-cars-version-2-/search'
            'https://mkp.gem.gov.in/writing-instruments-ball-point-pens-as-per-is-3705/search'
        ]
        category = [
            'Computer',
            # 'Computer',
            'Office machines',
            'Automobiles',
            'Office Supplies'
        ]
        subCategory = [
            'Desktop',
            # 'Laptops',
            'MultiFunction Machines',
            'Cars'
            'Ball Point Pen'
        ]

        for (url, sCat, cat) in zip(urls, subCategory, category):
            self.item = ItemLoader(item=GemItem())
            self.item.add_value('category', cat)
            self.item.add_value('subCategory', sCat)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        URLs = response.css(".variant-image > a::attr('href')").getall()
        for url in URLs:
            self.item.add_value('url', url)
            yield scrapy.Request(url="https://mkp.gem.gov.in" + url, callback=self.moreFeatures)

    def moreFeatures(self, response):
        name = response.xpath("//*[@id='title']/h1/text()").get().strip()
        price = response.xpath("//*[@id='pricing_summary']/div[1]/div[1]/span/span/text()").get()
        features = response.xpath('//*[@id="golden-parameters"]/div/div').getall()
        length = len(features)
        print(length)
        key = []
        val = []
        for i in range(1, length+1):
            k = response.xpath('//*[@id="golden-parameters"]/div/div['+ str(i) + ']/span[1]/text()').extract()
            v = response.xpath('//*[@id="golden-parameters"]/div/div['+ str(i) + ']/span[2]/text()').extract()
            key.append(k)
            val.append(v)
        
        self.item.add_value('name', name)
        self.item.add_value('price', price)
        self.item.add_value('key', key)
        self.item.add_value('val', val)
        yield self.item.load_item()