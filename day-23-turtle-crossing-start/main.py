import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_player, "Up")

game_is_on = True
car_counter = 1
car_list = []
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_counter += 1
    if car_counter % 6 == 0:
        car_manager.add_car()

    car_manager.move_cars()

    # Detect when the turtle player collides with a car and stop the game if this happens. If you get stuck,
    # check the video walkthrough in Step 5.
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect when player has reached the top of the screen
    if player.ycor() >= player.finish_line:
        player.reset_player()
        scoreboard.increase_score()
        car_manager.increase_speed()


screen.exitonclick()





