import glob
import os
import zipfile
import shutil

path = glob.glob("*.cbz")

for file in path:
    if ".cbz" in file:
        folder = file.replace(".cbz", "")
        tempfolder = folder + "temp"
        os.makedirs(tempfolder)
        os.makedirs(folder)
        zip_ref = zipfile.ZipFile(file, 'r')
        zip_ref.extractall(tempfolder)
        temppath = glob.glob(tempfolder + "/*.avif")
        temppath.sort(reverse=True)
        oldnum = len(path) - 1
        lennum = len(str(oldnum))
        newnum = 0

        for tempfile in temppath:
            shutil.copyfile(tempfile, folder + "/" + str(newnum).zfill(lennum) + ".avif")
            newnum += 1

