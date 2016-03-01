#!/usr/bin/python3
# Borja Egea Madrid

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
			print ('Waiting for connections')
			(recvSocket, address) = mySocket.accept()
			print ('HTTP request received (going to parse and process):')
			request = recvSocket.recv(2048)
			print (request)
			parsedRequest = self.parse(request)
			(returnCode, htmlAnswer) = self.process(parsedRequest)
			print ('Answering back...')
			recvSocket.send(bytes("HTTP/1.1 " + returnCode + " \r\n\r\n"
					+ htmlAnswer + "\r\n", 'utf-8'))
			recvSocket.close()

class sumadorApp(webApp):

	def parse(self, request):
		try:
			numero  = int(request.split()[1][1:])
			valido = True
		except ValueError:
			valido = False
			numero = 0
		return numero, valido

	def process(self, parsedRequest):
			numero, valido = parsedRequest
			if not valido:
				return ("200 OK", "<html><body><h1>Solo manejo enteros </h1></body></html>")
			if self.esPrimero:
				self.primer_num = numero
				self.esPrimero = False
				return ("200 OK", "<html><body><h1>Dame otro numero </h1></body></html>")

			else:
				segundo_num = numero
				suma = self.primer_num + segundo_num
				self.esPrimero = True
				return("HTTP/1.1 200 OK\r\n\r\n",
						"<html><body><h1>" + str(self.primer_num) + " + " + str(segundo_num) + " = " + str(suma)
						+ "</h1></body></html>" + "\r\n")



	def __init__(self,hostname, port):
			self.esPrimero = True
			super(sumadorApp, self).__init__(hostname,port)

if __name__ == "__main__":
	sumador = sumadorApp("localhost", 8080)
