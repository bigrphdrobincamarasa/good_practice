# Class to generate the neural network of choice


class Network(object):
    "Abstract class : with virtual functions to be overloaded"

    def __init__(self, size_image,
                 num_channels_in,
                 num_classes_out,
                 num_featmaps_in,
                 isUse_valid_convols=False):
        "Implement : constructor"
        self.size_image      = size_image
        self.num_channels_in = num_channels_in
        self.num_classes_out = num_classes_out
        self.num_featmaps_in = num_featmaps_in

        if isUse_valid_convols:
            # compute the output size from the series of layers in the designed network
            self.size_output = self.get_size_output_valid(self.size_image)
        else:
            self.size_output = self.size_image


    def get_size_input(self):
        return [self.num_channels_in] + list(self.size_image)

    def get_size_output(self):
        return [self.num_classes_out] + list(self.size_output)

    def preprocess(self, *args, **kwargs):
        "Implement : if needed, any operation prior to building the model (for tailored networks)"
        pass

    def get_size_output_valid(self, size_input):
        return NotImplemented

    def build_model(self):
        return NotImplemented



class Unet3D(Network):

    num_level_default = 5
    num_featmaps_in_default = 16

    def __init__(self, size_image,
                 num_levels=num_level_default,
                 num_channels_in=1,
                 num_classes_out=1,
                 num_featmaps_in=num_featmaps_in_default,
                 isUse_valid_convols=False):
        super(Unet3D, self).__init__(size_image,
                                     num_channels_in,
                                     num_classes_out,
                                     num_featmaps_in,
                                     isUse_valid_convols=isUse_valid_convols)
        # build model
        self.build_model()


    def get_size_output_valid(self, size_input):
        "Implement: obtain the output size from whichever input size, when using valid convolutions in the network"
        pass

    def build_model(self):
        #Implement: build network by putting together different layers: Convolutions, Poolings / Upsample, ...
        pass