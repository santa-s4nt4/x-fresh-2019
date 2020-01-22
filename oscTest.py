# server
from pythonosc import osc_server
from pythonosc.dispatcher import Dispatcher

# client
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

IP = '127.0.0.1'
SERVER_PORT = 54410
CLIENT_PORT = 54411

client = udp_client.UDPClient(IP, CLIENT_PORT)


def oscReceive(unused_addr, bang):
    print('Receive Number: ' + bang)
    msg = OscMessageBuilder(address='/')
    msg.add_arg('is genius.')

    m = msg.build()
    client.send(m)


dispatcher = Dispatcher()
dispatcher.map('/bang', oscReceive)

server = osc_server.ThreadingOSCUDPServer((IP, SERVER_PORT), dispatcher)
print(f'Serving on {server.server_address}')
server.serve_forever()
