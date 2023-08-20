from flask import Flask, request, jsonify
from bson import json_util
import json
import pymongo
import requests
import numpy as np
import pandas as pd
import pinecone
import time
from sentence_transformers import SentenceTransformer

# model = SentenceTransformer('sentence-transformers/all-distilroberta-v1')
# pinecone.init(api_key="01a99633-0c29-4ff8-a8f0-e713b8ccc63c", environment="us-west1-gcp-free")
# index = pinecone.Index("grid-hax-final")

app = Flask(__name__)


# def vectorSearch(inputQuery, k=3):
#     resultant_list = []
#     qa_vector = model.encode(inputQuery).tolist()
#     results = index.query(
#       vector=qa_vector,
#       top_k=k,
#       include_values=True
#     )
#     for i in range(k):
#         resultant_list.append(results['matches'][i]['id'])
#     return resultant_list

def connectMongo():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["grid_fashion"]
    mycol = mydb["griddb"]
    return mycol

# @app.route("/")
# def health():
#     return "OK"


# @app.route("/getData",methods=["POST"])
# def getData():
#     prompt = request.json["prompt"]
#     resp = requests.post("https://b327-35-185-158-27.ngrok-free.app/chatbot",json={"prompt":prompt})
#     all_ids=[]
#     resp = resp.json()
#     print(resp)
#     for tag in resp["data"]:
#         ids = vectorSearch(inputQuery=tag)
#         all_ids += ids  
#     col = connectMongo()
#     complete_data=[]
#     for id in all_ids:
#         doc = col.find_one({"id":int(id)})
#         # print(doc)
#         doc.pop('_id')
#         complete_data.append(doc)
#     response_data = {
#         "data": complete_data
#     }
#     return response_data


# @app.route("/dbData",methods=["POST"])
# def dbData():
#     resp = ["saree","sherwani"]
#     all_ids=[]
#     print(resp)
#     for tag in resp:
#         ids = vectorSearch(inputQuery=tag)
#         all_ids += ids  
#     print(all_ids)
#     col = connectMongo()
#     complete_data=[]
#     for id in all_ids:
#         doc = col.find_one({"id":int(id)})
#         # print(doc)
#         doc.pop('_id')
#         complete_data.append(doc)
#     response_data = {
#         "data": complete_data
#     }
#     return response_data


@app.route("/byGender",methods=["POST"])
def getbyGender():
    data = request.json
    limitnum = data.get("limit")
    if not limitnum:
        limitnum = 100;
    col = connectMongo()
    complete_data=[]
    gender = data["gender"].lower().capitalize()
    print(data)
    resp = col.find({"gender":gender}).limit(limitnum)
    for doc in resp:
        doc.pop('_id')
        complete_data.append(doc)
    response_data = {
        "data": complete_data
    }
    return response_data


@app.route("/byColor",methods=["POST"])
def getbyColor():
    data = request.json
    limitnum = data.get("limit")
    if not limitnum:
        limitnum = 100
    col = connectMongo()
    complete_data=[]
    color = data["color"].lower().capitalize()
    print(data)
    resp = col.find({"baseColour":color}).limit(limitnum)
    for doc in resp:
        doc.pop('_id')
        complete_data.append(doc)
    response_data = {
        "data": complete_data
    }
    return response_data


@app.route("/byBrand",methods=["POST"])
def getbyBrand():
    data = request.json
    limitnum = data.get("limit")
    if not limitnum:
        limitnum = 100
    col = connectMongo()
    complete_data=[]
    brand = data["brand"]
    print(data)
    resp = col.find({"brandName":brand}).limit(limitnum)
    for doc in resp:
        doc.pop('_id')
        complete_data.append(doc)
    response_data = {
        "data": complete_data
    }
    return response_data



if __name__ == '__main__':
    app.run(debug=True)

