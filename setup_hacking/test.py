# 피해자 컴퓨터의 디렉토리 목록을 출력해주는 함수
# os.walk는 시작 디렉터리부터 시작하여 그 하위 모든 디렉터리를 차례대로 방문하게 해주는 함수이다.

'''
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py': 
                    print(full_filename)
    except PermissionError:
        pass

search("c:/")

'''

'''
import os
for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.csv':
            print("%s/%s" % (path, filename))
'''
