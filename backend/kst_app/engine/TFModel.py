import tensorflow as tf

model = tf.keras.Model


def load_model():
    global model
    model = tf.keras.models.load_model('model1h.h5')


def save_model():
    model.save('model1h.h5')
    tf.keras.backend.clear_session()


def load_gustaw():
    def alst_time_step_mse(Y_true, Y_pred):
        return tf.keras.metrics.mean_squared_error(Y_true[:, -1], Y_pred[:, -1])

    return tf.keras.models.load_model('gustaw.h5',custom_objects={"alst_time_step_mse": alst_time_step_mse})


def save_gustaw(gustaw: tf.keras.Model):
    gustaw.save('gustaw.h5')
    tf.keras.backend.clear_session()
