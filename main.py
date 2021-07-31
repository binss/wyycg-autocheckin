import sys
import os
import requests
import json

sign_url = 'https://n.cg.163.com/api/v2/sign-today'
current = 'https://n.cg.163.com/api/v2/client-settings/@current'

cookies = os.environ["COOKIE"].split('#')
barkkey = os.environ["BARK_KEY"]
if barkkey.find('https') == -1 and barkkey.find('http') == -1:
    barkkey = f"https://api.day.app/{barkkey}"

def signin(url, cookie):
    header = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5',
        'Authorization': str(cookie),
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Host': 'n.cg.163.com',
        'Origin': 'https://cg.163.com',
        'Referer': 'https://cg.163.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'X-Platform': '0'
    }

    result = requests.post(url=url, headers=header)
    return result

def getme(url, cookie):
    header = {
        'Host': 'n.cg.163.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'X-Platform': '0',
        'Authorization': str(cookie),
        'Origin': 'https://cg.163.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://cg.163.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5'
    }
    result = requests.get(url=url, headers=header)
    return result

def report(method: str,
            url: str,
            max_retries: int = 2,
            params=None,
            data=None,
            json=None,
            headers=None,
            **kwargs):
    # The first HTTP(S) request is not a retry, so need to + 1
    total_requests = max_retries + 1
    for i in range(total_requests):
        try:
            response = requests.Session().request(
                method,
                url,
                params=params,
                data=data,
                json=json,
                headers=headers,
                timeout=21,
                **kwargs)
        except Exception as e:
            print('Request failed: {url}\n{e}').format(url=url, e=e)
            if i == max_retries:
                raise Exception(_('Request failed ({count}/{total_requests}):\n{e}').format(
                    count=(i + 1), total_requests=total_requests, e=e
                ))

            seconds = 5
            log.info(_('Trying to reconnect in {seconds} seconds ({count}/{max_retries})...').format(
                seconds=seconds, count=(i + 1), max_retries=max_retries,
            ))
            time.sleep(seconds)
        else:
            return response

class BaseNotifier(object):
    app = 'WYYCG'
    status = ': Test'
    desp = 'wyycg-autocheckin'

    def __init__(self):
        self.name = None
        self.token = None
        self.retcode_key = None
        self.retcode_value = None

    def send(self):
        ...

    def push(self,
             method,
             url,
             params=None,
             data=None,
             json=None,
             headers=None):
        if not self.token:
            return
        try:
            response = report(method, url, 2, params, data, json, headers).json()
        except Exception as e:
            raise Exception(f'{self.name} failure\n{e}')
        else:
            retcode = response.get('data', {}).get(
                self.retcode_key,
                -1) if self.name == 'Server Chan Turbo' else response.get(
                self.retcode_key, -1)
            if retcode == self.retcode_value:
                print(f'{self.name} success')

class BarkNotifier(BaseNotifier):
    def __init__(self):
        self.name = 'Bark App'
        self.token = barkkey
        self.retcode_key = 'code'
        self.retcode_value = 200

    def send(self, text=BaseNotifier.app, status=BaseNotifier.status, desp=BaseNotifier.desp):
        url = barkkey
        data = {
            'title': f'{text} {status}',
            'body': desp,
            'sound': "healthnotification"
        }
        return self.push('post', url, data=data)


if __name__ == "__main__":
    print('检测到{}个账号，即将开始签到！'.format(len(cookies)))
    success = []
    failure = []
    msg = []
    for i in cookies:
        cookie = i
        autherror = False
        signerror = False
        sign_return = None
        me = None
        try:
            me = getme(current, cookie)
        except:
            message = '第{}个账号验证失败！请检查Cookie是否过期！'.format(
                cookies.index(i) + 1)
            failure.append(cookie)
            msg.append(message)
            autherror = True
        if me.status_code != 200 and not autherror:
            message = '第{}个账号验证失败！请检查Cookie是否过期！'.format(
                cookies.index(i) + 1)
            failure.append(cookie)
            msg.append(message)
        elif me.status_code == 200:
            try:
                sign_return = signin(sign_url, cookie)
            except:
                message = '第{}个账号签到失败，回显状态码为{}，具体错误信息如下：{}'.format(cookies.index(i) + 1, sign_return.status_code, sign_return.text)
                failure.append(cookie)
                msg.append(message)
                signerror = True

            if sign_return.status_code == 200:
                message = '第{}个账号签到成功！'.format(cookies.index(i) + 1)
                success.append(cookie)
                msg.append(message)
            elif not signerror:
                message = '第{}个账号签到失败，回显状态码为{}，具体错误信息如下：{}'.format(cookies.index(i) + 1, sign_return.status_code, sign_return.text)
                failure.append(cookie)
                msg.append(message)
    outputmsg = str(msg).replace("[", '').replace(']', '').replace(',', '<br>').replace('\'', '')
    push_message = '''
    今日网易云游戏签到结果如下：
    成功数量：{0}/{2}
    失败数量：{1}/{2}
    具体情况如下：
    {3}
    '''.format(len(success), len(failure), len(cookies), outputmsg)
    print(push_message)
    notifier = BarkNotifier()
    notifier.send("网易云游戏签到", "OK", push_message)
