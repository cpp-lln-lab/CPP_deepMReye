import json
import os

from pathlib import Path


def get_bidsname_config(config_file="") -> dict:
    """
    See the Path construction demo in the pybids tuto
    https://github.com/bids-standard/pybids/blob/master/examples/pybids_tutorial.ipynb
    """
    default = "config_bidsname.json"
    return get_config(config_file, default)


def get_pybids_config(config_file="") -> dict:
    """
    Pybids configs are stored in the layout module
    https://github.com/bids-standard/pybids/tree/master/bids/layout/config

    But they don't cover the ``ephys`` so we are using modified config, that
    should cover both ephys and microscopy.

    TODO the "default_path_patterns" of that config has not been extended for
    ephys or microscopy yet
    """
    default = "config_pybids.json"
    return get_config(config_file, default)


def get_config(config_file="", default="") -> dict:

    if config_file == "" or not Path(config_file).exists():
        my_path = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(my_path, default)

    if config_file == "" or not Path(config_file).exists():
        return
    with open(config_file, "r") as ff:
        return json.load(ff)


def create_mask_name(layout, filename: str) -> str:

    entities = layout.parse_file_entities(filename)

    bids_name_config = get_bidsname_config()
    output_file = layout.build_path(entities, bids_name_config["mask"], validate=False)

    output_file = os.path.join(layout.root, output_file)

    return output_file
