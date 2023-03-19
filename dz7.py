from setuptools import setup, find_packages

setup(
    name="clean_folder",
    version="1.0.0",
    author="Ваше ім'я",
    author_email="ваша електронна пошта",
    description="Python-пакет для очищення папки",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main'
        ]
    },
)
