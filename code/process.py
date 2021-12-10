from deepmreye import preprocess

def coregister_and_extract_data(img: str):

    (eyemask_small,
    eyemask_big,
    dme_template,
    mask,
    x_edges,
    y_edges,
    z_edges) = preprocess.get_masks()

    print(f"Input file: {img}")

    preprocess.run_participant(
        img, dme_template, eyemask_big, eyemask_small, x_edges, y_edges, z_edges
    )