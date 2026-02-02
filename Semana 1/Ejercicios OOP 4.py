class Head:
    def __init__(self):
        self.has_brain=True

class Torso:
    def __init__(self):
        self.has_heart=True

class Arms:
    def __init__(self,side):
        self.side=side

class Hands:
    def __init__(self,side):
        self.side=side
        self.fingers=5

class Legs:
    def __init__(self,side):
        self.side=side

class Feet:
    def __init__(self,side):
        self.side=side
        self.toes=5

class Human:
    def __init__(self):
        self.head=Head()
        self.torso=Torso()
        self.right_arm=Arms("Right")
        self.left_arm=Arms("Left")
        self.right_hand=Hands("Right")
        self.left_hand=Hands("Left")
        self.right_leg=Legs("Right")
        self.left_leg=Legs("Left")
        self.right_foot=Feet("Right")
        self.left_foot=Feet("Left")

h=Human()
print(h.head.has_brain)
print(h.left_foot.toes)
print(h.right_hand.fingers)