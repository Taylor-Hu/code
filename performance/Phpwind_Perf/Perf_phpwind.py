import requests, re, random
from performance.Phpwind_Perf.common import *

class PhpwindTest:
    def __init__(self):
        self.session = requests.session()
        self.fid = []
        self.verifycode = ''

    def home(self):
        resp = self.session.get('http://192.168.80.128/phpwind/index.php')
        resp.encoding = 'utf-8'
        self.fid = re.findall('thread\.php\?fid=(.+?)" id="fn', resp.text)
        download(self.session, resp.text)


    def login(self):
        # data = post_2_dict('forward=&jumpurl=http%3A%2F%2Flocalhost%2Fphpwind%2F&step=2&lgt=0&pwuser=pyuser_1&pwpwd=123456&hideid=0&cktime=31536000')
        data = {'forward': '', 'jumpurl': 'http%3A%2F%2Flocalhost%2Fphpwind%2F', 'step': '2', 'lgt': '0',
                'pwuser': 'pyuser_1', 'pwpwd': '123456', 'hideid': '0', 'cktime': '31536000'}
        resp = self.session.post('http://192.168.80.128/phpwind/login.php?', data=data)
        resp.encoding = 'utf-8'
        if '您已经顺利登录' in resp.text:
            print("登录成功")
        else:
            print("登录失败")

    def go_post(self):
        # 发正式发帖之前，先获取到POST请求中的verify隐藏表单的值
        resp = self.session.get('http://192.168.80.128/phpwind/post.php?fid=2')
        express = "verify\" value=\"(.*)\" />"
        list = re.findall(express, resp.text)
        self.verifycode = list[0]

    @monitor('发帖', 3, 1)
    def post(self):
        randseq = random.randint(10000, 99999)
        randfid = random.randint(2, 11)     # 版块编号必须连续，只能针对当前这个论坛
        print(randfid)

        data = {'magicname': '', 'magicid': '', 'verify': self.verifycode, 'atc_title': '这是一个Python帖子标题-%d' % randseq,
                'atc_iconid': 0,
                'atc_content': '这是一个Python帖子内容-%d' % randseq, 'atc_autourl': 1, 'atc_usesign': 1, 'atc_convert': 1,
                'atc_rvrc': 0,
                'atc_enhidetype': 'rvrc', 'atc_money': 0, 'atc_credittype': 'money', 'atc_desc1': '', 'att_special1': 0,
                'att_ctype1': 'money', 'atc_needrvrc1': 0, 'step': 2, 'pid': '', 'action': 'new', 'fid': randfid, 'tid': '',
                'article': 0, 'special': 0, }
        resp = self.session.post('http://192.168.80.128/phpwind/post.php?', data=data)
        resp.encoding = 'utf-8'
        if '发帖完毕点击进入主题列表' in resp.text:
            print("发帖成功")
        else:
            print("发帖失败")

    @monitor('发帖', 3, 1)
    def post2(self):
        randseq = random.randint(10000, 99999)
        randfid = random.choice(self.fid)
        print(randfid)

        data = {'magicname': '', 'magicid': '', 'verify': self.verifycode, 'atc_title': '这是一个Python帖子标题-%d' % randseq,
                'atc_iconid': 0,
                'atc_content': '这是一个Python帖子内容-%d' % randseq, 'atc_autourl': 1, 'atc_usesign': 1, 'atc_convert': 1,
                'atc_rvrc': 0,
                'atc_enhidetype': 'rvrc', 'atc_money': 0, 'atc_credittype': 'money', 'atc_desc1': '', 'att_special1': 0,
                'att_ctype1': 'money', 'atc_needrvrc1': 0, 'step': 2, 'pid': '', 'action': 'new', 'fid': randfid,
                'tid': '',
                'article': 0, 'special': 0, }
        resp = self.session.post('http://192.168.80.128/phpwind/post.php?', data=data)
        resp.encoding = 'utf-8'
        if '发帖完毕点击进入主题列表' in resp.text:
            print("发帖成功")
        else:
            print("发帖失败")

    # select fid from pw_forums ORDER BY RAND() limit 0,1 从数据库中随机查询一条版块编号
    @monitor('发帖', 3, 1)
    def post2(self):
        pass


    # 实现随机回帖，从页面的响应中查找fid和tid
    @monitor('发帖', 1, 1)
    def reply(self):
        randseq = random.randint(10000, 99999)
        randfid = random.choice(self.fid)

        resp = self.session.get('http://localhost/phpwind/thread.php?fid=%s' % randfid)
        list = re.findall('read\.php\?tid=(.+?)" target="_blank"', resp.text)
        randtid = random.choice(list)
        print(randtid)

        data = {'verify': self.verifycode, 'atc_title': 're:这是一个Python帖子标题-%d' % randseq,
                'atc_content': 're:这是一个Python帖子内容-%d' % randseq, 'atc_autourl': 1, 'atc_usesign': 1, 'atc_convert': 1,
                'atc_rvrc': 0, 'atc_money': 0, 'atc_desc1': '', 'att_special1': 0,
                'att_ctype1': 'money', 'atc_needrvrc1': 0, 'step': 2, 'action': 'reply', 'fid': randfid,
                'tid': randtid, }
        resp = self.session.post('http://localhost/phpwind/post.php?', data=data)
        print(resp.text)


if __name__ == '__main__':
    pt = PhpwindTest()
    pt.home()
    pt.login()
    pt.go_post()
    # pt.post()
    # pt.post2
    pt.reply()


# 今日作业：
# 1. 利用Python代码注册200个账号  10分钟
# 2. 实现发帖功能   10分钟
# 3. 向不同的版块，随机发帖    10分钟
# 4. 利用Python代码实现针对随机一个帖子的回复     30分钟内
# 5. 随机从页面中挑选一个版块，从版块中随机一个页面，再从页面中随机一个帖子，进行回复。


