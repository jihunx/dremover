# -*- coding: utf-8 -*-
import os, shutil

# 대상 디렉터리 지정
target_dir1 = r"/home/gd/movie"
target_dir2 = r"/home/gd/tv"
target_dir3 = r"/home/gd/drama"

# 대상 확장자 지정
target_ext = (".mkv", ".mp4", ".avi", ".3gp", ".mpg", ".qt", ".wmv", ".flv", ".webm", ".mov")


# 매개 변수 디렉터리가 특정한 조건에 부합되지 않으면 삭제한다.
def remove_dir(path):
    # 디렉터리 삭제 설정값 지정
    delete = True

    items = os.listdir(path)

    for item in items:
        full_path = os.path.join(path, item)
        # 디렉터리에 아무 것도 없으면 삭제
        if len(items) == 0:
            break
        # 디렉터리 안에 디렉터리가 있다면 삭제 안 함
        elif os.path.isdir(full_path):
            delete = False
            break
        # 디렉터리 안에 대상 확장자의 파일이 있다면 삭제 안 함
        elif os.path.isfile(full_path) and item.endswith(target_ext):
            delete = False
            break
        else:
            continue

    # 디렉터리 삭제 설정값이 True면 디렉터리 삭제
    if delete:
        try:
            print("{} 디렉터리를 삭제합니다.".format(path))
            shutil.rmtree(path)
        except Exception as e:
            print(e)
            print("{} 디렉터리 삭제에 실패했습니다.".format(path))
            pass


# 대상 디렉터리에서 가장 하위 디렉터리 경로를 꺼낸다.
def find_dir(path):
    for root, dirnames, filenames in os.walk(path, topdown=False):
        remove_dir(root)


find_dir(target_dir1)
find_dir(target_dir2)
find_dir(target_dir3)
