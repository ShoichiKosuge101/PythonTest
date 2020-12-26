import glob

#print(glob.glob('sample_dir1/*'))
#print(glob.glob('sample_dir1/*.txt'))

print(glob.glob('sample_dir1/**/*.txt',recursive=True))
print(glob.glob('sample_dir1/**/',recursive=True))