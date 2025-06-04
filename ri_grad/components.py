import numpy as np

class Container:
    def __init__(self, width=40, height=25):
        self.width = width
        self.height = height

class Layer:
    def __init__(self, y_0, y_f, n):
        self.y_0 = y_0
        self.y_f = y_f
        self.n = n

class Medium:
    def __init__(
        self, 
        container: Container, 
        n_0: float = 1.0, 
        n_f: float = 1.5, 
        n_layers: int = 15, 
        color: str = 'blue'
        ):

        self.container = container
        self.n_0 = n_0
        self.n_f = n_f
        self.n_layers = n_layers
        self.color = color

        self.layer_thickness = self.container.height / self.n_layers
        self.layers = self._create_layer_list()
    
    def _create_layer_list(self):
        layer_list = []
        y_0 = 0
        y_f = self.container.height / self.n_layers

        for i in range(self.n_layers):
            layer_list.append(Layer(y_0, y_f, self.get_layer_ri(i)))
            y_0 += y_f
        
        return layer_list

    def get_layer_from_y(self, y):
        index = self.n_layers - (y // self.layer_thickness) - 1
        return self.layers[index] if index >= 0 else self.layers[0]
    
class Beam:
    def __init__(self, wavelength=550, angle=0, y_0=0):
        self.angle = angle
        self.wavelength = wavelength
        self.y_0

