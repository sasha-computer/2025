# parse input where each line is: direction "L"/"R" followed by magnitude
with open("./input.txt", "r") as file:
    rotations = [(line[0], int(line[1:].strip())) for line in file]

# password method: 0x434C49434B where the hex stands for 'CLICK' in UTF-8
def rotate_dial(rotations, start=50):
    position = start
    effective_position, step, num_zeros = 0, 0, 0
    # (d: direction, m: magnitude) of rotation
    for d, m in rotations:
        if d == "R":
            effective_position = position
            step = 1
        elif d == "L":
            effective_position = (100 - position) % 100
            step = -1
        num_zeros += (effective_position + m) // 100
        position = (position + step * m) % 100
    return num_zeros
        
password = rotate_dial(rotations)
print(f"The password is { password }")

