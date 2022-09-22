from pathlib import Path
import numpy as np
import pandas as pd

recogned_suffix = [".dat", ".ascii", ".spec"]


def clean_spectrum(
        file_path: Path | str
):
    if isinstance(file_path, str):
        file_path = Path(file_path)

    if file_path.suffix == ".spec":

        df = pd.read_table(
            file_path,
            comment="#",
            names=["wavelength", "flux", "sky_flux", "flux_unc", "xpixel", "ypixel", "response", "flag"],
            sep="\s+"
        )

        mask = np.logical_and(
            df["flux"] > 0.,
            df["flag"] == 0.
        )
        df = df[mask]

    else:
        print(file_path.suffix)

    print(df)

    print(file_path)

    new_path = file_path.parent / (file_path.stem + '_clean.spxtxt')

    df[["wavelength", "flux"]].to_csv(new_path, index=False, header=False, sep=" ")

    return new_path