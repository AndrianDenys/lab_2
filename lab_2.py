class Game_board(object):
    def __init__(self,size):
        self.size = size
    def generate_field(self):
        field = []
        i = 0
        j = 0
        while i < self.size:
            field.append(["0" for j in range(self.size)])
            i+= 1
        return field
    def user_fire(self, a, b):
        # "0" == empty node
        # "1" == empty and checked node
        # "2" == damaged ship
        if field[a][b] == "0":
            if [a,b] in Ship.ships:
                Ship.ships.remove(self, [a,b])
                field[a][b] = "2"
            else:
                field[a][b] = "1"
        else:
            print("This node already destroyed")
            self.user_fire(a, b)
        return field


class Ship(Game_board):
    blocked = []
    ships = []
    def spawn_a_ship(self, size):
        i = random.randrange(len(super().size))
        j = random.randrange(len(super().size))
        node = [i, j]

        def check(self, node):
        if node is not in blocked:
            return True
        else:
            return False
    if size == 4:
        if check(node) and check([i+3, j]) and check([i+1, j]) and check([i+2, j]):
            ship.append(node, [i+1,j], [i+2, j], [i+3, j])
            blocked.append(node, [i+1,j], [i+2, j], [i+3, j], [i-1,j], [i+4, j], [i, j-1], [i+1,j-1], [i+2, j-1], [i+3, j-1], [i-1,j-1], [i+4, j-1], [i, j+1], [i+1,j+1], [i+2, j+1], [i+3, j+1], [i-1,j+1], [i+4, j+1])
            #killmepls
        elif check(node) and check([i-3, j]) and check([i-1, j]) and check([i-2, j]):
            ship.append(node, [i-1, j], [i-2, j], [i-3, j])
            blocked.append(node, [i-1, j], [i-2, j], [i-3, j], [i+1, j], [i-4,j], [i, j-1], [i-1, j-1], [i-2, j-1], [i-3, j-1], [i+1, j-1], [i-4,j-1], [i, j+1], [i-1, j+1], [i-2, j+1], [i-3, j+1], [i+1, j+1], [i-4,j+1])
        elif check(node) and check([i, j+3]) and check([i, j+1]) and check([i, j+2]):
            ship.append(node, [i, j+1], [i, j+2], [i, j+3])
            blocked.append(node, [i, j+1], [i, j+2], [i, j+3], [i, j-1], [i, j+4], [i+1, j], [i+1, j+1], [i+1, j+2], [i+1, j+3], [i+1, j-1], [i+1, j+4], [i-1, j], [i-1, j+1], [i-1, j+2], [i-1, j+3], [i-1, j-1], [i-1, j+4])
        elif check(node) and check([i, j-3]) and check([i, j-2]) and check([i, j-1]):
            ship.append(node, [i, j-1], [i, j-2], [i, j-3])
            blocked.append(node, [i, j-1], [i, j-2], [i, j-3], [i, j-4], [i, j+1], [i-1, j], [i-1, j-1], [i-1, j-2], [i-1, j-3], [i-1, j-4], [i-1, j+1], [i+1, j], [i+1, j-1], [i+1, j-2], [i+1, j-3], [i+1, j-4], [i+1, j+1])
        else:
            spawn_a_ship(size)
    elif size == 3:
        if check(node) and check([i + 1, j]) and check([i + 2, j]):
            ship.append(node, [i + 1, j], [i + 2, j])
            blocked.append(node, [i + 1, j], [i + 2, j], [i - 1, j], [i + 3, j], [i, j - 1],
                           [i + 1, j - 1], [i + 2, j - 1], [i + 3, j - 1], [i - 1, j - 1],
                           [i, j + 1], [i + 1, j + 1], [i + 2, j + 1], [i + 3, j + 1], [i - 1, j + 1])

        elif check(node) and check([i - 1, j]) and check([i - 2, j]):
            ship.append(node, [i - 1, j], [i - 2, j])
            blocked.append(node, [i - 1, j], [i - 2, j], [i - 3, j], [i + 1, j], [i, j - 1],
                           [i - 1, j - 1], [i - 2, j - 1], [i - 3, j - 1], [i + 1, j - 1],
                           [i, j + 1], [i - 1, j + 1], [i - 2, j + 1], [i - 3, j + 1], [i + 1, j + 1])
        elif check(node) and check([i, j + 1]) and check([i, j + 2]):
            ship.append(node, [i, j + 1], [i, j + 2])
            blocked.append(node, [i, j + 1], [i, j + 2], [i, j + 3], [i, j - 1], [i + 1, j],
                           [i + 1, j + 1], [i + 1, j + 2], [i + 1, j + 3], [i + 1, j - 1],
                           [i - 1, j], [i - 1, j + 1], [i - 1, j + 2], [i - 1, j + 3], [i - 1, j - 1])
        elif check(node) and check([i, j - 2]) and check([i, j - 1]):
             ship.append(node, [i, j - 1], [i, j - 2])
             blocked.append(node, [i, j - 1], [i, j - 2], [i, j - 3], [i, j + 1], [i - 1, j],
                           [i - 1, j - 1], [i - 1, j - 2], [i - 1, j - 3], [i - 1, j + 1],
                           [i + 1, j], [i +1, j - 1], [i +1, j - 2], [i + 1, j - 3], [i +1, j + 1])
        else:
            spawn_a_ship(size)
    elif size == 2:
        if check(node) and check([i + 1, j]):
            ship.append(node, [i + 1, j])
            blocked.append(node, [i + 1, j], [i + 2, j], [i - 1, j], [i, j - 1],
                           [i + 1, j - 1], [i + 2, j - 1], [i - 1, j - 1],
                           [i, j + 1], [i + 1, j + 1], [i + 2, j + 1], [i - 1, j + 1])
            #really
        elif check(node) and check([i - 1, j]):
            ship.append(node, [i - 1, j])
            blocked.append(node, [i - 1, j], [i - 2, j], [i + 1, j], [i, j - 1],
                           [i - 1, j - 1], [i - 2, j - 1], [i + 1, j - 1],
                           [i, j + 1], [i - 1, j + 1], [i - 2, j + 1], [i + 1, j + 1])
        elif check(node) and check([i, j + 1]):
            ship.append(node, [i, j + 1])
            blocked.append(node, [i, j + 1], [i, j + 2], [i, j - 1], [i + 1, j],
                           [i + 1, j + 1], [i + 1, j + 2], [i + 1, j - 1],
                           [i - 1, j], [i - 1, j + 1], [i - 1, j + 2], [i - 1, j - 1])
        elif check(node) and check([i, j - 2]):
            ship.append(node, [i, j - 1])
            blocked.append(node, [i, j - 1], [i, j - 2], [i, j + 1], [i - 1, j],
                           [i - 1, j - 1], [i - 1, j - 2], [i - 1, j + 1],
                           [i + 1, j], [i + 1, j - 1], [i + 1, j - 2], [i + 1, j + 1])
        else:
            spawn_a_ship(size)
    elif size == 1:
        if check(node):
            ship.append(node)
            blocked.append(node, [i + 1, j], [i - 1, j], [i, j - 1],
                           [i + 1, j - 1]], [i - 1, j - 1],
                           [i, j + 1], [i + 1, j + 1], [i - 1, j + 1])
        elif check(node):
            ship.append(node)
            blocked.append(node, [i - 1, j], [i + 1, j], [i, j - 1],
                           [i - 1, j - 1], [i + 1, j - 1],
                           [i, j + 1], [i - 1, j + 1], [i + 1, j + 1])
        elif check(node):
            ship.append(node)
            blocked.append(node, [i, j + 1], [i, j - 1], [i + 1, j],
                           [i + 1, j + 1], [i + 1, j - 1],
                           [i - 1, j], [i - 1, j + 1], [i - 1, j - 1])
        elif check(node):
            ship.append(node)
            blocked.append(node, [i, j - 1], [i, j + 1], [i - 1, j],
                           [i - 1, j - 1], [i - 1, j + 1],
                           [i + 1, j], [i + 1, j - 1], [i + 1, j + 1])
        else:
            spawn_a_ship(size)
    spawn_a_ship(4)
    spawn_a_ship(3)
    spawn_a_ship(3)
    spawn_a_ship(2)
    spawn_a_ship(2)
    spawn_a_ship(2)
    spawn_a_ship(1)
    spawn_a_ship(1)
    spawn_a_ship(1)
    spawn_a_ship(1)