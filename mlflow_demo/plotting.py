import numpy as np
from plotly import graph_objs as go
from sklearn.metrics import confusion_matrix


def create_confusion_matrix_fig(labels, labels_pred, colorscale='Greens'):
    """
    Create a confusion matrix figure with Plotly
    Args:
        labels (numpy.array): Real labels
        labels_pred (numpy.array): Prediction labels
        colorscale: Plotly color scale to use
    Returns:
        dict: Plotly figure spec
    """
    cm = confusion_matrix(labels, labels_pred)
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    labels_unq = ["class " + str(label) if not isinstance(label, str) else label for label in np.unique(labels)]
    data = [
        go.Heatmap(x=labels_unq[::-1], y=labels_unq, z=cm[::-1], colorscale=colorscale, reversescale=True)
    ]
    layout = dict(
        width=1000, height=1000,
        title="Confusion Matrix"
    )
    return go.Figure(data=data, layout=layout)