import os

kThisPath = os.path.dirname(__file__)
kDownloadPath = os.path.join(kThisPath, 'downloads')

kZipFilePath = os.path.join(kDownloadPath, 'state_dicts.zip')
kModelExtractPath = os.path.join(kDownloadPath, 'cifar10_models')

os.makedirs(kModelExtractPath, exist_ok=True)
