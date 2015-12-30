import re


def split_response(response):
    response = response[2:-3].replace('\"title":\"', '')
    response = re.split('"},{', response)
    return response

