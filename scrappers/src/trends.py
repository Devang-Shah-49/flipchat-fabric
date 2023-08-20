import pandas as pd     
import time                   
from pytrends.request import TrendReq

#provide your search terms

class GTrends:
    def scrape(tag):
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=tag,cat=0, geo='IN')
        related_queries = pytrend.related_queries()
        related_topics = pytrend.related_topics()

        rising_tags = list(related_queries.values())[0]['rising']["query"]
        top_tags = list(related_queries.values())[0]['top']["query"]
        rising_tags =[*rising_tags,*list(related_topics.values())[0]['rising']["query"]]
        top_tags =[*top_tags,*list(related_topics.values())[0]['top']["query"]]
        return [*rising_tags,*top_tags]




#build lists dataframes

# top = list(related_queries.values())[0]['top']


# print(rising)
# from pytrends.request import TrendReq

# # Create a PyTrends object
# pytrends = TrendReq(hl='en-US', tz=360)

# # List of clothing-related keywords
# clothing_keywords = ["t-shirt", "jeans", "dress", "sweater", "jacket", "skirt", "shorts", "hoodie", "blouse", "pants"]

# # Build the payload
# pytrends.build_payload(kw_list=clothing_keywords)

# # Get the interest over time data
# interest_data = pytrends.interest_over_time()

# # Print the extracted data
# print(interest_data)