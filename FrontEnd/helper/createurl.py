from FrontEnd.constants.frontendconstants import *

def createurl(type, id):
    if type == CHANNEL:
        endpoint=CHANNELAPIENDPOINT
    elif type == VIDEO:
        endpoint=VIDEOAPIENDPOINT
    else:
        endpoint=''
        id=''

    return "{0}{1}:{2}{3}{4}".format(PROTOCOL,HOST, PORT, endpoint, id)