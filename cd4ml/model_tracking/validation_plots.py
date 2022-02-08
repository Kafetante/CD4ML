import itertools
from tempfile import NamedTemporaryFile

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from bokeh.plotting import figure, output_file


def get_validation_plot(true_value, prediction):
    output_file(NamedTemporaryFile().name)
    x_min = min(min(true_value), min(prediction))
    x_max = max(max(true_value), max(prediction))

    x_range = [x_min, x_max]
    y_range = x_range

    plot = figure(width=800, height=800,
                  x_range=x_range, y_range=y_range)

    plot.xaxis.axis_label = "True value"
    plot.xaxis.axis_label_text_font_size = '14pt'
    plot.xaxis.major_label_text_font_size = '12pt'

    plot.yaxis.axis_label = "Prediction"
    plot.yaxis.axis_label_text_font_size = '14pt'
    plot.yaxis.major_label_text_font_size = '12pt'

    plot.circle(true_value, prediction)

    plot.line(x_range, y_range, line_dash='dashed', color='gray')
    return plot


def get_confusion_matrix_plot(confusion_matrix,
                              target_names,
                              title='Confusion matrix',
                              cmap=None,
                              normalize=True):
    """
    given a sklearn confusion matrix (cm), make a nice plot

    Arguments
    ---------
    confusion_matrix:           confusion matrix from sklearn.metrics.confusion_matrix

    target_names: given classification classes such as [0, 1, 2]
                  the class names, for example: ['high', 'medium', 'low']

    title:        the text to display at the top of the matrix

    cmap:         the gradient of the values displayed from matplotlib.pyplot.cm
                  see http://matplotlib.org/examples/color/colormaps_reference.html
                  plt.get_cmap('jet') or plt.cm.Blues

    normalize:    If False, plot the raw numbers
                  If True, plot the proportions

    Usage
    -----
    plot_confusion_matrix(cm           = cm,                  # confusion matrix created by
                                                              # sklearn.metrics.confusion_matrix
                          normalize    = True,                # show proportions
                          target_names = y_labels_vals,       # list of names of the classes
                          title        = best_estimator_name) # title of graph

    Citiation
    ---------
    http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html

    """
    if normalize:
        confusion_matrix = confusion_matrix.astype('float') / confusion_matrix.sum()
    accuracy = np.trace(confusion_matrix) / np.sum(confusion_matrix).astype('float')
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(8, 8))
    plt.imshow(confusion_matrix, interpolation='nearest', cmap=cmap, vmin=0, vmax=1)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    matplotlib.rcParams.update({'font.size': 20})
    thresh = confusion_matrix.max() / 1.5 if normalize else confusion_matrix.max() / 2
    for i, j in itertools.product(range(confusion_matrix.shape[0]), range(confusion_matrix.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(confusion_matrix[i, j]),
                     horizontalalignment="center",
                     color="white" if confusion_matrix[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(confusion_matrix[i, j]),
                     horizontalalignment="center",
                     color="white" if confusion_matrix[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label', fontsize=16)
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass), fontsize=16)
    return plt
