from collections import deque

def fill_the_box(height, length, width, *args):
    box_size = height * length * width
    cubes = deque(args)

    while cubes[0] != "Finish":
        box_size -= cubes.popleft()

        if box_size < 0:
            cubes_left = sum(x for x in cubes if x != "Finish")
            return f"No more free space! You have {cubes_left + abs(box_size)} more cubes."
            raise SystemExit

    return f"There is free space in the box. You could put {box_size} more cubes."



print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))