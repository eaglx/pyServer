#!/usr/bin/python2

import socket
import json
import struct
import os

CRYTOP_HOST = '127.0.0.1'

HOST = CRYTOP_HOST  # The remote host
PORT = 50008

class rpc(object):
    def __init__(self):
        self.s = None

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))
    
    def disconnect(self):
        self.s.close()

    def __getattr__(self, name):	#Prevent AttributeError
	    def worker(*args):
	        self.connect()
	        
	        d = {
	            "func": name,
	            "argv": list(args)
	            }
	        d = json.dumps(d)
	        
	        self.s.sendall(struct.pack("<I", len(d)))
	        self.s.sendall(d)

	        data = self.s.recv(4)
	        if not data:
	            self.disconnect()
	            return

	        data_len = struct.unpack("<I", data)[0]
	        
	        data = self.s.recv(data_len)
	        if not data:
	            self.disconnect()
	            return
	        if data_len != len(data):
	            print "Error!"
	            os.exit(1)

	        self.disconnect()

	        data = json.loads(data)
	        return data

	    return worker

r = rpc()
print r.add(1, 2)
print r.add(0, 3)
print r.test()
