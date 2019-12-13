import re
import os

import sys 
reload(sys)
sys.setdefaultencoding('utf8')

def get_arg_by_idx(args, idx = 1):
    arg = None
    if len(args) > idx:
        if args[idx] != 'None':
            arg = args[idx]
    return arg

def main(args):
    dir_path = get_arg_by_idx(args, 1)
    file_object = open('string.txt', 'a')
    for root,dirs,files in os.walk(dir_path): 
        for file_name in files:
            if os.path.splitext(file_name)[1] == '.ts':
                file_path = os.path.join(root, file_name)
                file = open(file_path, 'r')
                file_content = file.read()
                file.close()
                print "----------------------------" + file_name + "----------------------------"
                file_object.write("----------------------------" + file_name + "----------------------------\n")
                mth=re.findall('"(.*?)"', file_content)
                for m in mth:
                    file_object.write(m+"\n")
    file_object.close()

if __name__ == '__main__':
    main(sys.argv)