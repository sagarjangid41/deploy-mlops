import os 
from keras.datasets import mnist
from keras.optimizers import RMSprop
dataset = mnist.load_data('mymnist.db')
train , test = dataset
X_train , y_train = train
X_test , y_test = test
X_train_1d = X_train.reshape(-1 , 28*28)
X_test_1d = X_test.reshape(-1 , 28*28)
X_train = X_train_1d.astype('float32')
X_test = X_test_1d.astype('float32')
from keras.utils.np_utils import to_categorical
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

from keras.layers import Dense
from keras.models import Sequential
model = Sequential()
model.add(Dense(units=512, input_dim=28*28, activation='relu'))
model.add(Dense(units=256, activation='relu'))
model.add(Dense(units=100, activation='relu'))
#1()

model.add(Dense(units=10, activation='softmax'))

from keras.optimizers import RMSprop
model.compile(optimizer=RMSprop(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
h = model.fit(X_train, y_train_cat,validation_data=(X_test, y_test_cat), epochs=5, verbose=0)
scores = model.evaluate(X_test, y_test_cat, verbose=0)
print("Accuracy:  %.2f%%" % (scores[1]*100))
a = 90

if scores[1]*100 > a:
    os.system(cmd)
    print("Sending the report to the target User through mail")
    model.save('bestaccuracymodel.h5')
    file1 = open("cnn_resultbestaccuracy.txt","w+")
    file1.write(str(scores[1]*100))
    file1.close()
else:
    print("Accuracy:  %.2f%%" % (scores[1]*100))
    print("Your Accuracy is very low. You have to tweak your model")
    
    file1 = open("cnn_resultlowaccuracy.txt","w+")
    file1.write(str(scores[1]*100))
    file1.close()
