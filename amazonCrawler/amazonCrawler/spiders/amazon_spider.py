# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazoncrawlerItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.com']
    page_number = 2
    start_urls = ['https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1592135608&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0']

    def parse(self, response):
        items = AmazoncrawlerItem()

        all_products_divs = response.css(".s-latency-cf-section")

        for product in all_products_divs:
            


            product_name = product.css(".a-color-base.a-text-normal::text").extract()
            product_author = product.css(".a-color-secondary .a-size-base.a-link-normal::text").extract()
            product_price = product.css(".a-spacing-top-small .a-price-whole::text").extract()
            product_img = product.css(".s-image::attr(src)").extract()
        
            if(type(product_name =='list')):
                items['product_name'] = product_name[0]
            else:
                items['product_name'] = product_name
            
            items['product_author']= product_author
            if(type(product_price =='list')):
                items['product_price'] = product_price[0]
            else:
                items['product_price']=product_price
            
            if(type(product_img =='list')):

                items['product_img'] = product_img[0]
            else:
                items['product_img'] = product_img
                
            
            yield items
            
        

        next_page = "https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page="+str(AmazonSpiderSpider.page_number)+"&fst=as%3Aoff&qid=1592138004&rnid=1250225011&ref=sr_pg_2"
        if AmazonSpiderSpider.page_number != 25:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page,callback=self.parse)
