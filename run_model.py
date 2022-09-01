import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd





model = tf.keras.models.load_model('model.h5',custom_objects={'KerasLayer':hub.KerasLayer})

df = pd.read_csv('test.csv', encoding= 'unicode_escape')

df = df[['title']]
test = df['title'].values


def predict():
    prediction = model.predict(test)
    
    return prediction

print(predict())