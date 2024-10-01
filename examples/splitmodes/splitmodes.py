from pathlib import Path
from sys import argv
from sys import stderr
from PIL import Image

def read_images(input_dir):
    files = input_dir.glob("*.png")
    # TODO: add validation and exceptions
    # 1.* points of the spec
    return list(files)

if __name__ == "__main__":
    # 1. The program accepts as input a folder containing PNG image
    # 2. Collect all valid images from dir -> path_list
    # If I call this program with
    # python splitmodes.py /my/images/
    # argv[1] will contain "/my/images"
    try:
        input_dir = Path(argv[1])
    except IndexError:
        print("Usage: <input dir>", file=stderr)
        exit(1)

    img_list = read_images(input_dir)
    # TODO: Use logging library to debug-log the 
    #       content of img_list

    # 3. Create the output folder at the same level as the 
    #     input folder and name it as input folder + suffix "_channels"
    out_dir = Path(str(input_dir.absolute()) + "_channels")
    try:
        out_dir.mkdir()
    except FileExistsError:
        print(f"Output dir {out_dir} already exists.")
        exit(1)


    # HINT: you need to install the `pillow` library and find how 
    # to read images in the documentation

    # im = Image.open("hopper.ppm")
    # im.save("out.png")

    # 4. Loop over valid images
    chan_to_idx = {0: "R", 1: "G", 2: "B"}

    for img_file in img_list:
        im = Image.open(img_file)
        channels = im.split()

        for i, c in enumerate(channels):
            try:
                out_file = out_dir / f"{img_file.stem}_{chan_to_idx[i]}.png"
            except KeyError as e:
                print("discaring alpha channel", file=stderr)
                break
            c.save(out_file)
    exit(0)
