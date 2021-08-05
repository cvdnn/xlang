from xlang import iox
from xlang.iox import SizeType

print(iox.split_path('*.jpg'))

print(iox.get_file_size('/Users/xiot/xiot/54807405-187c3f00-4cb8-11e9-8a8e-8092c5472dc1.gif', SizeType.KB))
