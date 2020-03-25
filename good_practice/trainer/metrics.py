# Class to compute different metrics (also used as losses)


class Metrics(object):
    "Abstract class : with virtual functions to be overloaded"

    def __init__(self):
        "Implement : constructor"
        pass

    def loss(self, y_true, y_pred):
        return NotImplemented

    def compute(self, y_true, y_pred):
        return NotImplemented


class MeanSquared(Metrics):

    def __init__(self):
        "Implement : constructor"
        super(MeanSquared, self).__init__()
        pass

    def compute(self, y_true, y_pred):
        "Implement : compute Mean Squared Error"

    def loss(self, y_true, y_pred):
        "Implement : when using as loss function"
        return self.compute(y_true, y_pred)


class BinaryCrossEntropy(Metrics):

    def __init__(self):
        "Implement : constructor"
        super(BinaryCrossEntropy, self).__init__()
        pass

    def compute(self, y_true, y_pred):
        "Implement : compute Binary Cross Entropy"

    def loss(self, y_true, y_pred):
        "Implement : when using as loss function"
        return self.compute(y_true, y_pred)


class DiceCoefficient(Metrics):

    def __init__(self):
        "Implement : constructor"
        super(DiceCoefficient, self).__init__()
        pass

    def compute(self, y_true, y_pred):
        "Implement : compute Dice coefficient"

    def loss(self, y_true, y_pred):
        "Implement : when using as loss function"
        return 1.0 - self.compute(y_true, y_pred)