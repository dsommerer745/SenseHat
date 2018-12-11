from sense_hat import SenseHat
from time import sleep, strftime

sense = SenseHat()

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
  'e' : [0, 0, 0] 


}

with open("pictures.txt", "r") as f:
    all_pics = f.readlines()
    door = all_pics[1]
    display_pic(door)

# ------------------------------------------------
# FUNCTIONS
# ------------------------------------------------

# ------------------------------------------------
def display_pic(pic_string):

  # Get rid of newline and split the line into a list
  pic_string = pic_string.strip("\n")
  pic_string = pic_string.split(",")

  # Look up each letter in the dictionary of colours and add it to the list
  pic_list = []
  for letter in pic_string:
      pic_list.append(colours[letter])

  # Display the pixel colours from the from sense_hat import SenseHat
from time import sleep, strftime

sense = SenseHat()

# ------------------------------------------------
# DATA
# ------------------------------------------------


# ------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------
sense.clear()
display_pic(all_pics[7])


