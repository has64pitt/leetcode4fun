import os

file_path = os.path.abspath(__file__)
cur_dir = file_path.rsplit('/', 1)[0]

for i in range(0, 2400, 50):
    istr = str(i).zfill(4)
    iplus49 = str(i+49).zfill(4)
    dirname = cur_dir + '/' + istr + '-' + iplus49
    if not os.path.exists(dirname):
        os.mkdir(dirname)

