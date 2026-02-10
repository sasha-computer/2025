# parse input where each line is: direction "L"/"R" followed by magnitude
with open("./input.txt", "r") as file:
    rotations = [(line[0], int(line[1:].strip())) for line in file]

def rotate_dial(rotations, start=50):
    position = start
    num_zeros = 0
    # (d: direction, m: magnitude) of rotation
    for d, m in rotations:
        position  = (position + m) % 100 if d == "R" else (position - m) % 100
        if position == 0:
            num_zeros += 1
    return num_zeros
        
password = rotate_dial(rotations)
print(f"The password is { password }")

