import shutil
import sys


ARGS = {{ cookiecutter }}


def validate_dirname():
    dir_name = ARGS['dir_name']
    if dir_name != dir_name.lower().replace(' ', ''):
        print('Invalid dir name. Remove all spaces and uppercase characters.')
        sys.exit(1)


def remove_files():
    """Executes after file structure is generated. Directory names with
    jinja `if` statements were causing unexpected behavior at times. Remove
    directories that the user chose to exclude.
    """
    for dir_ in ['apps', 'reports']:
        if ARGS[dir_] == 'no':
            shutil.rmtree(dir_)
        # Validate inputs and stop build if not recognized.
        elif ARGS[dir_] != 'yes':
            print(f'Invalid choice for {dir_}: {ARGS[dir_]}')
            sys.exit(1)


def main():
    validate_dirname()
    remove_files()


if __name__ == '__main__':
    main()

