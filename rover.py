class rover():
  def __init__(self, hub, colors):
    self.hub = hub
    self.colors = colors
  
  def act(self):
    #print( self.left_wheel, self.right_wheel)
    self.hub.motor_AB.timed(1, self.left_wheel, self.right_wheel)

  def sense(self, color, distance):
    speed = distance/10
    self.hub.led.set_color(color)
    if color == 9: 
      print("saw {} STOP".format(self.colors[color]))
      self.hub.motor_AB.stop()
      self.hub.motor_external.stop()

    elif color == 6 or color == 5 or color == 7:
      print("saw {} FORWARD {}".format(self.colors[color], speed))
      self.hub.motor_AB.start_speed(speed)

    elif color == 3:
      print("saw {} BACKWARDS {}".format(self.colors[color], speed))
      self.hub.motor_AB.start_speed(-speed)

    elif color == 10:
      print("saw {} ROTOR".format(self.colors[color]))
      self.hub.motor_external.start_speed()
