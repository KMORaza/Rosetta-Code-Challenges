# 100 Doors
def final_open_doors(num_doors):
    doors = [False] * num_doors
    for pass_num in range(1, num_doors + 1):
        for door_num in range(pass_num - 1, num_doors, pass_num):
            doors[door_num] = not doors[door_num]
    open_doors = [i + 1 for i, is_open in enumerate(doors) if is_open]
    return open_doors
num_doors = 100
result = final_open_doors(num_doors)
print("Open doors after the last pass = ", result)