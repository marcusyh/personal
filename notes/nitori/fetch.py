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
             syncflist['match'][fpath] = ''
             continue

         spaths = []
         for spath in tmplist:
             if spath.find(f) >=0:
                 spaths.append(spath)
         if len(spaths) == 1:
             fpath = spaths[0]
             syncflist['match'][fpath] = ''
         else:
             syncflist['missing'][f] = ''
             if spaths:
                print('\n'.join([x for x in spaths]))

             
    return list(syncflist['match'].keys()), list(syncflist['missing'].keys())


def sync_files(dst_dir, flist):
    for fpath in flist:
        dirname = os.path.join(dst_dir, os.path.dirname(fpath))
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        shutil.copy2(fpath, dirname)


def sync_file(source, destination, syncfile):
    source1 = os.path.join(source, '01_本部', '01_VB／Excel')
    source2 = os.path.join(source, '02_店舗', '01_VB／Excel')
    total, synclist = get_src_sync_flist(syncfile)

    finishlist2, missinglist = get_sync_flist(source2, synclist)
    sync_files(destination, finishlist2)

    finishlist1, missinglist = get_sync_flist(source1, missinglist)
    sync_files(destination, finishlist1)

    return total, len(synclist), finishlist2 + finishlist1, missinglist


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('3 parameters needed.')
        sys.exit(0)
    total, unique, finish, missing = sync_file(sys.argv[1], sys.argv[2], sys.argv[3])
    print('%s lines in total, %s unique, %s files copied successufully, %s files missing.\nThe missing files list here:' %(total, unique, len(finish), len(missing)))
    for f in missing:
        print('\t%s' %f)


