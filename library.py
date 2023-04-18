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
import json
# 引入json模块，进行解析

"""
# 创建一个空字典用于接收缓存的图书数据，后续使用cushy-storage库进行数据缓存-----功能待开发
from cushy_storage import CushyDict

cache = CushyDict('./data')
cache['book_list'] = [
                      {"id_book":1,"name_book":"大一下语文","author":"xiaolai"},
                      {"id_book":2,"name_book":"大一下数学","author":"zinan"}
                     ]
"""

# 引入time模块
import time
# 通过时间戳自动生成图书编号
def _get_book_id():
    """
    # 判断book_id是否重复
    if book_id and book_id in cache:
        return book_id
    """
    return str(time.time())

# 增加图书
def add_book():
    id_book = _get_book_id()
    name_book = input('请输入书名：')
    author_book = input('请输入作者：')
    type_book = input('请输入种类：')
    publish_book = input('请输入出版社：')
    num_book = int(input('请输入数量：'))

    '''
    自动计算图书剩余数量--待开发
    global surplus_book
    surplus_book += num_book
    '''
    # 将图书信息以字典的方式存储
    '''
    引用cushy-stroage存储图书信息
    ret = cache['book_list']
    ret.append({"id":id_book,"book_name":name_book,"author":author_book,"type":type_book,"publish":publish_book,"num":num_book})
    cache['book_list'] = ret
    '''

    book_information = {"编号":id_book,"书名":name_book,"作者":author_book,"种类":type_book,"出版社":publish_book,"增加数量":num_book}

    with open("book_govering_information.txt","a",encoding="UTF-8") as f:
        # 换行\n保证数据在文件中按行存储，这样查询时用f.readlines()才能正常查询
        '''
        # 通过内置函数达到换行操作
        if os.path.getsize('book_govering_information.txt') != 0:
            f.write('\n')
        '''
        # 通过json模块写入文件并且换行
        f.write(json.dumps(book_information)+'\n')
    return "添加成功！"



# 删除图书
def delete_book():
    del_name = input("请输入删除图书的书名：")
    del_author = input("请输入删除图书的作者：")
    del_id = int(input("请输入删除的图书的编号"))
    inf_list=[]
    # 把文件信息全部提取出来
    with open("book_govering_information.txt","r", encoding='utf-8') as f:
        # 因为文件读取为一个字符串列表，所以要先将其解析为字典类型方可使用key查找书名、作者等，使用json模块
        for line in f:
            inf_list.append(json.loads(line))
        new_inf_list=[]
        # 循环查找想要想要删除的书名或作者
        for temp in inf_list:
            if del_name == temp["书名"] or del_author == temp["作者"] or del_id == temp["编号"]:
                # 找到那一项之后跳过这一项
                continue
            # 将其余项重新添加到新的列表中
            new_inf_list.append(temp)
    # 把删掉一项信息后的new_inf_list覆盖存储到文件中
    with open("book_govering_information.txt", "w",encoding='utf-8') as f:
        for temp in new_inf_list:
            f.write(json.dumps(temp)+'\n') # 注意存储时一定要是字符串格式,换行存储让文件更容易读取
    return "删除成功"

# 修改图书信息
def change_book():
    cha_name = input("请输入修改的图书书名：")
    # cha_id = int(input("请输入修改的图书编号："))
    inf_list = []
    with open("book_govering_information.txt","r", encoding='utf-8') as f:
        for line in f:
            inf_list.append(json.loads(line))
        new_inf_list = []
        for temp in inf_list:
            if cha_name == temp["书名"]:
                cha_inf = input("请输入想要修改的关键词：")
                value_cha = input("请输入想要修改成的信息：")
                temp[cha_inf] = value_cha
            new_inf_list.append(temp)
    with open("book_govering_information.txt", "w", encoding='utf-8') as f:
        for temp in new_inf_list:
            f.write(json.dumps(temp)+'\n')
    return "修改成功！"

# 查询图书
def query_book():
    qu_name = input("请输入查询的图书书名：")
    qu_author = input("请输入查询的图书作者：")
    inf_list = []
    with open("book_govering_information.txt","r",encoding='utf-8') as f:
        for line in f:
            inf_list.append(json.loads(line))
        for temp in inf_list:
            if qu_name == temp["书名"] or qu_author == temp["作者"]:
                print(temp)
    return "查询成功！"

# 展示所有图书信息
def show_book():
    print("***所有图书信息***")
    inf_list = []
    with open("book_govering_information.txt", "r", encoding='utf-8') as f:
        for line in f:
            inf_list.append(json.loads(line))
        for temp in inf_list:
            print(temp)
    return "展示成功！"

#功能菜单
def menu():
    pass

# 主程序，选择需要执行程序
def main():
    pass
