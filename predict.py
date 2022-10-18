import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import numpy as np

class Predict():
    def __init__(self):
        self.model = tf.keras.models.load_model('model1.h5')
        self.scale = MinMaxScaler(feature_range=(0,1))

    def preprocess(self, input):
        input = self.scale.fit_transform(input.head(30).iloc[:, 4:5])
        input = np.array(input)
        input_last = np.reshape(input, (input.shape[1], input.shape[0], 1))
        return input_last

    def predict_stock(self, data):
        model_input = self.preprocess(data)
        model_output = self.model.predict(model_input)
        stock_pred = self.scale.inverse_transform(model_output)[0][0].round(2)
        return stock_pred