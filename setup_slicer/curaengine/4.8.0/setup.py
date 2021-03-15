import logging
import os
import requests 

def download_zip(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

if __name__ == '__main__':
    FORMAT = '%(asctime)-15s %(levelname)s: %(message)s'
    DATEFMT = '%d/%m/%Y %H:%M:%S'
    FILENAME = 'slice_new_quotes.log'
    logging.basicConfig(format=FORMAT,
            level=logging.INFO,
            datefmt=DATEFMT)

    SLICER_SERVER_PATH = os.environ.get('3D_SLICER_SERVER_PATH', '/home/ouralgan/3DSliceServer')
    logging.info('Start')

    # PROTOBUF 3.15.6
    logging.info('Download and unzip Protobuf 3.15.6')
    url = 'https://github.com/protocolbuffers/protobuf/releases/download/v3.15.6/protobuf-all-3.15.6.zip'
    path = SLICER_SERVER_PATH + '/setup_slicer/curaengine/4.8.0/protobuf-all-3.15.6.zip'
    try:
        download_zip(url, path)
    except Exception as e:
        logging.error('Download and unzip Protobuf 3.15.6: %s', str(e))
        raise e

    # CURAENGINE 4.8.0
    logging.info('Download and unzip Curaengine 4.8.0')
    url = 'https://github.com/Ultimaker/CuraEngine/archive/4.8.0.zip'
    path = SLICER_SERVER_PATH + '/setup_slicer/curaengine/4.8.0/curaengine-4.8.0.zip'
    try:
        download_zip(url, path)
    except Exception as e:
        logging.error('Download and unzip Curaengine 4.8.0: %s', str(e))
        raise e

