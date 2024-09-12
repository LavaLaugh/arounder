import glob
import os
import zipfile
import shutil
import pathlib

path = glob.glob("*.cbz")

for file in path:
    folder = file.replace(".cbz", "")

    print("INFO: Creating folders for " + folder)
    tempfolder = folder + "temp"
    os.makedirs(tempfolder)
    os.makedirs(folder)

    print("INFO: Unzipping " + file)
    zip_ref = zipfile.ZipFile(file, 'r')
    zip_ref.extractall(tempfolder)

    temppath = glob.glob(tempfolder + "/*.avif")
    temppath.sort(reverse=True)
    oldnum = len(path) - 1
    lennum = len(str(oldnum))
    newnum = 0

    print("INFO: Renaming files")
    for tempfile in temppath:
        shutil.copyfile(tempfile, folder + "/" + str(newnum).zfill(lennum) + ".avif")
        newnum += 1

    print("INFO: Creating new cbz archive for " + folder)
    shutil.make_archive(folder, "zip", folder)

    print("INFO: Cleaning up")
    os.remove(folder)
    os.remove(file)
    shutil.rmtree(tempfolder)

    print("INFO: Renaming ZIP to CBZ for " + folder)
    p = pathlib.Path(folder + ".zip")
    p.rename(p.with_suffix(".cbz"))
