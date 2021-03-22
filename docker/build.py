from optparse import OptionParser
import logging
import json
import sys
import yaml

# Le but d e ce script est de generer un docker-compose.yaml qui ne contiendra que les slicers utile
# tres bon point pour un getting started ou on ne manipule pas le docker-compose.yml directement mais
# on utilisera une cli simnple: python build.py --slicer curaengine:4.8 --slicer slic3r:3.1.0

def check_slicer_args(opt_slicers, args):
    # slicer avalaible in json file
    with open('slicers_avalaible.json') as f:
        data = json.load(f)
        slicers_avalaible = []
        for key, value in data.items():
            for v in value:
                slicers_avalaible.append(key + ':' + v)
        for s in opt_slicers:
            if s not in slicers_avalaible:
                raise Exception('Slicer not avalaible: ' + s)

slicer_base = {
    'name':{
        'build':{
            'context': 'context'
        },
        'depends_on':['traefik', 'db'],
        'container_name': 'name',
        'hostname': 'hostname',
        'image': 'image_name',
        'env_file': 'env_path',
        'networks': ['db', 'traefik-inside']
    }
}

if __name__ == '__main__':
    # logging
    FORMAT = '%(asctime)-15s %(levelname)s: %(message)s'
    DATEFMT = '%d/%m/%Y %H:%M:%S'
    FILENAME = 'slice_new_quotes.log'
    logging.basicConfig(format=FORMAT,
            level=logging.INFO,
            datefmt=DATEFMT)
    logging.info('Start')

    # Optparse
    parser = OptionParser()
    parser.add_option("-s", "--slicer", action='append', dest="slicers",
            help="slicer name and version", metavar="SLICER:VERSION")
    (options, args) = parser.parse_args()

    # check slicers avalaible
    try:
        check_slicer_args(options.slicers, args)
    except Exception as e:
        logging.error(str(e))
        sys.exit(1)

    print(yaml.dump(slicer_base))
