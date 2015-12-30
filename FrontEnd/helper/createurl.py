from FrontEnd.constants.frontendconstants import *

def createurl(type, id):
    if type == 'channel':
        endpoint='/list?channelId='
    elif type == 'video':
        endpoint='/detail?videoId='
    else:
        endpoint=''
        id=''

    return "{0}{1}:{2}{3}{4}".format(PROTOCOL,HOST, PORT, endpoint, id)