import os
import zipfile
import json
import time
import pymongo

def connectMongo():
    myclient = pymongo.MongoClient(os.environ.get("MONGO_CLIENT"))
    mydb = myclient["grid_fashion"]
    mycol = mydb["griddb"]
    return mycol

all_data = []
index = 0

archive = zipfile.ZipFile("C:/Users/HP/Downloads/styles.zip", 'r')
file_info_list = archive.infolist()
for file in file_info_list:
    opened_json = json.loads(archive.read(file))["data"]
    opened_json.pop("styleOptions")
    opened_json.pop("articleDisplayAttr")
    opened_json.pop("otherFlags")
    opened_json["image_url"] = opened_json["styleImages"].get("default",{"imageURL":""}).get("imageURL","")
    opened_json.pop("styleImages")
    opened_json.pop("crossLinks")
    all_data.append(opened_json)

    print("Appended ",index)
    index += 1 
archive.close()

col = connectMongo()
print("connected")
x = col.insert_many(all_data)
print("Done")