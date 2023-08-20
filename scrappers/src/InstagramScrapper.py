import os, platform, time, urllib.request, openpyxl, operator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import Workbook



class InstagramScrapper:
    def scrape(self, tag, limit=20, browser='chrome'):
        keyword = tag
        # opening instagram in browser
        if 'chrome' in browser.lower():
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.get("https://www.instagram.com/" + "explore/tags/" + tag)

        print("Loading Posts")
        time.sleep(10)
        print("Loading Data")

        actions = ActionChains(driver)
        actions.send_keys(Keys.SPACE).perform()
        actions.send_keys(Keys.SPACE).perform()
        actions.send_keys(Keys.SPACE).perform()

        time.sleep(5)

        # Storing images links and captions.
        # are the 'most popular' posts for that tag
        factory_keywords = []
        img_caption = []
        hashtags = {}

        for data in driver.find_elements_by_class_name("FFVAD"):
            #     u.get_attribute("href").split("/")[4]
            img_caption.append(data.get_attribute("alt"))
            factory_keywords.append(data.get_attribute("alt"))

        img_caption.sort()

        for caption in img_caption:
            tags = caption.split("#")[1:]
            for tag in tags:
                cleaned = tag.replace(" ", "").replace("\n", "")
                cleaned = cleaned.lower()
                if cleaned not in hashtags and len(cleaned) < 20:
                    hashtags[cleaned] = 1
                elif cleaned in hashtags and len(cleaned) < 20:
                    hashtags[cleaned] = hashtags[cleaned] + 1

        # sort hashtags with frequencies and store them in excel
        hashtags = sorted(hashtags.items(), key=operator.itemgetter(1), reverse=True)

        driver.quit()
        return [*factory_keywords,*hashtags.values()]