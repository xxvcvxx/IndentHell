class Snake:

    def snake_move(snake_body):
        for seg in range(len(snake_body)-1, 0, -1):
            new_x = snake_body[seg - 1].xcor()
            new_y = snake_body[seg - 1].ycor()
            snake_body[seg].goto(new_x,new_y)
        snake_body[0].forward(20)
