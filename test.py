scores = open("Core_Change_Docking_Go\map11.txt", "r")
# print(file.read())
# print(type(file.read()))

map = []
i = 0

class Coordinate():
    int x
    int y
    
    def go_north():
        y -= 1
        
    def go_south():
        y += 1
        
    def go_east():
        x += 1
        
    def go_west():
        x -= 1
        
    def go_north_east():
        y -= 1
        x += 1
        
    def go_north_west():
        y -= 1
        x -= 1
    
    def go_south_west():
        y += 1
        x -= 1
        
    def go_south_east():
        y += 1
        x += 1    

class Seeker():
    seeker_coord = Coordinate()
    
    # Update postion
    def seek():
    
    # Update range    
    def update_range():
        
        
        

class Hider():
    hider_coord = Coordinate()
    
class Game():
    
        
        
