
from sense_hat import SenseHat
from time import sleep, strftime
from time import strftime


sense = SenseHat()
red = (255, 0, 0)
green = (0, 255, 0)


event = sense.stick.wait_for_event()
if event.action == "pressed" and event.direction == "middle":
  day = int(strftime("%d"))
  month = strftime("%B")

# ------------------------------------------------
# DATA
# ------------------------------------------------

# Colours
colours = {

  'r' : [255, 0, 0],
  'o' : [247, 131, 16],
  'y' : [255, 255, 0],
  'g' : [0, 255, 0],
  'b' : [0, 0, 255],
  'i' : [63, 15, 145],
  'v' : [42, 26, 62],
  'n' : [135, 80, 22],
  'w' : [255, 255, 255],
  'e' : [0, 0, 0]  # e stands for empty/black

}

with open("pictures.txt", "r") as f:
    all_pics = f.readlines()
door = all_pics[0]
# ------------------------------------------------
# FUNCTIONS
# ----------------------------------------------


def display_pic(pic_string):

  # Get rid of newline and split the line into a list  
  pic_string = pic_string.strip("\n")
  pic_string = pic_string.split(",")

  # Look up each letter in the dictionary of colours and add it to the list
  pic_list = []
  for letter in pic_string:
      pic_list.append(colours[letter])

  # Display the pixel colours from the file
  sense.set_pixels(pic_list)



# ------------------------------------------------
# ------------------------------------------------
sense.clear()
display_pic(door)
sense.show_message( str(month) )

if month == "December" and day < 15:
    sense.show_message(str(day))    # Convert day to a string
    sense.show_message("Almost Christmas!!", text_colour = red)
    display_pic(all_pics[day])
    sleep(5)
  
else:
    sense.show_message(str(day))
    sense.show_message("SOOO CLOSE TO CHRISTMAS!!", text_colour = green)
    display_pic(all_pics[day])
    sleep(5)
  
if month == "December" and day == 25:
  sense.show_message("IT'S CHRISTMAS", text_colour = red)
  display_pic(all_pics[day])
  sleep(5)

