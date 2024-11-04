objects = [[],[],[]]

# layer 0: Background Objects
# layer 1: Foreground Objects

def add_object(o, depth = 0):
    objects[depth].append(o)
def add_objects(ol, depth = 0):
    objects[depth] += ol
def remove_object(o):
     for layer in objects:
         if o in layer:
             layer.remove(o)
             return #
     raise ValueError('Cannot delete non existing object')


def update():
    for layer in objects:
         for o in layer:
             o.update()
def render():
    for layer in objects:
        for o in layer:
             o.draw()