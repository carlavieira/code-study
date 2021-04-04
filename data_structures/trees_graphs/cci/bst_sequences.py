class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst_sequences(root):
    sequences = []

    if not root:
        sequences.append([])
        return sequences

    prefix = []
    prefix.append(root.val)

    left_sequences = bst_sequences(root.left)
    right_sequences = bst_sequences(root.right)

    for left_sequence in left_sequences:
        for right_sequence in right_sequences:
            combinations = generate_combinations(prefix, left_sequence, right_sequence)
            sequences.extend(combinations)

    return sequences

def generate_combinations(prefix, left_sequence, right_sequence):
    combinations = []

    if not left_sequence or not right_sequence:
        combination = prefix.copy()
        combination.extend(left_sequence)
        combination.extend(right_sequence)
        combinations.append(combination)
        return combinations

    else:
        first_left_sequence = left_sequence[0]
        left_sequence = left_sequence[1:]
        prefix.append(first_left_sequence)
        combinations.extend(generate_combinations(prefix, left_sequence, right_sequence))
        prefix.pop()
        left_sequence = [first_left_sequence].extend(left_sequence)

        first_right_sequence = right_sequence[0]
        right_sequence = right_sequence[1:]
        prefix.append(first_right_sequence)
        combinations.extend(generate_combinations(prefix, left_sequence, right_sequence))
        prefix.pop()
        right_sequence = [first_left_sequence].extend(right_sequence)

    return combinations