import numpy as np
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, VGG16
from keras.models import Model
base_model = VGG16(weights='imagenet')
base_model.summary()

print(base_model.input)
print(base_model.output)

img_path = 'dataset/test/Ukiyo_e/utagawa-kunisada_the-actor-ichikawa-kodanji-iv-as-subashiri-no-kumagoro-1859.jpg'

img = image.load_img(img_path, target_size=(224, 224))
input = image.img_to_array(img)
result = base_model.predict(np.array([input]))
print("配列の中身", result)
print("配列の長さ: ", len(result[0]))

model = Model(inputs=base_model.input,
              outputs=base_model.get_layer("fc2").output)
print(model.input)
print(model.output)

img_path = 'dataset/test/Ukiyo_e/utagawa-kunisada_the-actor-ichikawa-kodanji-iv-as-subashiri-no-kumagoro-1859.jpg'
img = image.load_img(img_path, target_size=(224, 224))
input = image.img_to_array(img)
result = model.predict(np.array([input]))
print("実際の値", result)
print("配列の長さ: ", len(result[0]))

'''
画像類似度の計算手順
- 1000枚分のベクトルをどこかしらに保存
- 入力画像を『関数』でベクトルに変換
- 得られたベクトルとの類似度を1000枚分計算
- 類似度の値が小さい順に結果として返す
'''
