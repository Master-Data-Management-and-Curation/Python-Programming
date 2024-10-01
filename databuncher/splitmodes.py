from pathlib import Path
from sys import argv

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
    input_dir = Path(argv[1])
    img_list = read_images(input_dir)
    print(img_list)
    exit(0)

    # 3. Create the output folder at the same level as the 
    out_dir = str(input_dir) + "_channels"


    #     input folder and name it as input folder + suffix "_channels"

    # 4. Loop over valid images
    #     4.1 For each channel
    #         4.1.1 Create the monochromatic image
    #         4.1.2 save it in output dir by using the input file name + suffix (r,g,b)
    exit(0)
