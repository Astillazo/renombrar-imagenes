import os, re, sys, argparse


parser = argparse.ArgumentParser()
parser.add_argument('--prefix', required=True, type=str, help='Texto que precede al tamaño y extensión del archivo que tiene actualmente')
parser.add_argument('--folder', required=True, type=str, help='Nombre de la carpeta donde se encuentran las imágenes. Debe de estar en la misma carpeta que este archivo.')
args = vars(parser.parse_args())

base_dir = os.path.join(os.path.dirname(__file__), args['folder'])
list_of_files = os.listdir(base_dir)

for filename in list_of_files:
    match1 = re.search(r'(\d+x\d+)', filename)
    match2 = re.search(r'(\..*$)', filename)
    size = match1.group(1) if match1 else False
    extension = match2.group(1) if match2 else False

    if size and extension:
        current_name = os.path.join(base_dir, filename)
        next_name = os.path.join(base_dir, f'{args["prefix"]}_{size}{extension}')
        os.rename(current_name, next_name)
