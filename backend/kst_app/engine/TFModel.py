import tensorflow as tf

model = tf.keras.Model


def load_model():
    global model
    model = tf.keras.models.load_model('model1h.h5')


def save_model():
    model.save('model1h.h5')
    tf.keras.backend.clear_session()