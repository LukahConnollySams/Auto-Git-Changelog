import toml
from . import pyproject_file, update_dict


def get_version(pyproject_file: str=pyproject_file) -> str:
    """
    Returns the version stored in the pyproject.toml file.

    Parameters
    ----------
    pyproject_file : str, optional
        Name of file, by default 'pyproject.toml'

    Returns
    -------
    str
        Version tag
    """

    with open(pyproject_file, 'r') as file:
        toml_data = toml.load(file)

    return toml_data['tool']['poetry']['version']


def update_version(updated_version: str, pyproject_file: str=pyproject_file) -> None:
    """
    Updates the version stored in the project's toml file.

    Parameters
    ----------
    updated_version : str
        String of new version number
    pyproject_file : str, optional
        file path of project toml file, by default 'pyproject.toml'
    """

    with open(pyproject_file, 'r') as file:
        toml_data = toml.load(file)

    #update version number in toml file
    toml_data['tool']['poetry']['version'] = updated_version

    #rewrite toml file
    with open(pyproject_file, 'w') as file:
        toml_data = toml.dump(toml_data, file)


def bump_version(commit_message: str) -> str:

    version = get_version()

    major, minor, patch = map(int, version.split('.'))

    #strip all but start of commit message, to compare with dict
    commit_type: str = commit_message.split(':').strip()

    #determine commit semantic type
    if update_dict[commit_type] == 'patch':

        patch += 1

    elif update_dict[commit_type] == 'minor':

        minor += 1
        patch = 0

    elif update_dict[commit_type] == 'major':

        major += 1
        minor = 0
        patch = 0

    #compile new version number into string and update project toml file
    updated_version = f'{major}.{minor}.{patch}'

    update_version(updated_version)

    return updated_version