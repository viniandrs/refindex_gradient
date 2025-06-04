import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple
from ri_grad.components import Container
from ri_grad.medium import Medium

class Geometry:
    def __init__(self, container: Container, medium: Medium):
        self.container = container
        self.medium = medium

        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax

        self._container_drawn = False

    def render_container(self):
        plt.figure(self.fig.number)
        ax = self.ax

        ax.set_xlim(0, self.container.width)
        ax.set_ylim(0, self.container.height)
        ax.set_aspect('equal')

        # Remove top and right spines to resemble an aquarium
        ax.spines['top'].set_visible(False)

        # Keep only the bottom and left spines
        ax.spines['left'].set_color('black')
        ax.spines['right'].set_color('black')
        ax.spines['bottom'].set_color('black')

        # Remove ticks
        ax.set_xticks([])

        self._container_drawn = True

    def render_medium(self):
        if not self._container_drawn:
            self.render_container()

        ax = self.ax
        n_layers = self.medium.n_layers

        # Generate a linear light to dark blue gradient
        gradient = np.linspace(.3, 1, n_layers)[::-1]
        colors = plt.cm.Blues(gradient)

        # Draw the layers with the generated colors
        ax = self.ax
        for i in range(n_layers):
            layer_height = i * (self.container.height / n_layers)
            ax.fill_between(
                [0, self.container.width], 
                layer_height, 
                layer_height + (self.container.height / self.medium.n_layers), 
                color=colors[i], 
                alpha=0.5
            )

    def beamOn(self, beam: Beam):
        plt.figure(self.fig.number)
        ax = self.ax
        n_layers = n_layers
        
        incidence_points: List[Tuple[float]] = []
        incidence_angle = beam.angle
        incidence_point = [0, beam.y_0]

        incidence_points.append((*incidence_point, incidence_angle))
        for i in range(self.medium.n_layers):
            next_angle = np.arcsin(
                (self.medium.get_layer_n(i) / self.medium.get_layer_n(i + 1)) * np.sin(incidence_angle)
            )
            next_point = [incidence_point[0], incidence_point[1] + (self.container.height / self.medium.n_layers)]


    def show(self):
        plt.figure(self.fig.number)
        plt.show()