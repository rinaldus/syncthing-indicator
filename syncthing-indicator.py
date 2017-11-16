#!/usr/bin/env python3

from syncthing import Syncthing
import urllib3
import configparser
urllib3.disable_warnings()

def isConnected():
    try:
        config = configparser.ConfigParser()
        config.read('config.conf')
        apikey = config['DEFAULT']['apikey']
        s = Syncthing(apikey)
        connections=s.system.connections()
        connected = {
            uuid:conn
            for uuid, conn in connections['connections'].items()
            if conn.get('connected')
        }
        if connected:
            return(True)
        else:
            return(False)
    except:
        return(None)
 
print (isConnected())
