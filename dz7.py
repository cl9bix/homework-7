import argparse
import os
import shutil

def main():
    parser = argparse.ArgumentParser(description='Clean up folder')
    parser.add_argument('path', metavar='path', type=str, help='Path to folder')

    args = parser.parse_args()
    path = args.path

    if not os.path.exists(path):
        print(f'Error: Path "{path}" does not exist')
        return

    if not os.path.isdir(path):
        print(f'Error: "{path}" is not a directory')
        return

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Error: Failed to delete "{file_path}". Reason: {e}')
