from src.InstagramScrapper import InstagramScrapper
from src.TwitterScrapper import TwitterScrapper
from src.trends import GTrends
import os 

def scrapeKeywords():
    print("Starting Social Media Scrapper...")
    keyword = ["t-shirt", "jeans", "dress", "sweater", "jacket", "skirt", "shorts", "hoodie", "blouse", "pants"]
    insta_limit = 100
    twitter_limit = 100

    consumerKey = os.environ.get("consumerKey")
    consumerSecret = os.environ.get("consumerSecret")
    accessToken = os.environ.get("accessToken")
    accessTokenSecret = os.environ.get("accessTokenSecret")
    taglist = []

    scrapper = InstagramScrapper()
    taglist += scrapper.scrape(tag=keyword,
                              limit=insta_limit,
                              browser='chrome')


    twitter = TwitterScrapper()
    taglist += twitter.scrape(Consumer_Key=consumerKey,
                           Consumer_Secret=consumerSecret,
                           Access_Token=accessToken,
                           Access_Token_Secret=accessTokenSecret,
                           tag=keyword,
                           limit=twitter_limit,
                           lang='en') 
    
    gtrend = GTrends()
    taglist += gtrend.scrape(tag=keyword)


    print("Stopping Social Media Scrapper...")
    return taglist

