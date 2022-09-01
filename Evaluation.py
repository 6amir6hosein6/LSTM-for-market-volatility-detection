import matplotlib.pyplot as plt


def evaluation(history):
    plt.plot(history.history['mean_absolute_error'])
    plt.plot(history.history['root_mean_squared_error'])
    plt.title('model performance')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['mean_absolute_error', 'root_mean_squared_error'], loc='upper right')
    plt.show()


def resulting(history):
    pass
