import requests, zipfile, os
from tqdm import tqdm

from cifar10_paths import kZipFilePath, kModelExtractPath

kURL = "https://rutgers.box.com/shared/static/y9wi8ic7bshe2nn63prj9vsea7wibd4x.zip"

def main():
    fresh_download = False
    if os.path.isfile(kZipFilePath):
        print(f'File {kZipFilePath} already exists, skipping download!')
    else:
        # Streaming, so we can iterate over the response.
        r = requests.get(kURL, stream=True)

        # Total size in Mebibyte
        total_size = int(r.headers.get('content-length', 0))
        block_size = 2**20 # Mebibyte
        t=tqdm(total=total_size, unit='MiB', unit_scale=True)

        with open(kZipFilePath, 'wb') as f:
            for data in r.iter_content(block_size):
                t.update(len(data))
                f.write(data)
        t.close()

        if total_size != 0 and t.n != total_size:
            raise Exception('Error, something went wrong')

        print('Download successful. Unzipping file.')
        fresh_download = True

    if not os.path.isdir(kModelExtractPath) or fresh_download:
        # path_to_zip_file = os.path.join(os.getcwd(), 'state_dicts.zip')
        # directory_to_extract_to = os.path.join(os.getcwd(), 'cifar10_models')
        with zipfile.ZipFile(kZipFilePath, 'r') as zip_ref:
            zip_ref.extractall(kModelExtractPath)
            print('Unzip file successful!')
    else:
        print(f'Directory {kModelExtractPath} already exists and nothing new',
              'was downloaded. Skipping extraction!')

if __name__ == '__main__':
    main()
