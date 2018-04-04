#! /usr/bin/python
# ! _*_ coding=UTF-8 _*_

'''
try:
    print('try...')
    r = 10/int('20')
    print('result:',r)
except ZeroDivisionError as e:
    print('except:', e)   #if 10/0
except ValueError as e:
    print('ValueError',e)   #if 10/int('a')
else:
    print('no error')   #if 10/2
finally:
    print('finally...')
print('END')
'''

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('q')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()
