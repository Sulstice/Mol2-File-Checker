# -*- coding: utf-8 -*-
#
# Mol2 Check File
#
# ------------------------------------------------


# imports
# -------
from progress.bar import Bar
from argparse import ArgumentParser
from biopandas.mol2 import PandasMol2

class Mol2File(object):

    def __init__(self):


if __name__ == '__main__':

    parser = ArgumentParser(
        description='Parsing the Mol2 File used for checking')
    parser.add_argument("infile", type=str, help="Mol2 File")
    args = parser.parse_args()


    pmol = PandasMol2().read_mol2(args.infile)

    print('Molecule ID: %s' % pmol.df)
