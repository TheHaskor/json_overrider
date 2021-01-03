import sys
import json

resources_file = 'packages.json'
# to override the resources file use: key new_path


def get_dict_from_file():
    with open(resources_file) as f:
        dict_from_file = json.load(f)
    return dict_from_file


def write_dict(new_resources_dict):
    with open(resources_file, 'w') as f:
        json.dump(new_resources_dict, f, indent=4)


if __name__ == '__main__':
    resources_dict = get_dict_from_file()
    inputArgs = sys.argv
    if (len(inputArgs) - 1) % 2 != 0:
        raise Exception(f'command line is incorrect - structure is key_1 path_1  key_2 path_2 ...')

    for i in range(1, len(inputArgs), 2):
        key_arg = inputArgs[i]
        path_arg = inputArgs[i+1]
        if key_arg in resources_dict:
            resources_dict[key_arg] = path_arg
        else:
            raise Exception(f'key {key_arg} is not in packages file')

    write_dict(resources_dict)
