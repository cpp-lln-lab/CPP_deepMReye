from utils import (return_path_rel_dataset)

def test_return_path_rel_dataset():

    file_path = "/home/john/gin/datset/sub-03/func/sub-03_task-rest_space-T1w_desc-preproc_bold.nii.gz"
    dataset_path = "/home/john/gin/datset"
    rel_file_path = return_path_rel_dataset(file_path, dataset_path)

    assert rel_file_path == "sub-03/func/sub-03_task-rest_space-T1w_desc-preproc_bold.nii.gz"