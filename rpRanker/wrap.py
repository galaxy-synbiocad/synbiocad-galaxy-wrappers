from argparse import ArgumentParser
from rptools.rplibs import rpPathway


def read_args():
    parser = ArgumentParser()
    parser.add_argument(
        '--pathways',
        required=True,
        type=str,
        nargs='+',
        help='Pathways (rpSBML) to rank'
    )
    parser.add_argument(
        '--sorted_pathways',
        required=True,
        type=str,
        help='Filename which contains the list of sorted pathways'
    )
    return parser.parse_args()


def entry_point():
    args = read_args()
    pathways = {}
    for infile in args.pathways:
        pathway = rpPathway.from_rpSBML(infile)
        pathways[f'{pathway.get_id()} {infile} {pathway.get_global_score()}'] = pathway.get_global_score()
    sorted_pathways = dict(sorted(pathways.items(), key=lambda item: item[1]))
    sorted_pathways_str = '\n'.join(sorted_pathways.keys())
    print('Sorted Pathways')
    print('===============')
    print(sorted_pathways_str)
    f = open(args.sorted_pathways, 'w')
    f.write(sorted_pathways_str)
    f.close()
    return sorted_pathways


def _cli():
    entry_point()
    return 0


if __name__ == '__main__':
    _cli()
