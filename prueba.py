from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://snovap:VB3D5fi1xHQ6YNzP@nosqljosuemanrique.om5b7lb.mongodb.net/?retryWrites=true&w=majority&appName=NOSQLjosuemanrique"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)