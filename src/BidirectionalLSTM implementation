import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split
from keras.layers import Bidirectional
from keras.utils.np_utils import to_categorical

df = pd.read_csv('data/new_combined.csv')
df = df[['checked spelling', 'polarity']]
df['checked spelling'] = df['checked spelling'].astype(str)

arr = np.array(df['polarity'].values.tolist())

for (x, item) in enumerate(arr):
    if item < 0:
        arr[x] = -1
    elif item > 0:
        arr[x] = 1
print(arr)

df['results'] = arr
#print(df['results'])


MAX_FEATURES = 2000
tokenizer = Tokenizer(num_words = MAX_FEATURES, split=' ')
tokenizer.fit_on_texts(df['checked spelling'].values)
X = tokenizer.texts_to_sequences(df['checked spelling'].values)
X = pad_sequences(X, maxlen = 300)
print(X)

EMBED_DIM = 128
LSTM_OUT = 196
EPOCHS = 20
BATCH_SIZE = 32

model = Sequential()
model.add(Embedding(MAX_FEATURES, EMBED_DIM, input_length = X.shape[1]))
model.add(SpatialDropout1D(0.3))
model.add(Bidirectional(LSTM(LSTM_OUT, dropout = 0.2, recurrent_dropout = 0.2)))
model.add(Dense(30, input_shape=(392,), activation = 'relu'))
model.add(Dense(3, activation ='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
print(model.summary())
print(X)

Y = pd.get_dummies(df['results']).values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state = 42)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

# accuracy and loss graph over epochs

model.fit(X_train, Y_train, epochs = EPOCHS, batch_size = BATCH_SIZE)

model.save_weights('model2.h5')
print("Saved model to disk")
