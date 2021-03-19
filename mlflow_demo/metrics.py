class Scorer:
    def __init__(self, **metric_functions):
        self.metric_functions = metric_functions
        self.y_ = []
        self.y_pred_ = []

    def copy(self):
        return Scorer(**self.metric_functions)

    def __call__(self, estimator, X, y):
        y_pred = estimator.predict(X)
        self.y_.extend(y)
        self.y_pred_.extend(y_pred)
        return {
            metric_name: metric_function(y, y_pred)
            for metric_name, metric_function in self.metric_functions.items()
        }
