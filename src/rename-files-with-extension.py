# coding=utf-8
import os, re, argparse


def rename_images_keeping_size(prefix: str, folder: str, keep_remaining: bool) -> None:
    base_dir = os.path.join(os.path.dirname(__file__), folder)
    list_of_files = os.listdir(base_dir)

    for filename in list_of_files:
        match1 = re.search(r'(\d+x\d+)', filename)
        match2 = re.search(r'(\..*$)', filename)
        size = f'_{match1.group(1)}' if match1 else ''
        extension = match2.group(1) if match2 else False

        if extension:
            current_name = os.path.join(base_dir, filename)
            keeping_name = filename.replace(extension, '') if keep_remaining else ''
            next_name = os.path.join(base_dir, f'{prefix}{size}{keeping_name}{extension}')
            os.rename(current_name, next_name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--prefix', required=True, type=str,
                        help='Texto que precede al tamaño y extensión del archivo que tiene actualmente')
    parser.add_argument('--folder', required=True, type=str,
                        help='Nombre de la carpeta donde se encuentran las imágenes. Debe de estar en la misma carpeta '
                             'que este archivo.')
    parser.add_argument('--keep_name_remaining', default=False, type=str,
                        help='Mantener el nombre restante de la imagen.')
    parser.add_argument('--action', type=str, default='rename-keeping-size',
                        help='Acción a realizar: `rename-keeping-size`.')
    args = vars(parser.parse_args())

    if args['action'] == 'rename-keeping-size':
        rename_images_keeping_size(prefix=args["prefix"], folder=args['folder'],
                                   keep_remaining=(True if args['keep_name_remaining'] else False))


if __name__ == '__main__':
    main()
