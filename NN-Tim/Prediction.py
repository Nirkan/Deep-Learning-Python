# Import packages

import tensorflow as tf 
from tensorflow import keras 
import numpy as np
import matplotlib.pyplot as plt 

data = keras.datasets.fashion_mnist

(train_images, train_labels),(test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


# Schrunk down the data to between 0 and 1

train_images = train_images / 255.0
test_images  = test_images  / 255.0

print(train_images[7])


# Model training and fitting

model = keras.Sequential([
	keras.layers.Flatten(input_shape = (28,28)),
	keras.layers.Dense(128, activation = "relu"),
	keras.layers.Dense(10, activation= "softmax")
])


model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics = ["accuracy"])

model.fit(train_images, train_labels, epochs = 10)


## Make predictions using model

prediction = model.predict(test_images)


# Show both input and output as we loop throught different images
# We plot the input and prediction and see input and output together

for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap = plt.cm.binary)
    plt.xlabel("Actual : "+ class_names[test_labels[i]])
    plt.title("Prediction : " + class_names[np.argmax(prediction[i])])
    plt.show()

#prints all the outputs (np.argmax will print only maximum)

#print(class_names[np.argmax(prediction[0])])  