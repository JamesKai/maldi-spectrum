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
    annotate_mz = []
    file_name = os.path.basename(file_path[:-4])

    print("kai3")
    mz, intensity = read_file(f"{file_path}")
    spectrum = sus.MsmsSpectrum(file_name, 1.0, 1, mz, intensity,)
    annotate_mz = set(
        [
            int(m)
            for i, m in zip(spectrum.intensity, spectrum.mz)
            if i / spectrum.intensity.max() >= 0.10
        ]
    )
    smplfy_new_lst = []
    for i in annotate_mz:
        if smplfy_new_lst == [] or abs(smplfy_new_lst[-1] - i) > 3:
            smplfy_new_lst.append(i)

    print(smplfy_new_lst)
    for ano_mz in smplfy_new_lst:
        spectrum.annotate_mz_fragment(
            ano_mz, 1, 3, "Da",
        )
    print("kai4")

    fig, ax = plt.subplots(figsize=(12, 6))
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
    process_files(file_dir="20201030")


if __name__ == "__main__":
    main()
