from utils import (
    return_path_rel_dataset,
    get_dataset_layout,
    config,
    get_deepmreye_mask_name,
)


def test_get_dataset_layout_smoke_test():
    get_dataset_layout("data")


def test_return_path_rel_dataset():

    file_path = "/home/john/gin/datset/sub-03/func/sub-03_task-rest_space-T1w_desc-preproc_bold.nii.gz"
    dataset_path = "/home/john/gin/datset"
    rel_file_path = return_path_rel_dataset(file_path, dataset_path)

    assert (
        rel_file_path
        == "sub-03/func/sub-03_task-rest_space-T1w_desc-preproc_bold.nii.gz"
    )


def test_get_deepmreye_mask_name():

    cfg = config()
    layout = get_dataset_layout(cfg["input_folder"])

    img = layout.get(
        return_type="filename",
        subject="cb01",
        suffix="bold",
        task="rest",
        space="MNI152NLin2009cAsym",
        extension=".nii.gz",
    )

    deepmreye_mask_name = get_deepmreye_mask_name(layout, img)

    assert (
        deepmreye_mask_name
        == "/home/remi/github/CPP_deepMReye/inputs/rest_blnd_can_fmriprep/sub-cb01/func/mask_sub-cb01_task-rest_space-MNI152NLin2009cAsym_desc-preproc_bold.p"
    )
