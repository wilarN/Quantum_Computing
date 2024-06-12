
# Size of the matrix
number_of_x_rows = 11 # X
number_of_y_columns = 11 # Y
z_depth = 0 # Not used yet.

# Degrees
alpha_deg = 45
beta_deg = 45
gamma_deg = 45

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

    base_matrix[x][y] = "BLOCK"


def main():
    # Create a dummy location block
    dummy_location = location_block(5, 0, 0, 45, 45, 45)
    dummy_location_second = location_block(5, 5, 0, 45, 45, 45)

    # Add the blocks to the list of all blocks
    all_blocks.append(dummy_location)
    all_blocks.append(dummy_location_second)
    
    for block in all_blocks:
        # Visualises the blocks in the matrix
        place_block_in_matrix(block)

    # Visualises the surrounding cells of the block
    change_surrounding_cells_of(dummy_location_second.x, dummy_location_second.y, "SURRO")

    print_matrix()

if __name__ == "__main__":
    main()