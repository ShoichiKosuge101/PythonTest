import os
import pathlib

os.makedirs('sample_dir1/sample_dir2', exist_ok=True)

chrs = ['a','b','c','d']

for ch in chrs:
    pathlib.Path(f'sample_dir1/{ch * 3}.txt').touch()

pathlib.Path('sample_dir1/sample_dir2/eee.txt').touch()
pathlib.Path('sample_dir1/fff.csv').touch()
