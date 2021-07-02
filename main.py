from data_config import *
from elasticsearch import Elasticsearch



def create_record():
    record={"name": "John", "nickname": "Jo" }
    record.update({"age": 30, "category": "Food", "txn_type": "DR", "amount": 24.50, "currency": "GBP", "email": "example@example.com" })
    return record


''' create connection to Elasticsearch'''
try:
    elastic = Elasticsearch([es_host],http_auth=(es_user, es_password),use_ssl=True,verify_certs=False)
except Exception as error:
    print ("Elasticsearch Client Error:", error)
    exit

record=create_record()
response = elastic.index(index='employees', doc_type='person', body=record)