import socket

#add write flag to file

UDP_IP = "10.0.0.228"

UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

f = open("receive_data.txt","w") #opens file with name of "trial.txt"

while True:

	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	
	print "received message:", data # prints to console

	f.write(data) # writes to file

f.close()
