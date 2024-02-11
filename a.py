import os
import shutil

USERNAME = "john.appleseed"


def compress_to_epub(source, destination):
    for folder_name in os.listdir(source):
        src_path = os.path.join(source, folder_name)
        if os.path.isdir(src_path) and folder_name.endswith(".epub"):
            shutil.make_archive(os.path.join(destination, folder_name), "zip", src_path)
            os.rename(
                os.path.join(destination, folder_name + ".zip"),
                os.path.join(destination, folder_name),
            )


def main():
    src_folder = "/Users/" + USERNAME + "/Downloads/Books/"
    dest_folder = "/Users/" + USERNAME + "/Downloads/new_epubs/"

    compress_to_epub(src_folder, dest_folder)
