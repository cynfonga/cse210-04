from game.casting.actor import Actor
from game.casting.cast import Cast
from game.directing.director import Director
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point

DATA_PATH= os.pathdirname(os.path.abspath(_file_)) + "/data/messages.txt"
    White= color(255,255,255)
    DEFAULTS_ARTIFACTS=40

def main():

    cast=Cast()
    banner=Actor()
    banner.set_text("Scores:")
    banner.set_font_size(FONT_SIZE)
    banner.set_position(point(CELL_SIZE))
    cast.add_actor("banners",banner)
    #create the robot

    X=int(MAX_x/2)
    position=point(X, MAX_Y -20)
    robot.settext("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("Robot", robot)
     FRAME_RATE= 12
    MAX_X=900
    MAX_Y= 600
    CELL_SIZE=15
    FONT_SIZE=15
    COLS=60
    ROWS=40
    CAPTION='Robot Finds Kitter'

    #create artifacts

    for n in range (DEFAULT_ARTIFACTS):
        text=random.choice(["*", "o"])
        x=random.randint(1,cols-1)
        y=random.randint(1,rows-1)
        position=Point(x,y)
        position=position.scale(CELL_SIZE)
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        color=Color(r,g,b)
        artifact=Artifact()
        artifact.set_text(text)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_velocity(point(0,1))
        cast.add_actor("artifacts",artifact)
        #start the game
        keyboard_service=KeyboardService(Cell_SIZE)
        video_service=VideoService(CAPTION ,MAX_X,MAX_Y,CELL_SIZE,FRAME_RATE)
        director=Director(keyboard_service,video_service)
        director.start_game(cast)
        if _name_=="_main_":
            
            main()    