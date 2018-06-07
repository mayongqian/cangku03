import requests
import sys
import yagmail




WEB_URL = 'http://www.csdn.net/'


def run():

    try:

        page = requests.get(WEB_URL)

        if page.status_code == 200 and page.content.decode("utf-8").find('<title>CSDN-专业IT技术社区</title>') >= 0:

            print("CSDN is working great :)")

        else:

            print("It looks like CSDN is having trouble, some one please take a look at it")

            yag = yagmail.SMTP(user = '1321692006@qq.com', password = 'nwblnqbqvbdfijji', host = 'smtp.qq.com')
            yag.send(to = ['2802370278@qq.com'], subject = '异常', contents = ['uu'])
            sys.exit(-1)

    except:

        print("It looks like CSDN is having trouble, some one please take a look at it")
        yag = yagmail.SMTP(user = '1321692006@qq.com', password = 'nwblnqbqvbdfijji', host = 'smtp.qq.com')
        sys.exit(-1)
        yag.send(to = ['2802370278@qq.com'], subject = '异常', contents = ['uu'])
if __name__ == '__main__':

    run()
