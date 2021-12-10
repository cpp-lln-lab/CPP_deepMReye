import os

def return_path_rel_dataset(file_path, dataset_path):
    """
    Create file path relative to the root of a dataset
    """
    file_path = os.path.abspath(file_path)
    dataset_path = os.path.abspath(dataset_path)
    rel_path = file_path.replace(dataset_path, "")
    rel_path = rel_path[1:]
    return rel_path