def read_input(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    with open(input_file) as f:
        lines = [line.strip() for line in f]

        lol = []
        for line in lines:
            char_list = list(line)
            int_list = [int(char) for char in char_list]
            lol.append(int_list)

    return lol


def check_tree_visible(input, tree_x, tree_y, num_rows, num_columns):


    # If it is an outside tree, then it is by default visible
    if tree_x == 0 or tree_x == (num_rows-1) or tree_y == 0 or tree_y == (num_columns-1):
        return True

    # By default, set all angles visible. Then we evaluate each surrounding tree
    # and if we find one that is equal or taller on that side, the variable gets set
    # to False.
    left_visible, right_visible, above_visible, below_visible = True, True, True, True
    # check left
    li = 0
    while li < tree_y:
        # For each tree to the left, check if it is taller.
        # If it is, set visible=False
        if input[tree_x][li] >= input[tree_x][tree_y]:
            left_visible=False

        li += 1

    # check right
    ri = (num_columns-1)
    while ri > tree_y:
        # For each tree to the left, check if it is taller.
        # If it is, set visible=False
        if input[tree_x][ri] >= input[tree_x][tree_y]:
            right_visible = False

        ri -= 1

    # check above
    ai = 0
    while ai < tree_x:
        # For each tree to the left, check if it is taller.
        # If it is, set visible=False
        if input[ai][tree_y] >= input[tree_x][tree_y]:
            above_visible = False

        ai += 1

    # check below
    bi = (num_rows-1)
    while bi > tree_x:
        # For each tree to the left, check if it is taller.
        # If it is, set visible=False
        if input[bi][tree_y] >= input[tree_x][tree_y]:
            below_visible = False

        bi -= 1

    # Use max because only need 1 side to be visible
    return max(left_visible, right_visible, above_visible, below_visible)


def check_tree_view_distance(input, tree_x, tree_y, num_rows, num_columns):

    # If it is an outside tree, then it is by default visible
    if tree_x == 0 or tree_x == (num_rows - 1) or tree_y == 0 or tree_y == (num_columns - 1):
        return 0, (0,0,0,0)

    # check left
    li = (tree_y-1)
    left_view = 0
    while li >= 0:
        # For each tree to the left, check if it is taller.
        # If it is, set visible=False
        if input[tree_x][li] < input[tree_x][tree_y]:
            left_view += 1
        else:
            left_view += 1#max(1, left_view)
            break
        li -= 1

    # check right
    ri = (tree_y + 1)
    right_view = 0
    while ri <= (num_columns-1):
        # For each tree to the left, check if it is taller.
        # If it is, set visible=False
        if input[tree_x][ri] < input[tree_x][tree_y]:
            right_view += 1
        else:
            right_view += 1#max(1, left_view)
            break
        ri += 1

    # check above
    ai = (tree_x - 1)
    above_view = 0
    while ai >= 0:
        # For each tree to the left, check if it is taller.
        # If it is, set visible=False
        if input[ai][tree_y] < input[tree_x][tree_y]:
            above_view += 1
        else:
            above_view += 1#max(1, left_view)
            break
        ai -= 1

    # check above
    bi = (tree_x + 1)
    below_view = 0
    while bi <= (num_rows-1):
        # For each tree to the left, check if it is taller.
        # If it is, set visible=False
        if input[bi][tree_y] < input[tree_x][tree_y]:
            below_view += 1
        else:
            below_view += 1#max(1, left_view)
            break
        bi += 1


    scenic_score = left_view * right_view * above_view * below_view
    individual_scores = (left_view, right_view, above_view, below_view)

    return scenic_score, individual_scores


input = read_input('info.in')
num_columns = len(input[0])
num_rows = len(input)
print(f"Shape: [{num_rows}, {num_columns}]")

def part_1():

    visible_tree_counter = 0
    for x in range(num_rows):
        for y in range(num_columns):
            visible = check_tree_visible(input, x, y, num_rows, num_columns)
            print(f"({x}, {y}) = {input[x][y]} | {visible}")
            if visible:
                visible_tree_counter += 1

    print(visible_tree_counter, 123)


def part_2():

    max_scenic_score = 0
    max_scenic_score_loc = [(0,0)]

    for x in range(num_rows):
        for y in range(num_columns):
            scenic_score, indiv_scores = check_tree_view_distance(input, x, y, num_rows, num_columns)
            print(f"({x}, {y}) = {input[x][y]} | {scenic_score} | {indiv_scores}")
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
                max_scenic_score_loc[0] = (x, y)

    print(f"{max_scenic_score_loc} = {max_scenic_score}")

part_2()