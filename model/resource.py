from pathlib import Path
import resources


def path(file_name):
    return str(
        Path(resources.__file__).parent.joinpath(f'{file_name}').absolute()
    )