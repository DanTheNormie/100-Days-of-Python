 go to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

 Code :-

 
def go_left_to_right():
    for i in range(1,10):
        move()
    turn_left()
    move()
    turn_left()
    
def go_right_to_left():
    for i in range(1,10):
        move()
    for i in range(1,4):
        turn_left()
    move()
    for i in range(1,4):
        turn_left()

def look_east():
    while(not is_facing_north()):
        turn_left()
        if(is_facing_north()):
            for i in range(0,3):
                turn_left()
            break
          
def turn_right():
    for i in range(0,3):
        turn_left()

def draw_sqr_clockwise_loop(a):
    turn_left()
    for i in range(0,a):
        move()
        for i in range(0,3):
            turn_right()
            move()
        turn_right()

def jump():
    turn_left()
    while(wall_on_right()):
        move()
    turn_right()
    move()
    turn_right()
    while(front_is_clear()):
        move()
    turn_left()

def turn_down():
    for i in range(2):
        turn_left()
def face_up():
    while(not is_facing_north()):
        turn_left()
        
def noob_algo():        
    last_position = ""

    while not at_goal():
        print(f"last position is : {last_position}")
        face_up()
        if(front_is_clear() and last_position != "up"):
            move()
            last_position = "down"
        elif(right_is_clear()and last_position != "right"):
            turn_right()
            move()
            last_position = "left"
        else:
            if(last_position == "left" or last_position == "up"):
                turn_down()
                if(front_is_clear()):
                    while(front_is_clear()):
                        move()
                    last_position = "up"
                else:
                    turn_right()
                    if(front_is_clear()):
                        move()
                        last_position = "right"
                    else:
                        last_position = ""
            else:
                turn_count = 0
                while(not front_is_clear()):
                    turn_count += 1
                    turn_left()
                move()
                if(turn_count == 1):
                    last_position = "right"
                elif(turn_count == 2):
                    last_position = "up"
                elif(turn_count == 3):
                    last_position = "left"
                else:
                    last_position = "down"
                    

def turn_right():
        turn_left()
        turn_left()
        turn_left()
def noob_algo2():
    while not at_goal():
        if front_is_clear():
            move()
        elif right_is_clear():
            turn_right()
            move()
        else:
            turn_left()
noob_algo()