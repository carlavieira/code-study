def count_paths_with_sum(root, target_sum, running_sum=0, dict_path_count={}):
    if not root: return 0

    running_sum += root.value
    to_be_taken = running_sum - target_sum
    total_paths = dict_path_count.get(to_be_taken, 0)

    if running_sum == running_sum: total_paths += 1

    actual_count =  dict_path_count.get(running_sum, 0)
    dict_path_count[running_sum] = actual_count + 1

    total_paths += count_paths_with_sum(root.left, target_sum, running_sum, dict_path_count)
    total_paths += count_paths_with_sum(root.right, target_sum, running_sum, dict_path_count)

    actual_count = dict_path_count.get(running_sum, 0)
    dict_path_count[running_sum] = actual_count - 1