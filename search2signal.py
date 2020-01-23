import os
import numpy as np
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, VGG16
from keras.models import Model
from keras.backend import tensorflow_backend as backend
from annoy import AnnoyIndex

# server
from pythonosc import osc_server
from pythonosc.dispatcher import Dispatcher

# client
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

IP = '127.0.0.1'
SERVER_PORT = 54414
CLIENT_PORT = 54415

client = udp_client.UDPClient(IP, CLIENT_PORT)


def oscReceive(unused_addr, bang):

    while True:

        if bang == 'finish':
            print('Receive Number: ' + bang)
            break

        print('Receive Number: ' + bang)

        annoy_model_path = 'model/x-fresh.ann'

        # search_img_path = 'dataset/export/export.png' # max msp
        search_img_path = 'dataDrivenArt/bin/data/export/export.png'  # openFrameworks

        print(search_img_path)
        annoy_dim = 4096

        base_model = VGG16(weights="imagenet")
        model = Model(inputs=base_model.input,
                      outputs=base_model.get_layer("fc2").output)

        loaded_model = AnnoyIndex(annoy_dim)
        loaded_model.load(annoy_model_path)

        img_path = search_img_path
        img = image.load_img(img_path, target_size=(224, 224))

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        fc2_features = model.predict(x)
        items = loaded_model.get_nns_by_vector(
            fc2_features[0], 3, search_k=-1, include_distances=False)
        print(items)
        print(items[0])

        msg = OscMessageBuilder(address='/image')

        msg.add_arg(items[0])
        print(items[0])
        print('images/' + str(items[0]) + '.jpg')

        m = msg.build()
        client.send(m)

        backend.clear_session()
        print(f'Serving on {server.server_address}')
        break


dispatcher = Dispatcher()
dispatcher.map('/bang', oscReceive)

server = osc_server.ThreadingOSCUDPServer(
    (IP, SERVER_PORT), dispatcher)
print(f'Serving on {server.server_address}')
server.serve_forever()
