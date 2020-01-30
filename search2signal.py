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
import zmq

IP = '127.0.0.1'
SERVER_PORT = 54414

client = udp_client.UDPClient(IP, CLIENT_PORT)


def oscReceive(unused_addr, bang):

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:54414")

    while True:

        print('Receive Number: ' + bang)

        annoy_model_path = 'model/x-fresh-flatten.ann'

        # search_img_path = 'dataset/export/export.png' # max msp
        search_img_path = 'dataDrivenArt/bin/data/export/export.png'  # openFrameworks

        print(search_img_path)
        # annoy_dim = 4096 # fc2を使った場合
        annoy_dim = 25088  # flattenを使った場合

        base_model = VGG16(weights="imagenet")
        # model = Model(inputs=base_model.input, outputs=base_model.get_layer("fc2").output)
        model = Model(inputs=base_model.input,
                      outputs=base_model.get_layer("flatten").output)

        loaded_model = AnnoyIndex(annoy_dim)
        loaded_model.load(annoy_model_path)

        img_path = search_img_path
        img = image.load_img(img_path, target_size=(224, 224))

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        # fc2_features = model.predict(x)
        flatten_features = model.predict(x)
        # items = loaded_model.get_nns_by_vector(fc2_features[0], 3, search_k=-1, include_distances=False)
        items = loaded_model.get_nns_by_vector(
            flatten_features[0], 3, search_k=-1, include_distances=False)
        print(items)

        backend.clear_session()

        print(items[0])
        print(items[1])
        print(items[2])
        print('images/' + str(items[0]) + '.jpg')
        print('images/' + str(items[1]) + '.jpg')
        print('images/' + str(items[2]) + '.jpg')

        path1 = items[0]
        path2 = items[1]
        path3 = items[2]

        socket.send_string(path1)
        socket.send_string(path2)
        socket.send_string(path3)

        print(f'Serving on {server.server_address}')
        break


dispatcher = Dispatcher()
dispatcher.map('/bang', oscReceive)

server = osc_server.ThreadingOSCUDPServer(
    (IP, SERVER_PORT), dispatcher)
print(f'Serving on {server.server_address}')
server.serve_forever()
