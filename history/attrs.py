#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MyObject(object):

    def __init__(self,x):
        self.x = x

    def power(self):
        return self.x * self.x

obj = MyObject(3)
print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # ������'x'��
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # ������'y'��
setattr(obj, 'y', 19) # ����һ������'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # ������'y'��
print('getattr(obj, \'y\') =', getattr(obj, 'y')) # ��ȡ����'y'
print('obj.y =', obj.y) # ��ȡ����'y'

print('getattr(obj, \'z\') =',getattr(obj, 'z', 404)) # ��ȡ����'z'����������ڣ�����Ĭ��ֵ404

f = getattr(obj, 'power') # ��ȡ����'power'
print(f)
print(f())