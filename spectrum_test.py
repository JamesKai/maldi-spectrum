from os.path import isfile
import matplotlib.pyplot as plt
from matplotlib.pyplot import title
from numpy.core.fromnumeric import shape
import spectrum_utils.plot as sup
import spectrum_utils.spectrum as sus
import os
from typing import List, Tuple
import csv


def read_file(file_path: str) -> Tuple[List[float], List[float]]:

    with open(file_path, "r") as file_read:
        intensity, ms = [], []
        cv_reader = csv.reader(file_read, delimiter=" ")
        for row in cv_reader:
            ms_data, intensity_data = row
            intensity.append(float(intensity_data))
            ms.append(float(ms_data))
    return ms, intensity


def generate_graph(file_path: str):
    file_name = os.path.basename(file_path[:-4])
    # matrix = file_name.split("_")[0]
    # conc = file_name.split("_")[1]
    print("kai3")

    mz, intensity = read_file(f"{file_path}")
    spectrum = sus.MsmsSpectrum(file_name, 1.0, 1, mz, intensity,)
    print("kai4")
    # p2s_mz = 1116
    # spectrum.annotate_mz_fragment(p2s_mz, 1, 3, "Da", text=f"{p2s_mz}\nTriP-2S")
    # # spectrum.annotate_mz_fragment(902, 1, 3, "Da")
    # spectrum.annotate_mz_fragment(656, 1, 3, "Da")
    fig, ax = plt.subplots(figsize=(12, 6))
    # ax.set_title(f"${conc}$ Tri-P2S in {matrix} Matrix")
    save_path = os.path.join(os.path.dirname(file_path), "graph")
    try:
        os.makedirs(save_path)
    except:
        pass
    sup.spectrum(spectrum, ax=ax)
    fig.savefig(os.path.join(save_path, f"{file_name}.png"), dpi=600)
    plt.close()


def process_files(file_dir: str):
    print("kai1")
    only_txt_files = [
        os.path.join(os.getcwd(), file_dir, f)
        for f in os.listdir(os.path.join(os.getcwd(), file_dir))
        if f.endswith(".txt")
    ]
    print("kai2")
    for f in only_txt_files:
        generate_graph(f)
        print("finish a row")


def main():
    process_files(file_dir="test")


if __name__ == "__main__":
    main()
