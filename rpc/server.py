#!/usr/bin/python2

import socket
import struct
import os
import json

def rpc_add(a, b):
    return a + b

def rpc_sub(a, b):
    return a - b

rpc_functions = {
        "add": {
            "argv": [int, int],
            "f": rpc_add
        },
        "sub": {
            "argv": [int, int],
            "f": rpc_sub
        }
}

CRYTOP_HOST = '127.0.0.1'

HOST = CRYTOP_HOST  # Symbolic name meaning all available interfaces
PORT = 50008        # Arbitary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #TCP
s.bind((HOST, PORT))
s.listen(1)

while True:
	try: 
		conn, addr = s.accept()
		print 'Connected by ', addr
	   
		data = conn.recv(4)
		if not data:
		    conn.close()
		    continue

		data_len = struct.unpack("<I", data)[0]
	   
		data = conn.recv(data_len)
		if not data:
		    conn.close()
		    continue
		if data_len !=  len(data):
		    print "*** Data length problem! ***"
		    conn.close()
		    os.exit(1)

		data = json.loads(data)
		print data

		remote_name = data["func"]
		remote_args = tuple(data["argv"])

		if remote_name not in rpc_functions:
		    print "There isn't function: ", remote_name
		    conn.close()
		    continue

		func = rpc_functions[remote_name]
		for arg_type, remote_arg in zip(func["argv"], remote_args):
		    if type(remote_arg) is not arg_type:
		        print "Incorrect arg type ", arg_type, type(remote_arg)
		        conn.close()
		        continue

		print "Calling ", remote_name, remote_args
		ret = func["f"](*remote_args)   #(*(1,2)) == (1,2)
		print ret
		ret = json.dumps(ret)

		conn.sendall(struct.pack("<I", len(ret)))	# Little endian
		conn.sendall(ret)
		conn.close()
	except KeyboardInterrupt:
		print "\nKeyboardInterrupt, server closed."
		conn.close()
		sys.exit()
