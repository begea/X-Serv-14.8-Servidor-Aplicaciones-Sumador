#!/usr/bin/python

import socket

class webApp:

	def parse(self, request):
		return None

	def process(self, parsedRequest):
		return ("200 OK", "<html><body><h1>It works!</h1></body></html>")

	def __init__(self, hostname, port):

		# Create a TCP objet socket and bind it to a port
		mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		mySocket.bind((hostname, port))
	
		# Queue a maximum of 5 TCP connection requests
		mySocket.listen(5)
	
		# Accept connections, read incoming data, and call
		# parse and process methods (in a loop)
		
		primer = None
		while True:
			print 'Waiting for connections'
			(recvSocket, address) = mySocket.accept()
			print 'HTTP request received (going to parse and process):'
			request = recvSocket.recv(2048)
			print request
			parsedRequest = self.parse(request)
			(returnCode, htmlAnswer) = self.process(parsedRequest)
			print 'Answering back...'
			recvSocket.send("HTTP/1.1 " + returnCode + " \r\n\r\n"
					+ htmlAnswer + "\r\n")
	
class sumadorApp(webApp):
	
	def parse(self, request):
		return numero
	
	def process(self, parsedRequest):
			suma = None		
			primer = None

	def process(self, parsedRequest, primer):

			if primer == None:
				primer = parsedRequest
				return ("200 OK", "<html><body><h1>Dame otro numero </h1></body></html>")
	
			else:
				num = parsedRequest
				try:
					suma = int(primer) + int(num)	
					return("HTTP/1.1 200 OK\r\n\r\n" +
							"<html><body><h1>" + str(primer) + " + " + str(num) + " = " + str(suma) 
							+ "</h1></body></html>" + "\r\n")
	
					primer = None			

				except ValueError:
					return("HTTP/1.1 400 Error..\r\n\r\n" +
							"<html><body><h1>No podemos sumar enteros y caracteres</h1></body></html>"
							+"\r\n")

					primer = None

if __name__ == "__main__":
	sumador = sumadorApp("localhost", 8080)
