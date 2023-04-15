#!/user/bin/python
# -*- coding: utf-8 -*-
def gen_request(request):
    '''
    1.图书信息基本操作：增加、删除、修改、查询、展示所有图书信息
    2.通过文件存储图书信息
    3.图书具有作者、书名、出版社等属性
    '''
    pass
import os

# 创建一个空字典用于接收缓存的图书数据
from cushy_storage import CushyDict

cache = CushyDict('./data')
cache['book_list'] = [
                      {"id_book":1,"name_book":"大一下语文","author":"xiaolai"},
                      {"id_book":2,"name_book":"大一下数学","author":"zinan"}
                     ]





# 引入time模块
import time

# 通过时间戳自动生成图书编号
def _get_book_id(book_id):
    if book_id and book_id in cache:
        return book_id
    return str(time.time())

# 增加图书
def add_book():
    id_book = _get_book_id
    name_book = input('请输入书名：')
    author_book = input('请输入作者：')
    type_book = input('请输入种类：')
    publish_book = input('请输入出版社：')
    num_book = int(input('请输入数量：'))
    global surplus_book
    surplus_book += num_book
    # 将图书信息以字典的方式存储
    ret = cache['book_list']
    ret.append({"id":id_book,"book_name":name_book,"author":author_book,"type":type_book,"publish":publish_book,"num":num_book,"surplus":surplus_book})
    cache['book_list'] = ret

    '''global book_information
    book_information = {'编号':id_book,'书名':name_book,'作者':author_book,'种类':type_book,'出版社':publish_book,'增加数量':num_book,'剩余数量':surplus_book}
    '''

    with open("book_govering_information.txt","a",encoding="UTF-8")as f:
        if os.path.getsize('book_govering_information.txt') != 0:
            f.write
        f.write(str(cache['book_list']))


# 删除图书
def delete():
    del_id = int(input("请输入删除图书的编号："))
# 把文件信息全部提取出来
    with open("book_govering_information.txt","r") as f:
        f.readlines
# 循环查找想要编号的那一项
# 找到那一项之后把那一项删除
# 把删掉一项信息后的book_inf覆盖存储到文件中


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
