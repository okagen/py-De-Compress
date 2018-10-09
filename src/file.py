# -*- coding: utf-8 -*-

import  os
import  subprocess


def do_judge_fileType(f):
    
    return "lha"    
""" 
    args = ['file','-i',f]
    output = subprocess.run(args, stdout=subprocess.PIPE).stdout
    print("[DEBUG] %s" % output.decode('utf-8').lower())
    if 'gzip'.lower() in output.decode('utf-8').lower():
        print("gzip: {0}".format(output))
        return "gzip"
    elif 'bzip2'.lower() in output.decode('utf-8').lower():
        print("bzip2: {0}".format(output))
        return "bzip2"
    elif 'lzh'.lower() in output.decode('utf-8').lower():
        print("lha: {0}".format(output))
        return "lha"
    elif '7z'.lower() in output.decode('utf-8').lower():
        print("7zip: {0}".format(output))
        return "7zip"
    elif 'rar'.lower() in output.decode('utf-8').lower():
        print("rar: {0}".format(output))
        return "rar"
    elif 'cpio'.lower() in output.decode('utf-8').lower():
        print("cpio: {0}".format(output))
        return "cpio"
    elif 'x-archive'.lower() in output.decode('utf-8').lower():
        print("ar: {0}".format(output))
        return "ar"

    # *.tar, *.tgz, *.tar.bz2
    if   tarfile.is_tarfile(f):
        print("tar: {0}".format(f))
        return "tar"
    elif zipfile.is_zipfile(f):
        print("zip: {0}".format(f))
        return "zip"
    else:
        print("%s is not supported." % output)
        return "nil"

"""

# tar, zip, gzip, bz2, lha, 7z, rar, cpio, ar ... の展開

def do_unpack(sevenZipExePath, tgtDir, cmpFileName, extExt, outputDir):
    # 解凍元ファイル　フルパス
    tgtFile = os.path.join(tgtDir, cmpFileName)
    
    # '"C:\Program Files\7-Zip\7z.exe" -aoa e 
    # "C:\work\GitHub\py[De]Compress\data\ARCH-20180618-500050.lzh"
    # -o"C:\work\GitHub\py[De]Compress\data" *.wav'
    cmd = '"' + sevenZipExePath +  '"' + ' -aoa e ' \
            +  '"' + tgtFile + '"' \
            + ' -o' + '"' + outputDir +  '"' + " " + extExt

    chk = subprocess.getoutput(cmd)
    return chk


if __name__=='__main__':

    sevenZipExePath = r'C:\Program Files\7-Zip\7z.exe'
    tgtDir = r'C:\work\GitHub\py[De]Compress\data'
    outputDir = r'C:\work\GitHub\py[De]Compress\data'
    fileName = r'ARCH-20180618-500050.lzh'
    ext = '*.wav'

    chk = do_unpack(sevenZipExePath, tgtDir, fileName, ext, outputDir)
    print( chk )
