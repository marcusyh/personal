import sys
from excel import read_from_excel, write_to_excel
from fetch import copy_files

def check_common(matched, missing):
    lines = {}
    for f, a in matched.items():
        for line in a:
            if line not in lines:
                lines[line] = {"matched": []}
            if "matched" not in lines[line]:
                lines[line]["matched"] = []
            lines[line]['matched'].append(f) 
    for f, a in missing.items():
        for line in a:
            if line not in lines:
                lines[line] = {"missing": []}
            if "missing" not in lines[line]:
                lines[line]["missing"] = []
            lines[line]['missing'].append(f) 
    
    for k, v in lines.items():
        if len(v) >= 2:
            print(k, v)

def convert_to_lines(missing):
    missing_l = {}
    for k, v in missing.items():
        #if not v:
        #    print('\t%s\t%s' %(x, k))
        for x in v:
            if x not in missing_l:
                missing_l[x] = []
            missing_l[x].append(k)
    return missing_l



if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('3 parameters needed.')
        sys.exit(0)
    
    excel_cache, source_files = read_from_excel(sys.argv[3])
    total, unique, finish, missing = copy_files(sys.argv[1], sys.argv[2], source_files)
    finish_lines = write_to_excel(sys.argv[3], finish)
    missing2 = convert_to_lines(missing)
    print('总共%s行%s个文件，排重之后%s个文件，提取了%s个文件%s行，缺失%s行的%s个文件\n' %(len(excel_cache), total, unique, len(finish), finish_lines, len(missing2),len(missing)))
    for k, v in missing2.items():
        if not v:
            print('\t%s\t%s' %(k, v))
        for x in v:
            print('\t%s\t%s' %(k, x))
