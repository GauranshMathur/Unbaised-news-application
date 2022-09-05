import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd
import csv





model = tf.keras.models.load_model('model.h5',custom_objects={'KerasLayer':hub.KerasLayer})

df = pd.read_csv('test.csv', encoding= 'unicode_escape',skip_blank_lines=True).dropna()

df = df[['title']]
test = df['title'].values


prediction = model.predict(test)

f = open('final.csv', 'w')
writer = csv.writer(f)

for i,j in prediction,test:
    writer.writerow(prediction[i], test[j])
    
f.close()

 

