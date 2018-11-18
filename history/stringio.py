#from io import StringIO
#f=StringIO()
#f.write('hello world')
#print(f.getvalue())

from io import BytesIO
from io import StringIO

# write to BytesIO:
#f = StringIO()
#f.write('hello')
#f.write(' ')
#f.write('world!')
#print(f.getvalue())

f = StringIO('空山新雨后，\n天气晚来秋。\n明月松间照，\n清泉石上流。')
#while True:
#   s = f.readline()
#    if s == '':
#        break
print(f.read())