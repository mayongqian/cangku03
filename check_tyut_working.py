# encoding: utf-8  
import requests
import sys
import yagmail




WEB_URL = 'http://jwc.tyut.edu.cn/'


def run():

    try:

        page = requests.get(WEB_URL)

        if page.status_code == 200 and page.content.decode("utf-8").find('<title>太原理工大学-教务处</title>') >= 0:

            print("CSDN is working great :)")

        else:

            print("It looks like TYUT is having trouble, some one please take a look at it")

            yag = yagmail.SMTP(user = '1321692006@qq.com', password = 'nwblnqbqvbdfijji', host = 'smtp.qq.com')
            yag.send(to = ['2802370278@qq.com'], subject = '异常', contents = ['主页被篡改，请及时处理'])
            sys.exit(-1)

    except:

        print("It looks like TYUT is having trouble, some one please take a look at it")
        yag = yagmail.SMTP(user = '1321692006@qq.com', password = 'nwblnqbqvbdfijji', host = 'smtp.qq.com')
        yag.send(to = ['2802370278@qq.com'], subject = '异常', contents = ['主页被篡改，请及时处理'])
        sys.exit(-1)
if __name__ == '__main__':

    run()