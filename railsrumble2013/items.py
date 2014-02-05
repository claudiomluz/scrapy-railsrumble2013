# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class RailsRumble2013Item(Item):
    # define the fields for your item here like:
    # name = Field()
    name = Field()
    id = Field()
    href = Field()
    avatar = Field()
    competitor = Field()
    github = Field()

