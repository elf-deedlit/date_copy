#!/usr/bin/env python
# vim: set ts=4 sw=4 et smartindent ignorecase fileencoding=utf8:
import argparse
import glob
import os
import shutil
import time

def parse_option():
    parser = argparse.ArgumentParser(description = u'ファイルのタイムスタンプでフォルダを作成して移動する')
    parser.add_argument('--copy', type = bool,
            default = False, help = 'コピーモード')
    parser.add_argument('src', type = str, nargs = 1,
            default = None, help = 'src path')
    parser.add_argument('dest', type = str, nargs = 1,
            default = None, help = 'dest path')

    return parser.parse_args()

def main():
    args = parse_option()
    src_path = args.src[0]
    dest_path = args.dest[0]
    for f in glob.glob(os.path.join(src_path, '*.*')):
        tm = os.path.getctime(f)
        st = time.localtime(tm)
        year = st.tm_year
        month = st.tm_mon
        dpath = os.path.join(dest_path, '{0:04}'.format(year), '{0:02}'.format(month))
        if not os.path.isdir(dpath):
            os.makedirs(dpath)
        if args.copy:
            shutil.copy2(f, dpath)
            print(u'copy {0}->{1}'.format(f, dpath))
        else:
            shutil.move(f, dpath)
            print(u'move {0}->{1}'.format(f, dpath))

if __name__ == '__main__':
    main()