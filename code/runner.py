# coding:utf-8

import os.path
import sys
import pypandoc

name = sys.argv[1]
fmt = sys.argv[2]
type = sys.argv[3]

src = name+'.'+fmt
des = name+'.'+type

if type in ['docx', 'html']:
    pypandoc.convert_file(src, type, outputfile=des)
elif type in ['pdf']:
    pypandoc.convert_file(src, type, outputfile=des, extra_args=[
                          '-s', '--pdf-engine=xelatex', '--template=pm-template.latex', '-V', 'CJKmainfont="FZYanSongS-R-GB"'])
else:
    print("unsupported format!")
    os._exit(0)

print("success!")
