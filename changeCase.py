# -*- coding: utf-8 -*-
import json
import re

result = {
    "items": [
    ]
}


# 解析单词
def parseKeyword(keywork):
    # 下划线 分隔
    keywork = keywork.replace("_", " ")
    # 中杠 分隔
    keywork = keywork.replace("-", " ")
    # 首字母大写分隔
    k = ""
    for index in range(len(keywork)):
        char = keywork[index]
        if char.isupper():
            k = k + ' '
        k = k + char
    keywork = k

    # 空格分隔
    argv = keywork.split()

    # 转为 首字母大写 capitalize()
    for item in range(len(argv)):
        argv[item] = argv[item].capitalize()

    return argv


def buildUppercase(argv):
    keyword = ''
    for item in argv:
        keyword = keyword + item.upper() + '_'
    uppercase = keyword[0:-1]
    return {
        "title": "常量",
        "subtitle": "转换为常量：'%s'" % uppercase,   # 输出结果
        "arg": "%s" % uppercase,
        "icon": "uppercase.png"
    }


def buildSnakecase(argv):
    keyword = ''
    for item in argv:
        keyword = keyword + item.lower() + '_'
    snakecase = keyword[0:-1]
    return {
        "title": "下划线式",
        "subtitle": "转换为下划线式：'%s'" % (snakecase),
        "arg": "%s" % (snakecase),
        "icon": "snakecase.png"
    }


def buildClasscase(argv):
    keyword = ''
    for item in argv:
        keyword = keyword + item
    classcase = keyword
    return {
        "title": "类名",
        "subtitle": "转换为类命：'%s'" % classcase,
        "arg": "%s" % classcase,
        "icon": "classcase.png"
    }


def buildCamelcase(argv):
    flag = True
    keyword = ''
    for item in argv:
        if flag == True:
            flag = False
            item = item.lower()
        keyword = keyword + item

    camelcase = keyword
    return {
        "title": "驼峰式",
        "subtitle": "转换为驼峰式：'%s'" % camelcase,
        "arg": "%s" % camelcase,
        "icon": "camelcase.png"
    }


def buildKebabcase(argv):
    keyword = ''
    for item in argv:
        keyword = keyword + item.lower() + '-'
    kebabcase = keyword[0:-1]
    return {
        "title": "中杠式",
        "subtitle": "转换为中杠式：'%s'" % kebabcase,
        "arg": "%s" % kebabcase,
        "icon": "kebabcase.png"
    }


def buildLowercase(argv):
    keyword = ''
    for item in argv:
        keyword = keyword + item.lower() + ' '
    lowercase = keyword[0:-1]
    return {
        "title": "单词",
        "subtitle": "转换为单词：'%s'" % lowercase,
        "arg": "%s" % lowercase,
        "icon": "lowercase.png"
    }


# 输出最终结果
def outResult(keyword):
    argv = parseKeyword(keyword)
    result["items"].append(buildUppercase(argv))
    result["items"].append(buildSnakecase(argv))
    result["items"].append(buildClasscase(argv))
    result["items"].append(buildCamelcase(argv))
    result["items"].append(buildKebabcase(argv))
    result["items"].append(buildLowercase(argv))

    print json.dumps(result)


if __name__ == '__main__':
    outResult(
        "AbcDeFGhiijdfKBdre-gfg-hfh-dfd- er-er  -ere_vd-ser-_fb_dggergrxhdtgh-gh-fg-h-hf")
