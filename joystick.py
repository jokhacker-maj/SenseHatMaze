from sense_hat import SenseHat
import maze
import time
sense = SenseHat()
coordinate = [0,0]


def draw(mesh, color):
    for y in range(0, 8):
        for x in range(0, 8):
            if mesh[y , x] == 1:
                sense.set_pixel(x, y, 255, 0, 0) ## barvo bo treba dodat
                
def move(position, table):
    if event.direction == "up":
        y = -1      # Up arrow
        x = 0
    elif event.direction == "down":
        y = 1      # Down arrow
        x = 0
    elif event.direction == "left": 
        x = -1      # Left arrow
        y = 0
    elif event.direction == "right":
        x = 1      # Right arrow
        y = 0
    elif event.direction == "middle":
        x = 0      
        y = 0
    x1 = position[0]
    y1 = position[1]
    x = x + x1
    y = y +y1
    if table[x, y]:
        return position
    elif x<0 or x>7 or y<0 or y>7:
        return position
    else:
        position = [x, y]
        return position
    
def drawPath(path, color):
    for pos in path:
        sense.set_pixel(pos[0], pos[1], 0, 0, 255) # teba dodat barvo

def main():
    table =  maze.generate_maze(8,8)
    coordinate = [0,0]
    path = []
    path.append(coordinate)
    draw(path, "blue")
    while coordinate != [7,7]:
        draw(table , "red")
        coordinate = move(coordinate, table)
        path.append(coordinate)
        draw(path, "blue")
        time.sleep(0.3)

while True:
    main()
    