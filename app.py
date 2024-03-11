import pyglet
from pyglet.window import key



window = pyglet.window.Window()




@window.event
def on_draw():
    window.clear()



@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('A key was pressed')

if __name__ == '__main__':
    pyglet.app.run()
