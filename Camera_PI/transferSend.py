import socket

#add flag for read from file and add multiple lines
UPD_IP = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]

UDP_PORT = 5005

f = open('send_data.txt' , 'r')

# REad only one line
MESSAGE = f.readline()

f.close()


print "UDP target IP:", UDP_IP

print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet

socket.SOCK_DGRAM) # UDP

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

#Reference:
#http://www.mrhobbytronics.com/raspberry-pi-communicating-between-pis/
#**************************************************************************************/
