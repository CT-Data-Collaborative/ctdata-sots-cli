from os import listdir, rename
import zipfile

def prep_release_files(path_to_zips):
    zips = [f for f in listdir(path_to_zips)
            if f.split('.')[1] == 'ZIP']

    for z in zips:
        print(z)
        dir_name = path_to_zips + z.split('.')[0]
        zipfile_path = path_to_zips + z
        zip_ref = zipfile.ZipFile(zipfile_path, 'r')
        zip_ref.extractall(path_to_zips)
        rename(path_to_zips + 'SSP', dir_name)
        zip_ref.close()
