import tarfile

with tarfile.open('tar_sample.tar.gz','r:gz') as tr:
    tr.extractall('tar_sample')