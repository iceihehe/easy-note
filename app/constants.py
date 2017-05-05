# -*- coding: utf-8 -*-


class Code:

    SUCCESS = 10000

    USERNAME_OR_PASSWORD_ERROR = 10001
    NO_SUCH_NOTEBOOK = 10002
    NO_SUCH_NOTE = 10003
    NO_SUCH_USER = 10004
    NO_UPFILE = 10005

    MSG = {
        SUCCESS: '成功',
        USERNAME_OR_PASSWORD_ERROR: '账号或密码错误',
        NO_SUCH_NOTEBOOK: '该笔记本不存在',
        NO_SUCH_NOTE: '该笔记不存在',
        NO_SUCH_USER: '该用户不存在',
        NO_UPFILE: '没有上传文件',
    }
