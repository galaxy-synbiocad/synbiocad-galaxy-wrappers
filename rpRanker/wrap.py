from argparse import ArgumentParser
from rptools.rplibs import rpPathway


def read_args():
    parser = ArgumentParser()
    parser.add_argument(
        '--pathways',
        required=True,
        type='str',
        nargs='+',
        help='show the version number and exit'
    )
    parser.add_argument(
        '--data_outdir',
        required=True,
        type='str',
        help='show the version number and exit'
    )
    return parser.parse_args()


def entry_point():
    args = read_args()
    pathways = {}
    for infile in args.pathways:
        pathways[infile] = rpPathway.from_rpSBML(infile).get_global_score()
    sorted_pathways = sorted(pathways.items(), key=lambda item: item[1])
    print(
        '\n'.join(sorted_pathways)
    )
    return sorted_pathways()


def _cli():
    entry_point()
    return 0


if __name__ == '__main__':
    _cli()
