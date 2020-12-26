import shutil
import glob

#shutil.copy('sample_dir1/aaa.txt','sample_dir1/sample_dir2/xxx.txt')
#shutil.copytree('sample_dir1/sample_dir2','sample_dir1/sample_dir3')

#shutil.move('sample_dir1/aaa.txt','sample_dir1/sample_dir2/')
print(glob.glob('sample_dir1/sample_dir2/*'))

shutil.rmtree('sample_dir1/')