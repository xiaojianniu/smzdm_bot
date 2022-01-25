"""
什么值得买自动签到脚本
使用github actions 定时执行
@author : stark
"""
import requests,os
from sys import argv

import config
from utils.serverchan_push import push_to_wechat

class SMZDM_Bot(object):
    def __init__(self):
        self.session = requests.Session()
        # 添加 headers
        self.session.headers = config.DEFAULT_HEADERS

    def __json_check(self, msg):
        """
        对请求 盖乐世社区 返回的数据进行进行检查
        1.判断是否 json 形式
        """
        try:
            result = msg.json()
            print(result)
            return True
        except Exception as e:
            print(f'Error : {e}')            
            return False

    def load_cookie_str(self, cookies):
        """
        起一个什么值得买的，带cookie的session
        cookie 为浏览器复制来的字符串
        :param cookie: 登录过的社区网站 cookie
        """
        self.session.headers['Cookie'] = cookies    

    def checkin(self):
        """
        签到函数
        """
        url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
        msg = self.session.get(url)
        if self.__json_check(msg):
            return msg.json()
        return msg.content




if __name__ == '__main__':
    sb = SMZDM_Bot()
    # sb.load_cookie_str(config.TEST_COOKIE)
    cookies = os.environ["__ckguid=lnIrOb1hJTLx5hQXxqIWu2; device_id=21307064331643114436904534bb6e72a61c33ba95c5a36218c6877456; homepage_sug=a; r_sort_type=score; __jsluid_s=e04c91546bd679987d94f3c85b07c73c; _zdmA.vid=*; sajssdk_2015_cross_new_user=1; footer_floating_layer=0; ad_date=25; ad_json_feed=%7B%7D; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1643114441; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217e91409e681e9-05ee6474236978-f791539-2073600-17e91409e6a749%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217e91409e681e9-05ee6474236978-f791539-2073600-17e91409e6a749%22%7D; sess=AT-zv1kzQYvLsvuqr1SiipQ64%2BVQKf6HivNB8OM9aX361fS7Euj90ysjxut6wQCJSgUXNhtgnK7Kz1cd32P87gognOMETByGR9AN%2FZeaes9wcwqvmLPyT2mWOiP; user=user%3A1048617333%7C1048617333; smzdm_id=1048617333; _zdmA.time=1643115316420.40318.https%3A%2F%2Fwww.smzdm.com%2F; _zdmA.uid=ZDMA.lItVm3FQi.1643115317.2419200; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1643115317; bannerCounter=%5B%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; amvid=69b4103f65dd72928f2ed74436d0dca1"]
    sb.load_cookie_str(cookies)
    res = sb.checkin()
    print(res)
    SERVERCHAN_SECRETKEY = os.environ["SCT110071T46qpZ1CAVfK0E5fHCguLcOjT"]
    print('sc_key: ', SERVERCHAN_SECRETKEY)
    if isinstance(SERVERCHAN_SECRETKEY,str) and len(SERVERCHAN_SECRETKEY)>0:
        print('检测到 SCKEY， 准备推送')
        push_to_wechat(text = '什么值得买每日签到',
                        desp = str(res),
                        secretKey = SERVERCHAN_SECRETKEY)
    print('代码完毕')
