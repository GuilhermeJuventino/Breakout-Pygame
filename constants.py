# Game settings

WIDTH = 1280
HEIGHT = 720

# Block settings

BLOCK_MAP = [
    "666666666666",
    "444557755444",
    "333333333333",
    "222222222222",
    "111111111111",
    "            ",
    "            ",
    "            ",
    "            "]

COLOR_LEGEND = {
    "1": "blue",
    "2": "green",
    "3": "red",
    "4": "orange",
    "5": "purple",
    "6": "chocolate",
    "7": "grey"
}

GAP_SIZE = 2
BLOCK_WIDTH = WIDTH / len(BLOCK_MAP) - 35 - GAP_SIZE
BLOCK_HEIGHT = HEIGHT / len(BLOCK_MAP[0]) - GAP_SIZE
TOP_OFFSET = 54
