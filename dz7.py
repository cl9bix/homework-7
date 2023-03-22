
from clean_folder.clean_folder.clean import sort_files
import argparse

parser = argparse.ArgumentParser(description='Clean folder utiliti')
parser.add_argument('folder_path', type=str, help='Path to folder')
args = parser.parse_args()

if __name__ == '__main__':
    sort_files(args.folder_path)


from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder=clean_folder.clean_folder.clean:sort_files'
        ]
    }
)

