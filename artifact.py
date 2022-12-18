from game.casting.actor. import Actor
def _init_(self):
    Super()._init_()


def calculate_points(self):
    points=0
    if (self.get_text()='*'):
        points=1
    else:
        points=-1
    return points            