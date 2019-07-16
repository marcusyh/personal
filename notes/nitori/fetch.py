import os
import sys
import shutil

def get_src_sync_flist(syncfile):
    synclist = {}
    h = open(syncfile, 'r')
    for l in h.readlines():
        f = l.strip().replace('#', '/').replace('\\', '/')
        synclist[f] = synclist.get(f, 0) + 1
    h.close()
    return sum(synclist.values()), list(synclist.keys())


def get_sync_flist(src_dir, synclist):
    syncflist = {
            "match": {},
            "missing": {}
            }
    tmplist = []
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            fpath = os.path.join(root, f)
            if os.path.isfile(fpath):
                tmplist.append(fpath)

    for f in synclist:
        fpath = os.path.join(src_dir, f)

        if os.path.isfile(fpath):
            if fpath in syncflist['match']:
                print(fpath, f)
            syncflist['match'][fpath] = ''
            continue
        
        if f.endswith('.frm'):
            t = f.replace('.frm', '.vb')
            print('replaced %s to %s' %(f, t))
            f = t
        spaths = []
        for spath in tmplist:
            if spath.find(f) >=0:
                spaths.append(spath)
        if not spaths:
            if fpath in syncflist['missing']:
                print(fpath, f)
            syncflist['missing'][f] = ''
        elif len(spaths) == 1:
            if fpath in syncflist['match']:
                print(fpath, f)
            fpath = spaths[0]
            syncflist['match'][fpath] = ''
        else:
            print('\n'.join([x for x in spaths]))

             
    return list(syncflist['match'].keys()), list(syncflist['missing'].keys())


def sync_files(dst_dir, flist):
    for fpath in flist:
        dirname = os.path.join(dst_dir, os.path.dirname(fpath))
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        shutil.copy2(fpath, dirname)


def sync_file(source, destination, syncfile):
    total, synclist = get_src_sync_flist(syncfile)

    source1 = os.path.join(source, '01_本部', '01_VB／Excel')
    source2 = os.path.join(source, '02_店舗', '01_VB／Excel')
    source3 = os.path.join(source, '03_海外拠点', '01_VB／Excel')
    
    if os.path.isdir(source1) or os.path.isdir(source2):
        finishlist2, missinglist = get_sync_flist(source2, synclist)
        sync_files(destination, finishlist2)
        print(source2, len(synclist), len(finishlist2), len(missinglist))

        finishlist1, missinglist = get_sync_flist(source1, missinglist)
        sync_files(destination, finishlist1)
        print(source1, len(synclist), len(finishlist1), len(missinglist))
        
        finishlist3, missinglist = get_sync_flist(source3, missinglist)
        sync_files(destination, finishlist3)
        print(source3, len(synclist), len(finishlist3), len(missinglist))
        
        return total, len(synclist), finishlist2 + finishlist1 + finishlist3, missinglist


    finishlist, missinglist = get_sync_flist(source, synclist)
    sync_files(destination, finishlist)
    return total, len(synclist), finishlist, missinglist



if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('3 parameters needed.')
        sys.exit(0)
    total, unique, finish, missing = sync_file(sys.argv[1], sys.argv[2], sys.argv[3])
    print('总共%s行，排重之后%s个，提取了%s个，%s个缺失\n' %(total, unique, len(finish), len(missing)))
    for f in missing:
        print('\t%s' %f)


