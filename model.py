import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd


df = pd.read_csv('data.csv', encoding= 'unicode_escape')

df = df[['title','unbias']]

train = df.sample(frac=0.8) 
test = df.drop(train.index)

train_examples, train_labels = train['title'].values, train['unbias'].values
test_examples, test_labels = test['title'].values, test['unbias'].values

import os
os.environ['TFHUB_CACHE_DIR'] = r'C:\Users\Arkhaya\Documents\GitHub\Unbaised-news-application'

model = "https://tfhub.dev/google/nnlm-en-dim128-with-normalization/2"
hub_layer = hub.KerasLayer(model, input_shape=[], dtype=tf.string, trainable=True)

hub_layer(train_examples[0:1])

model = tf.keras.Sequential()
model.add(hub_layer) # add tokenization layer
model.add(tf.keras.layers.Dense(16, activation='relu')) # create hidden layer with 16 nodes
model.add(tf.keras.layers.Dense(8, activation='relu')) # create hidden layer with 8 nodes
model.add(tf.keras.layers.Dense(1, activation='sigmoid')) # output layer, 1 node, sigmoid, for binary classification
model.summary()

model.compile(optimizer='adam',
              loss=tf.losses.BinaryCrossentropy(from_logits=True),
              metrics=[tf.metrics.BinaryAccuracy(threshold=0.5, name='accuracy')])

x_val = train_examples[:10]
partial_x_train = train_examples[10:]

y_val = train_labels[:10]
partial_y_train = train_labels[10:]

print(len(x_val), len(partial_x_train))

history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=10,
                    batch_size=40,
                    validation_data=(x_val, y_val),
                    verbose=1)

model.save("model.h5")

results = model.evaluate(test_examples, test_labels)
print(results)



