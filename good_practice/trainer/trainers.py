# Class to design the algorithm to train the network (needed for Pytorch)


class Trainer(object):

    def __init__(self, modelnet,
                 optimizer,
                 lossfun,
                 metrics=None,
                 callbacks=None):
        self.modelnet  = modelnet
        self.optimizer = optimizer
        self.lossfun   = lossfun
        self.metrics   = metrics
        self.callbacks = callbacks


    def _train_epoch(self):
        "Implement : the series of operations on training data on each epoch"

    def _validation_epoch(self):
        "Implement : the series of operations on validation data on each epoch"

    def _run_epoch(self):
        "Implement : the series of operations during one epoch of training (including train and validation data)"


    def train(self, train_data_generator,
              num_epochs= 1,
              max_steps_epoch= None,
              valid_data_generator= None,
              initial_epoch= 0):
        "Implement : the algorithm to train the network"


    def predict(self, test_data_generator):
        "Implement : compute prediction from trained model"


    def _run_callbacks(self):
        for callback in self.callbacks:
            callback()
        # endfor