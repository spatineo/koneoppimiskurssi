import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})

np.set_printoptions(precision=2)


def plot_confusion_matrix(cm, classes, names=None,
                          normalize=True, title='Sekaannusmatriisi'):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py
    """

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    rcParams.update({'figure.autolayout': True})
    import itertools
    cmap = plt.cm.Blues
    fig, ax = plt.subplots(figsize=(8, 4))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.set_title(title)
    ax.set_ylabel('True label')
    ax.set_xlabel('Predicted label')
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)
    if names:
        plt.yticks(tick_marks, names)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        ax.text(j, i, format(cm[i, j], fmt),
                horizontalalignment="center",
                color="white" if cm[i, j] > thresh else "black")
