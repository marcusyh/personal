import os
import sys
import shutil

def get_source_files(syncfiles):
    syncpool = {}
    for k, v in syncfiles.items():
        f = k.strip().strip('0x000d').replace('#', '/').replace('\\', '/').replace('//', '/')
        if not f:
            continue
        if '.xls/' in f:
            f = f.split('.xls/')[0] + '.xls'
        if '.xlsm/' in f:
            f = f.split('.xlsm/')[0] + '.xlsm'
        if f not in syncpool:
            syncpool[f] = []
        syncpool[f] = syncpool[f] + v
    return syncpool

def get_sync_files(src_dir, syncpool):
    syncfiles = {
            "match": {},
            "missing": {}
            }
    tmplist = []
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            fpath = os.path.join(root, f)
            if os.path.isfile(fpath):
                tmplist.append(fpath)

    for f in syncpool.keys():
        fpath = os.path.join(src_dir, f)
        value = syncpool[f]

        if os.path.isfile(fpath):
            if fpath in syncfiles['match']:
                #print('exists', fpath, f)
                syncfiles['match'][fpath] += value
            else:
                syncfiles['match'][fpath] = value
            continue
        
        if f.endswith('.frm'):
            t = f.replace('.frm', '.vb')
            #print('replaced %s to %s' %(f, t))
            f = t
        spaths = []
        for spath in tmplist:
            if spath.find(f) >=0:
                spaths.append(spath)
        if not spaths:
            if fpath in syncfiles['missing']:
                #print('exists', fpath, f)
                syncfiles['missing'][fpath] += value
            else:
                syncfiles['missing'][f] = value
        elif len(spaths) == 1:
            if fpath in syncfiles['match']:
                #print('exists', fpath, f)
                syncfiles['match'][fpath] += value
            else:
                fpath = spaths[0]
                syncfiles['match'][fpath] = value
        else:
            if fpath in syncfiles['missing']:
                #print('exists', fpath, f)
                syncfiles['missing'][fpath] += value
            else:
                syncfiles['missing'][f] = value
            print(f, value)
            print('\n'.join([x for x in spaths]) + '\n\n')

    return syncfiles['match'], syncfiles['missing']

def sync_files(dst_dir, flist):
    for fpath in flist:
        dirname = os.path.join(dst_dir, os.path.dirname(fpath))
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        shutil.copy2(fpath, dirname)


def copy_files(source, destination, syncfile):
    syncpool = get_source_files(syncfile)
    total = sum([len(x) for x in syncpool.values()])
    unique = len(syncpool)
    
    matched = {}
    for i in ['02_店舗', '03_海外拠点/01_台湾', '01_本部']:
        source_dir = os.path.join(source, i, '103_VB' if i == '03_海外拠点/01_台湾' else '01_VB／Excel')

        if not os.path.isdir(source_dir):
            continue

        a, syncpool = get_sync_files(source_dir, syncpool)
        matched.update(a)

    sync_files(destination, matched.keys())
    return total, unique, matched, syncpool 
