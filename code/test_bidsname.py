import pytest
from bidsname import create_bidsname
from bidsname import get_bidsname_config
from bidsname import set_dataset_description
from bidsname import write_dataset_description
from utils import get_dataset_layout


def test_write_dataset_description_smoke_test():
    layout = get_dataset_layout("data")
    layout = set_dataset_description(layout)
    layout.dataset_description["GeneratedBy"][0]["Name"] = "deepMReye"
    write_dataset_description(layout)


def test_get_bidsname_config_smoke_test():
    bidsname_config = get_bidsname_config()
    assert list(bidsname_config.keys()) == ["mask", "report"]


@pytest.mark.parametrize(
    "output, filetype",
    [
        (
            "/home/remi/github/CPP_deepMReye/code/data/sub-03/func/sub-03_task-rest_space-T1w_desc-eye_mask.p",
            "mask",
        ),
        (
            "/home/remi/github/CPP_deepMReye/code/data/sub-03/func/sub-03_task-rest_space-T1w_desc-eye_report.html",
            "report",
        ),
    ],
)
def test_create_bidsname(output, filetype):

    # TODO make test not dependent on local absolute path

    filename = "/home/john/gin/dataset/sub-03/func/sub-03_task-rest_space-T1w_desc-preproc_bold.nii.gz"

    layout = get_dataset_layout("data")
    mask = create_bidsname(layout, filename, filetype)
    assert mask == output
