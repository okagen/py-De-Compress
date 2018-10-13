# -*- coding: utf-8 -*-

import os
import subprocess
import shutil

# ------------------------------------------------------
# ディレクトリが無ければ作成。
def makeDir(tgtParentDir, newDirName):
    """Make a directory if it isn't exist.
    Arguments:
        tgtParentDir: parent directory of the new direcoty.
        newDirName: name of directory to be created.
    """
    newDir = os.path.join(tgtParentDir, newDirName)
    if not os.path.exists(newDir):
        os.makedirs(newDir)
        
# ------------------------------------------------------
# ディレクトリ削除。サブディレクトリも含む。
def delDir(tgtParentDir, delDirName):
    """Delete an entire directory tree
    Arguments:
        tgtParentDir: parent directory of the directory to be deleted.
        delDirName: name of directory to be deleted. 
    """
    delDir = os.path.join(tgtParentDir, delDirName)
    if os.path.exists(delDir):
        shutil.rmtree(delDir)
        
# ------------------------------------------------------
# 指定した圧縮ファイルの中から、指定した拡張子のファイルを抽出する。
def do_extract(sevenZipExePath, tgtParentDir, cmpressedFileName, extExt, outputDirName):
    """Extract some files from a compressed file by using extension.
    Arguments:
        sevenZipExePath: full path of the 7zip exe(7z.exe).
        tgtParentDir: path of the directory which includes some compressed files.
        cmpressedFileName: name of compressed file which extract some filese form.
            e.g.) 'abc.lzh'
        extExt: file extension which was extracted from the "compressedFileName".
            e.g.) '*.wav'
        outputDirName: name of directory in which the extracted files saved.
    Returns:
        result of subprocess.getoutput(cmd)
    """    
    tgtFile = os.path.join(tgtParentDir, cmpressedFileName)
    extDir = os.path.join(tgtParentDir, outputDirName)
    cmd = '"' + sevenZipExePath +  '"' + ' -aoa e ' \
            +  '"' + tgtFile + '"' \
            + ' -o' + '"' + extDir +  '"' + " " + extExt
    chk = subprocess.getoutput(cmd)
    return chk


# ------------------------------------------------------
# 指定した圧縮ファイルの中から、指定したファイルを抽出する。
def do_extract_file(sevenZipExePath, tgtParentDir, cmpressedFileName, tgtFileName, outputDirName):
    """Extract some files from a compressed file by using extension.
    Arguments:
        sevenZipExePath: full path of the 7zip exe(7z.exe).
        tgtParentDir: path of the directory which includes some compressed files.
        cmpressedFileName: name of compressed file which extract some filese form.
            e.g.) 'abc.lzh'
        tgtFileName: name of file to be extruded.
        outputDirName: name of directory in which the extracted files saved.
    Returns:
        result of subprocess.getoutput(cmd)
    """    
    tgtFile = os.path.join(tgtParentDir, cmpressedFileName)
    extDir = os.path.join(tgtParentDir, outputDirName)
    cmd = '"' + sevenZipExePath +  '"' + ' -aoa e ' \
            +  '"' + tgtFile + '"' \
            + ' -o' + '"' + extDir +  '"' + " " + tgtFileName
    chk = subprocess.getoutput(cmd)
    return chk

# ------------------------------------------------------
# 指定したディレクトリを、指定したファイルの名前で圧縮する。
def do_compress(sevenZipExePath, tgtParentDir, tgtDirName, newCmpFileName):
    """Compress files in the target directory.
    Arguments:
        sevenZipExePath: full path of the 7zip exe(7z.exe).
        tgtParentDir: path of the directory which includes target directory to be compressed.
        tgtDirName: name of directory to be compressed.
        newCmpFileName: name of file after compressed.
    Returns:
        result of subprocess.getoutput(cmd)
    """
    newCmpFile = os.path.join(tgtParentDir, newCmpFileName)
    tgtDir = os.path.join(tgtParentDir, tgtDirName)
    cmd = '"' + sevenZipExePath +  '"' + ' a ' \
            +  '"' + newCmpFile + '"' \
            + ' ' + '"' + tgtDir +  '"'
    chk = subprocess.getoutput(cmd)
    return chk

# ------------------------------------------------------
# 指定したディレクトリ内のファイル数をカウントする。
def countFiles(tgtParentDir, tgtDirName):
    """Count number of files in the target directory.
    Arguments:
        tgtParentDir: path of the directory which includes target directory to be compressed.
        tgtDirName: name of the target directory.
    Returns:
        cntFiles: number of files.
    """    
    tgtDir = os.path.join(tgtParentDir, tgtDirName)
    path, dirs, files = next(os.walk(tgtDir))
    cntFiles = len(files)
    return cntFiles

# ------------------------------------------------------
# 指定したディレクトリ内の指定した拡張子のファイルのリストを取得
def getFileListByExt(tgtDir, tgtExt):
    """Get a list of files which have specified extention in the target directory.
    Arguments:
        tgtDir: full path of the target directory.
        tgtExt: extension of target file.
            e.g.) '.lzh'
    """    
    path, dirs, files = next(os.walk(tgtDir))
    retFiles = []
    for file in files:
        base, ext = os.path.splitext(file)
        if ext == tgtExt:
            retFiles.append(file)
    
    return retFiles



if __name__=='__main__':

    sevenZipExePath = r'C:\Program Files\7-Zip\7z.exe'
    tgtDir = r'C:\work\GitHub\pyCompDecomp\data'
    extWav = '*.wav'
    extLzh = '.lzh'
 
    print()
    print( '===== start new process =====' )
        
    # ------------------------------------------------------
    # 指定したディレクトリ内の指定した拡張子のファイルのリストを取得
    lzhFileList = getFileListByExt(tgtDir, extLzh)
        
    for lzhFileName in lzhFileList:
        #事前準備
        lzhFileName_base, lzhFileName_ext = os.path.splitext(lzhFileName)
        fileName = lzhFileName
        outputDirName = lzhFileName_base
        newFileName = outputDirName + ".zip"

        #print( '-----  start:::,' + fileName)
        
        #一時的にファイルを展開するディレクトリを作成
        delDir(tgtDir, outputDirName)
        makeDir(tgtDir, outputDirName)
    
        #wavファイル抽出
        #print( '-----  extracting' )
        chk = do_extract(sevenZipExePath, tgtDir, fileName, extWav, outputDirName)
        #print( chk )
    
        #一時的に展開したwavファイルの数をカウント
        print('-----,' + fileName + ',,,' + str(countFiles(tgtDir, outputDirName)))
        
        #一時的にファイルを展開したディレクトリをzipで圧縮
        #print( '-----  comressing  -----' )
        chk = do_compress(sevenZipExePath, tgtDir, outputDirName, newFileName)
        #print( chk )
        
        #一時的にファイルを展開したディレクトリを削除
        delDir(tgtDir, outputDirName)
        #print( 'finish  -----' )

    print( '===== finish process =====' )
