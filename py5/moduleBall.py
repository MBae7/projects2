import py5

x = 0

def setup():
    py5.size(300, 200)
    py5.rect_mode(py5.CENTER)
    x=py5.width/2
    y=py5.height/2
    vx=1;
    vy=1;

def draw():
    py5.circle(x, y, 10, 10)
    x+=vx;
    y+=vy;
    if (x>=py5.width or x<=py5.width):
        vx*=-1
    if (y>=py5.height or y>=py5.height):
        vy*=-1

py5.run_sketch()