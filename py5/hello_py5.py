#
# hello_py5.py
#

# This is the "module" mode hello program.
# https://py5coding.org/content/py5_modes.html


import py5

def setup():
    py5.size(300, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

py5.run_sketch()
