# coding=utf-8
import logging
from os import listdir, rename
from os.path import join, dirname, isdir
import re
import argparse
from shutil import copyfile


def get_list_inside_dir_and_dir_path(folder: str) -> None:
    base_dir = join(dirname(__file__), folder)
    list_of_items = listdir(base_dir)

    return base_dir, list_of_items


def get_extension_from_filename(filename: str) -> str:
    match = re.search(r'(\..{3,4})$', filename, re.IGNORECASE)
    return match.group(1) if match else False


def rename_images_keeping_size(prefix: str, folder: str, keep_remaining: bool) -> None:
    base_dir, list_of_items = get_list_inside_dir_and_dir_path(folder=folder)

    for filename in list_of_items:
        match = re.search(r'(\d+x\d+)', filename, re.IGNORECASE)
        size = f'_{match.group(1)}' if match else ''
        extension = get_extension_from_filename(filename=filename)

        if extension:
            logging.info(f'Se va a cambiar el nombre a la imagen `{filename}`')
            current_path = join(base_dir, filename)
            keeping_name = filename.replace(
                extension, '') if keep_remaining else ''
            next_name = f'{prefix}{size}{keeping_name}{extension}'
            next_path = join(base_dir, next_name)
            rename(current_path, next_path)
            logging.info(f'El nuevo nombre es `{next_name}`')


def join_folders_files_in_the_same_folder(folder: str) -> None:
    base_dir, list_of_items = get_list_inside_dir_and_dir_path(folder=folder)

    for folder_name in list_of_items:
        folder_path = join(base_dir, folder_name)

        if isdir(folder_path):
            logging.info(
                f'Encontrada la careta `{folder_name}` dentro de `{folder}`')
            filenames = listdir(folder_path)

            for filename in filenames:
                extension = get_extension_from_filename(filename)
                if extension:
                    previous_path = join(folder_path, filename)
                    next_path = join(base_dir, f'{folder_name}{extension}')
                    copyfile(previous_path, next_path)
                    logging.info(
                        f'El nuevo nombre para `{previous_path}` es `{next_path}`')


def main() -> None:
    logging.getLogger().setLevel(logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', required=True, type=str,
                        help='Nombre de la carpeta donde se encuentran las imágenes o carpetas con las imágenes. Debe'
                        ' de estar en la misma carpeta que este archivo.')
    parser.add_argument('--prefix', default='', type=str,
                        help='Texto que precede al tamaño y extensión del archivo que tiene actualmente')
    parser.add_argument('--keep_name_remaining', default=False, type=str,
                        help='Mantener el nombre restante de la imagen.')
    parser.add_argument('--action', type=str, default='rename-keeping-size',
                        help='Acción a realizar: `rename-keeping-size`.')
    args = vars(parser.parse_args())

    if args['action'] == 'rename-keeping-size':
        rename_images_keeping_size(prefix=args["prefix"], folder=args['folder'],
                                   keep_remaining=(True if args['keep_name_remaining'] else False))
    elif args['action'] == 'join-folders-files-in-the-same-folder':
        join_folders_files_in_the_same_folder(folder=args['folder'])


if __name__ == '__main__':
    main()
