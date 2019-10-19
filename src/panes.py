
from luma.core.render import canvas

class _Generic_Pane:
    def __init__(self, device):
        self.device = device
        self.draw = canvas(self.device)

    def ready(self):
        print("Ready!")

    def destroy(self):
        print("Destroying!")
            
    def left(self):
        pass

    def right(self):
        pass

    def shutter(self):
        pass

    def select(self):
        pass


class Pane_Left(_Generic_Pane):
    def ready(self):
        with self.draw as draw:
            draw.rectangle(self.device.bounding_box, outline="white", fill="black")
            draw.text((30,10), "Left!", fill="white")

    def right(self):
        return "Pane_Center"


class Pane_Center(_Generic_Pane):
    def ready(self):
        with self.draw as draw:
            draw.rectangle(self.device.bounding_box, outline="white", fill="black")
            draw.text((30,10), "Center!", fill="white")

    def left(self):
        return "Pane_Left"

    
    def right(self):
        return "Pane_Right"



    
class Pane_Right(_Generic_Pane):
    def ready(self):
        with self.draw as draw:
            draw.rectangle(self.device.bounding_box, outline="white", fill="black")
            draw.text((30,10), "Right!", fill="white")

    def left(self):
        return "Pane_Center"

