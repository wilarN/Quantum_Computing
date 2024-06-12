import math

#* -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#* source main_prep_env/bin/activate
#* -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

#* -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# Size of the matrix
number_of_x_rows = 11 # X
number_of_y_columns = 11 # Y
z_depth = 0 # Not used yet.

# Degrees
alpha_deg = 45
beta_deg = 45
gamma_deg = 45

# Key values
key_values = [5, 5]

# Visualisers
block_visualiser = "BLOCK"
surrounding_visualiser = "SURRO"

# Create a base matrix to store the blocks and their locations
base_matrix = [["--x--" for x in range(number_of_x_rows)] for y in range(number_of_y_columns)]

# Create a list to store all the blocks active
all_blocks = []

# Block class
class location_block:
    def __init__(self, x, y, z, alpha, beta, gamma):
        self.x = x
        self.y = y
        self.z = z
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    # Fetch coordinates of the block in the base matrix
    def get_location(self):
        return [self.x, self.y, self.z]

    # Fetch angles of the block
    def get_angles(self):
        return [self.alpha, self.beta, self.gamma]

# Dummy block to fetch the location of a block // (Used for testing)
dummy_x_location_fetch_block = [
    [
        [0, 0, 0,],
        [0, 0, 0,], # First 3x the x, y, z coordinates of the point
        [0, 0, 0,]
    ],
    [
        [45, 45, 45], # Section 2: The alpha, beta, gamma, n-angle angles of the point defined. Length is dependent on the number of angles set when creating the point.
    ]
]

#* Section 1: The x, y, z coordinates of the point, 3 sets of coordinates
#? dummy_x_location_fetch_block[0][0] = [x, y, z]
#? dummy_x_location_fetch_block[0][1] = [x, y, z]
#? dummy_x_location_fetch_block[0][2] = [x, y, z]
#* Section 2: The alpha, beta, gamma, n-angle angles of the point defined. Length is dependent on the number of angles set when creating the point.
#? dummy_x_location_fetch_block[1] = [alpha, beta, gamma]


# Function to get the surrounding cells of a block
def get_surrounding_cells_of(x, y):
    surrounding_cells = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if x + i < 0 or y + j < 0:
                continue
            try:
                surrounding_cells.append(base_matrix[x + i][y + j])
            except IndexError:
                continue
    return surrounding_cells

# Function to change the surrounding cells of a block
def change_surrounding_cells_of(x, y, new_value):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if x + i < 0 or y + j < 0:
                continue
            try:
                base_matrix[x + i][y + j] = new_value
            except IndexError:
                continue

def print_matrix():
    for row in base_matrix:
        print(row)

def encrypt_matrix():
    pass

def decrypt_matrix():
    pass

# Function to place a block into the base matrix
def place_block_in_matrix(block):
    loc = block.get_location()
    angles = block.get_angles()
    x = loc[0]
    y = loc[1]
    z = loc[2]
    alpha = angles[0]
    beta = angles[1]
    gamma = angles[2]

    base_matrix[x][y] = block_visualiser

def get_angle_between_two_points_in_matrix(x1, y1, x2, y2):
    # NOTE: Always returns the angle is positive degrees, it is meant to be this way.
    delta_x = abs(x2 - x1)
    delta_y = abs(y1 - y2)
    angle = math.degrees(math.atan2(delta_y, delta_x))
    if angle < 0:
        angle += 360
    return angle

def main():
    # Create a dummy location block
    dummy_location = location_block(key_values[0], key_values[1], 0, 45, 45, 45) # key_values[0] = x, key_values[1] = y
    target_block = location_block(number_of_x_rows-1, number_of_y_columns-1, 0, 45, 45, 45)

    # Add the blocks to the list of all blocks
    all_blocks.append(dummy_location)
    all_blocks.append(target_block)

    for block in all_blocks:
        # Visualizes the blocks in the matrix
        place_block_in_matrix(block)

    # Visualizes the surrounding cells of the block
    change_surrounding_cells_of(dummy_location.x, dummy_location.y, surrounding_visualiser)

    print_matrix()
    print(get_angle_between_two_points_in_matrix(dummy_location.x, dummy_location.y, target_block.x, target_block.y))

if __name__ == "__main__":
    main()