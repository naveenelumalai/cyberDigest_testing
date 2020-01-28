import scrapy
import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

from second_app.models import CyberStories

class CyberDigestSpider(scrapy.Spider):
    name = "scrapyToDb"

    def start_requests(self):
        urls = [
            'https://www.wired.com/feed/category/security/latest/rss',
            'http://www.independent.co.uk/topic/cyber-security/rss',
            'https://www.scmagazine.com/home/security-news/feed/',
            'http://feeds.feedburner.com/TheHackersNews?format=xml',
            'https://cio.economictimes.indiatimes.com/rss',
            'https://news.sophos.com/en-us/feed/',
            'https://anonhq.com/feed/',
            'https://indianexpress.com/section/technology/feed/',
            'https://cyware.com/allnews/feed',
            'https://threatpost.com/feed/',
            'https://www.securitymagazine.com/rss/articles',
            'https://www.news18.com/rss/tech.xml',
            'https://feeds.feedburner.com/securityweek'

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        storyTitle = []
        storyLink = []
        storyPublished = []
        storyDescription = []

        for post in response.xpath('//channel/item'):
            print(post)
            storyTitle.append(post.xpath('title//text()').extract_first())
            storyLink.append(post.xpath('link//text()').extract_first())
            tempPublished = post.xpath('pubDate//text()').extract_first()
            tempPublished = tempPublished[5:25]
            dateFormat = '%d %b %Y %H:%M:%S'
            formatedDate = datetime.datetime.strptime(tempPublished,dateFormat)
            storyPublished.append(formatedDate)
            storyDescription.append(post.xpath('description//text()').extract_first())

        i = 0
        totalStory = len(storyTitle)

        while i < totalStory:
            addStory = CyberStories.objects.get_or_create(Title=storyTitle[i],
                                                        Link = storyLink[i],
                                                        Published = storyPublished[i],
                                                        Description = storyDescription[i]
                                                        )[0]

            i += 1
        
