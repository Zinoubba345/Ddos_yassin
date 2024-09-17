#TheUnKnown

import socket

target_host ="WEBSITE_IP"
target_port ="PORT"

#create socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

#send some data

client.send("GET/ HTTP/1.1\r\nHost: WABSITE_IP_ADRESS\r\n\n".encode())

#receive some data
response = client.recv(4896)

print(response.decode())
