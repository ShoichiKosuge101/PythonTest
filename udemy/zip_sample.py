import zipfile
import glob

#with zipfile.ZipFile('sample_dir1/sample_zip.zip','w') as zf:
#    for f in glob.glob('sample_dir1/*.txt'):
#        zf.write(f)

#with zipfile.ZipFile('sample_dir1/sample_zip.zip','a') as zf:
#        zf.write('sample_dir1/fff.csv')

with zipfile.ZipFile('sample_dir1/sample_zip.zip') as zf:
        #zf.extractall('sample_dir1/sample_dir2')
        zf.extract('sample_dir1/ddd.txt','sample_dir1/sample_dir2')