import matplotlib.pyplot as plt
% matplotlib inline


class circle(object):
    def __init__(self, radius, color="blue"):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)

    def drawcircle(self):
        plt.gca().add_patch(plt.circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()


RedCircle = circle(10, 'red')
RedCircle.drawcircle()