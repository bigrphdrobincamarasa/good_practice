# Class to generate an iterator to create random data batches from loaded data


class BatchDataGenerator(object):

    def __init__(self):
        "Implement : constructor"
        pass

    def __len__(self):
        "Implement : return the number of batches per epoch"
        pass

    def on_epoch_end(self):
        "Implement : update indexes of random batches after each epoch"
        pass

    def __getitem__(self, index):
        "Implement : generate and return one batch of data"
        pass