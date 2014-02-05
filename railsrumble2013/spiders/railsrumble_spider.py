from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
import urlparse

from railsrumble2013.items import RailsRumble2013Item

class RailsRumble2013Spider(Spider):
   name = "railsrumble2013"
   allowed_domains = ["railsrumble.com", "github.com"]
   start_urls = [
       "http://railsrumble.com/participants",
       "http://railsrumble.com/participants?page=2",
       "http://railsrumble.com/participants?page=3",
       "http://railsrumble.com/participants?page=4",
       "http://railsrumble.com/participants?page=5",
       "http://railsrumble.com/participants?page=6",
       "http://railsrumble.com/participants?page=7",
       "http://railsrumble.com/participants?page=8",
       "http://railsrumble.com/participants?page=9",
       "http://railsrumble.com/participants?page=10",
       "http://railsrumble.com/participants?page=11",
       "http://railsrumble.com/participants?page=12",
       "http://railsrumble.com/participants?page=13",
       "http://railsrumble.com/participants?page=14",
       "http://railsrumble.com/participants?page=15",
       "http://railsrumble.com/participants?page=16",
       "http://railsrumble.com/participants?page=17",
       "http://railsrumble.com/participants?page=18",
       "http://railsrumble.com/participants?page=19",
       "http://railsrumble.com/participants?page=20",
       "http://railsrumble.com/participants?page=21",
       "http://railsrumble.com/participants?page=22",
       "http://railsrumble.com/participants?page=23",
       "http://railsrumble.com/participants?page=24",
       "http://railsrumble.com/participants?page=25",
       "http://railsrumble.com/participants?page=26",
       "http://railsrumble.com/participants?page=27",
       "http://railsrumble.com/participants?page=28"  
   ]

   def parse(self, response):
       sel = Selector(response)
       people = sel.xpath('//div[@id="people"]/a')
       links = []

       items = []
       for person in people:
           item = RailsRumble2013Item()
           item['id'] = person.xpath('@id').extract()[0].strip()
           item['name'] = person.xpath('span[2]/text()').extract()[0].strip()
           item['avatar'] = person.xpath('span/img/@src').extract()[0].strip()
           item['href'] = person.xpath('@href').extract()[0].strip()
           
           url = urlparse.urljoin('http://railsrumble.com', item['href'])
           yield Request(url, meta = {'item':item}, callback=self.parse_person)


   def parse_person(self, response):
       sel = Selector(response)
       details = sel.xpath('//div[@id="details"]')

       item = response.request.meta['item']
       item['competitor'] = details.xpath('ul/li[1]/a/text()').extract()[0].strip()
       url_github = details.xpath('ul/li[2]/a/@href').extract()[0].strip()
       item['github'] = url_github
       
       #yield item
       yield Request(url_github, meta = {'item':item}, callback=self.parse_github)



   def parse_github(self, response):
       sel = Selector(response)
       item = response.request.meta['item']
       location = sel.xpath('//ul[@class="vcard-details"]/li[@itemprop="homeLocation"]/text()').extract()
       if location:
          item['location'] = location[0].strip()
       else:
          item['location'] = "not declared"
       yield item



