import os

from deepmreye import preprocess
from rich import print
from utils import (
    config,
    create_dir_if_absent,
    create_dir_for_file,
    get_deepmreye_mask_name,
    get_dataset_layout,
    list_subjects,
    return_regex,
    check_layout,
)
from bidsname import create_mask_name


def coregister_and_extract_data(img: str):

    (
        eyemask_small,
        eyemask_big,
        dme_template,
        mask,
        x_edges,
        y_edges,
        z_edges,
    ) = preprocess.get_masks()

    print(f"Input file: {img}")

    preprocess.run_participant(
        img, dme_template, eyemask_big, eyemask_small, x_edges, y_edges, z_edges
    )


def preprocess_subject(layout, subject_label):

    cfg = config()

    layout = get_dataset_layout(cfg["input_folder"])

    print(f"Running subject: {subject_label}")

    bf = layout.get(
        return_type="filename",
        subject=return_regex(subject_label),
        suffix="^bold$",
        task=return_regex(cfg["task"]),
        space=return_regex(cfg["space"]),
        extension=".nii.*",
        regex_search=True,
    )

    for img in bf:
        coregister_and_extract_data(img)

        output = get_dataset_layout(cfg["output_folder"])
        mask_name = create_mask_name(output, img)
        create_dir_for_file(mask_name)

        deepmreye_mask_name = get_deepmreye_mask_name(layout, img)

        print(f"{deepmreye_mask_name} --> {mask_name}")
        os.rename(deepmreye_mask_name, mask_name)


def preprocess_dataset(dataset_path):

    cfg = config()

    layout = get_dataset_layout(dataset_path)
    check_layout(layout)

    create_dir_if_absent(cfg["output_folder"])

    subjects = list_subjects(layout)
    if cfg["debug"]:
        subjects = [subjects[0]]

    for subject_label in subjects:

        preprocess_subject(layout, subject_label)


def main():

    cfg = config()

    print(f"\nindexing {cfg['input_folder']}\n")
    preprocess_dataset(cfg["input_folder"])


if __name__ == "__main__":

    main()
