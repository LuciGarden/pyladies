from turtle import fillcolor, begin_fill, forward, left, end_fill, exitonclick

size = 100
<<<<<<< HEAD
color = "#purple"
=======
color = "#blue"
>>>>>>> sestiuhelnik

# Nastaví barvu
fillcolor(color)
begin_fill()

# Nakreslí šestiuhelník
for _ in range(6):
    forward(size)
    left(60)

end_fill()

exitonclick()