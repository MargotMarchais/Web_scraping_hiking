import scrapy

class HikeScraper(scrapy.Spider):
    name = 'labalaguere_last_voyage' 
    start_urls = ['https://www.labalaguere.com/groupe-accompagne.html'] 

    def parse(self, response):
        for hikes in response.css('li.voyage.last'): 
            yield {
                'name':  hikes.css('h3.title a::text').get(),
                'place': hikes.css('div.zone span::text').get(),
				'duration': hikes.css('div.prix span.duree::text').get(),
                'travel_type': hikes.css('div.ligne.ligne2 span::text').get().strip(),
				'difficulty_level1': hikes.css('div.niveaux.niv span i:nth-of-type(1)::attr(class)').get(),
                'difficulty_level2': hikes.css('div.niveaux.niv span i:nth-of-type(2)::attr(class)').get(),
                'difficulty_level3': hikes.css('div.niveaux.niv span i:nth-of-type(3)::attr(class)').get(),
                'difficulty_level4': hikes.css('div.niveaux.niv span i:nth-of-type(4)::attr(class)').get(),
                'difficulty_level5': hikes.css('div.niveaux.niv span i:nth-of-type(5)::attr(class)').get(),
                'price': hikes.css('div.prix span.orange::text').get(),
				'special_info': 'N/A',
                'notations': 'N/A',
                'stars': 'N/A',
                'travel_info_1': 'N/A',
                'travel_info_2': 'N/A',
				'is_available_month1': hikes.css('div.saison ul li:nth-of-type(1) a::attr(title)').get(),
                'is_available_month2': hikes.css('div.saison ul li:nth-of-type(2) a::attr(title)').get(),
                'is_available_month3': hikes.css('div.saison ul li:nth-of-type(3) a::attr(title)').get(),
                'is_available_month4': hikes.css('div.saison ul li:nth-of-type(4) a::attr(title)').get(),
                'is_available_month5': hikes.css('div.saison ul li:nth-of-type(5) a::attr(title)').get(),
                'is_available_month6': hikes.css('div.saison ul li:nth-of-type(6) a::attr(title)').get(),
                'is_available_month7': hikes.css('div.saison ul li:nth-of-type(7) a::attr(title)').get(),
                'is_available_month8': hikes.css('div.saison ul li:nth-of-type(8) a::attr(title)').get(),
                'is_available_month9': hikes.css('div.saison ul li:nth-of-type(9) a::attr(title)').get(),
                'is_available_month10': hikes.css('div.saison ul li:nth-of-type(10) a::attr(title)').get(),
                'is_available_month11': hikes.css('div.saison ul li:nth-of-type(11) a::attr(title)').get(),
                'is_available_month12': hikes.css('div.saison ul li:nth-of-type(12) a::attr(title)').get(),
                'url':  hikes.css('h3.title a::attr(href)').get(),
                'itinerary': hikes.css('div.ligne.ligne1bis::text').get(),
                'next_departure' : hikes.css('div.depart span::text').get(),
                'description': hikes.css('div.ligne.ligne5 a::text').get().strip()
            }

        # Next pages:
        next_page =  'https://www.labalaguere.com' + response.css('div.item-list li.pager-next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)



            