# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move_to(self, direction, current_location):

        attribute = direction + '_to'

        if hasattr(current_location, attribute):
            return getattr(current_location, attribute)
        print("--------------------")
        print("That way is blocked!")
        print("--------------------")

        return current_location
