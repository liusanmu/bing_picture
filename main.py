import requests
from bs4 import BeautifulSoup
import threading
import time

page = 1
# 线程池数量
pools = 10


class Http(threading.Thread):

    def __init__(self, page):
        threading.Thread.__init__(self)
        self.page = page


    # 爬去bing壁纸
    def run(self):
        global images
        resp = requests.get("https://bing.ioliu.cn/?p=" + str(self.page))

        print("https://bing.ioliu.cn/?p=" + str(self.page))
        soup = BeautifulSoup(resp.text, 'lxml')
        a_s = soup.find_all('a', class_='mark')
        for a in a_s:
            # print()
            image_name = a.attrs['href']
            images_name = image_name.split('/')
            image_name = images_name[2]
            image_name = image_name.split('?')[0] + "_640x360.jpg"
            url = 'http://h1.ioliu.cn/bing/' + image_name
            # images.append()
            print("下载文件:" + url)
            ir = requests.get(url)

            if ir.status_code == 200:
                im = open("C:/Users/Administrator/PycharmProjects/bing_picture/images/" + str(time.time()) + ".jpg", 'wb+')

                im.write(ir.content)
                im.flush()
                im.close()
            else:
                image_name = a.attrs['href']
                images_name = image_name.split('/')
                image_name = images_name[2]
                image_name = image_name.split('?')[0] + "_1920x1080.jpg"
                url = 'http://h1.ioliu.cn/bing/' + image_name
                print("下载文件:" + url)
                ir = requests.get(url)

                if ir.status_code == 200:
                    im = open("C:/Users/Administrator/PycharmProjects/bing_picture/images/" + str(time.time()) + ".jpg",
                              'wb+')

                    im.write(ir.content)
                    im.flush()
                    im.close()
                else:
                    print("error:" + url)

        # if page == 65:
        #     write_file()
        # print(a_s)


def thread_pool():
    global page
    pools_new = 0

    over = True

    while over:
        if (pools_new < pools):
            Http(page=page).start()
            page += 1
            if page >= 65:
                over = False








thread_pool()
