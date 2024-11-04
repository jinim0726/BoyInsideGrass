# world[0]: background 객체
# world[1]: foreground 객체
world = [[],[]]

def add_object(o, depth):
    world[depth].append(o)

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    print(f'CRITICAL: delete {o} is none')