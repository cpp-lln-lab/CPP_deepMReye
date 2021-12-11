import os
from bids import BIDSLayout
from rich import print
from pathlib import Path


def config():

    cfg = {
        "output_folder": "../outputs/deepMReye/",
        "input_folder": "../inputs/rest_blnd_can_fmriprep/",
        "model_weights_file": "../inputs/models/dataset1_guided_fixations.h5",
        "space": "MNI152NLin2009cAsym",
        "suffix": "bold",
        "task": "rest",
        "debug": True,
    }

    has_GPU = False

    os.environ["CUDA_VISIBLE_DEVICES"] = "0" if has_GPU else ""

    return cfg


def create_dir_if_absent(output_path):
    if not Path(output_path).exists():
        print(f"Creating dir: {output_path}")
        os.makedirs(output_path)


def create_dir_for_file(file: str):
    output_path = os.path.dirname(os.path.abspath(file))
    create_dir_if_absent(output_path)


def return_regex(string):
    return f"^{string}$"


def list_subjects(layout):
    subjects = layout.get_subjects()
    return subjects


def get_dataset_layout(dataset_path: str):

    create_dir_if_absent(dataset_path)

    layout = BIDSLayout(dataset_path, validate=False, derivatives=False)
    return layout


def check_layout(layout):

    # TODO check that subject requested exists and has data to process

    desc = layout.get_dataset_description()
    if desc["DatasetType"] != "derivative":
        raise Exception("Input dataset should be BIDS derivative")

    cfg = config()
    bf = layout.get(
        return_type="filename",
        task=cfg["task"],
        space=cfg["space"],
        suffix="^bold$",
        extension="nii.*",
        regex_search=True,
    )

    if bf == []:
        raise Exception("Input dataset does not have any data to process")


def return_path_rel_dataset(file_path, dataset_path):
    """
    Create file path relative to the root of a dataset
    """
    file_path = os.path.abspath(file_path)
    dataset_path = os.path.abspath(dataset_path)
    rel_path = file_path.replace(dataset_path, "")
    rel_path = rel_path[1:]
    return rel_path


def get_deepmreye_mask_name(layout, img):

    if isinstance(img, (list)):
        img = img[0]

    bf = layout.get_file(img)
    filename = bf.filename
    filename = "mask_" + filename.replace("nii.gz", "p")
    filefolder = os.path.dirname(os.path.abspath(img))

    deepmreye_mask_name = os.path.join(filefolder, filename)

    return deepmreye_mask_name
