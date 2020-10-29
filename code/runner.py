import os.path,sys
import pypandoc

name=sys.argv[1]
fmt=sys.argv[2]
type=sys.argv[3]

src=name+'.'+fmt
des=name+'.'+type

if type in ['docx','doc','html','pdf']:
    pypandoc.convert_file(src,type,outputfile=des)
else:
    pypandoc.convert_file(src,type,outputfile=des,extra_args=['-V ','mainfont="Microsoft YaHei"','--template=pm-template.latex', '--pdf-engine=xelatex'])

print("success!")