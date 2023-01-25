import tensorflow as tf

def create_clean_model_hour():
    input_rec = tf.keras.layers.Input((24, 150))
    norm = tf.keras.layers.Normalization()(input_rec)
    LSTM1 = tf.keras.layers.LSTM(800, return_sequences=True)(norm)
    LSTM2 = tf.keras.layers.LSTM(800, dropout=.1)(LSTM1)

    inputs_aux = tf.keras.layers.Input((24, 10))
    flatten = tf.keras.layers.Flatten()(inputs_aux)
    pre_preprocess = tf.keras.layers.Dense(256, activation='elu', kernel_regularizer='l2')(flatten)
    pre_preprocess = tf.keras.layers.Dense(256, activation='elu', kernel_regularizer='l2')(pre_preprocess)
    preprocess = tf.keras.layers.Dense(128, activation='elu', kernel_regularizer='l2')(pre_preprocess)

    combine = tf.keras.layers.Concatenate()([preprocess, LSTM2])
    broad_layer = tf.keras.layers.Dense(300, activation='elu', kernel_regularizer='l2')(combine)
    out = tf.keras.layers.Dense(150, activation='linear')(broad_layer)

    model = tf.keras.Model([input_rec, inputs_aux], out)
    model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), metrics=['mse'])

    return model