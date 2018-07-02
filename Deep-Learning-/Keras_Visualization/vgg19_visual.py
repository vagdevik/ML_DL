# https://machinelearningmastery.com/visualize-deep-learning-neural-network-model-keras/

from keras.applications.vgg19 import VGG19
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.vis_utils import plot_model
model = VGG19()
plot_model(model, to_file='vgg19_plot.png', show_shapes=True, show_layer_names=True)
