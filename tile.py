class Tile:
    def __init__(self, number, resource_type):
        self.number = number
        self.resource_type = resource_type

    def __str__(self):
        return f"Tile {self.number}: {self.resource_type}"


# Create the tiles
tile1 = Tile(2, "brick")
tile2 = Tile(3, "ore")
tile3 = Tile(4, "wheat")
tile4 = Tile(5, "wood")
tile5 = Tile(6, "sheep")
tile6 = Tile(8, "ore")
tile7 = Tile(9, "wheat")
tile8 = Tile(10, "wood")
tile9 = Tile(11, "brick")
tile10 = Tile(12, "sheep")
tile11 = Tile(11, "wood")
tile12 = Tile(10, "ore")
tile13 = Tile(9, "sheep")
tile14 = Tile(8, "wheat")
tile15 = Tile(6, "brick")
tile16 = Tile(5, "wheat")
tile17 = Tile(4, "ore")
tile18 = Tile(3, "sheep")

# Store the tiles in a list
tiles = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9,
         tile10, tile11, tile12, tile13, tile14, tile15, tile16, tile17, tile18]
