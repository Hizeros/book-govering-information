#!/user/bin/python
# -*- coding: utf-8 -*-

# 创建一个空字典用于接收缓存的图书数据



# 引入time模块
import time

# 通过时间戳自动生成图书编号
def _get_book_id(book_id):
    if book_id and book_id in cache:
        return book_id
    return str(time.time())

# 增加图书
def add():
    id_book = _get_book_id
    name_book = input('请输入书名：')
    author_book = input('请输入作者：')
    type_book = input('请输入种类：')
    num_book = int(input('请输入数量：'))
    global surplus_book
    surplus_book += num_book
    # 将图书信息以字典的方式存储
    book_information = {'编号':id_book,'书名':name_book,'作者':author_book,'种类':type_book,'增加数量':num_book,'剩余数量':surplus_book}
    with open("book_govering_information.txt","a",encoding="UTF-8")as f:
        f.write(str(book_information))


# 删除图书
def delete():
    pass

# 修改图书注释
def change():
    pass

# 查询图书
def query():
    pass

# 展示所有图书信息
def show():
    pass

#功能菜单
def menu():
    pass

# 主程序，选择需要执行程序
def main():
    pass
