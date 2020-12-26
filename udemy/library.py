#import os
import pathlib

#print(os.getcwd())

#if not os.path.isdir('sample_dir'):
#    os.mkdir('sample_dir')

#if not os.path.exists('sample_dir'):
    #os.mkdir('sample_dir')
#os.makedirs('sample_dir/sample_dir2', exist_ok = True)

#os.rmdir('sample_dir')

#p = pathlib.Path('sample_dir/sample.txt')
#p.touch()

#print(p,type(p))

#with p.open(mode='w') as f:
#    f.write('Good morning\n')

#with p.open(mode='r') as f:
#    print(f.read())

#text = p.read_text()
#print(text)

#count = p.write_text('Good afternoon')
#print(count)

#print(p.exists())
#p.unlink()
#print(p.exists())

#for i in range(10):
#    p= pathlib.Path(f'sample_dir/{i}.txt')
#    p.touch()

p_dir = pathlib.Path('sample_dir')

for p in p_dir.iterdir():
    if p.is_file():
        p.unlink()