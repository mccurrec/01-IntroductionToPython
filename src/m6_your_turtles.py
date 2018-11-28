"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Ezrie McCurry.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
ezrie = rg.SimpleTurtle('classic')
ezrie.pen = rg.Pen('pink',10)
ezrie.speed = 10
frank = rg.SimpleTurtle('turtle')
frank.pen = rg.Pen('green',10)
frank.speed = 15

size_ezrie = 200
number_ezrie = 15

for k in range(10)
    ezrie.draw_regular_polygon(number_ezrie,size_ezrie)
    ezrie.pen_up()
    ezrie.forward(10)
    ezrie.pen_down()
    size_ezrie = size_ezrie-10
