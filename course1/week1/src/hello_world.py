import keras
import numpy as np

NUM_EPOCHS = 500

if __name__ == "__main__":
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer="sgd", loss="mean_squared_error")

    xs = np.array([-1, 0, 1, 2, 3, 4], dtype=int)
    ys = np.array([-3, -1, 1, 3, 5, 7], dtype=int)

    model.fit(xs, ys, epochs=NUM_EPOCHS)

    print(model.predict([10]))
