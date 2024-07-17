from pymongo import MongoClient

link=MongoClient("")
db=link.tokengenerate
col=db.col