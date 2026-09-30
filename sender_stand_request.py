
import configuration

import requests

import data 



def post_new_order(body):
   
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, 
                         json=body)


def get_new_order_track():
    response = post_new_order(data.order_body)
    return response.json()["track"]


def get_order_by_track(track):
    response = requests.get(configuration.URL_SERVICE + f"{configuration.ORDER_BY_TRACK}{track}")
    return response

