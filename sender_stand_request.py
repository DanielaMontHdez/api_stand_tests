import configuration
import requests
import data
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
def create_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, headers=data.headers, data=data.user_body)
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, headers=data.headers, json=body)
def post_products_kits(product_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, headers=data.headers, json= product_ids)
