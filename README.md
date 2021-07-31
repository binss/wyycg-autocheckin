# 网易云游戏自动签到

请注意：关于LICENSE，在Apache-2.0的基础上增加一条：**禁止上传到CSDN等网站盈利，禁止放在某宝某鱼等平台贩卖**，否则官方找上门就**删库跑路**！

本脚本通过使用Github Action来进行[网易云游戏](https://cloudgame.webapp.163.com/newer.html?invite_code=2ZLPWY)签到操作，让你能够天天白嫖网易云游戏时长和云电脑！

喜欢就给我点个STAR吧！

签到时间是早上10点，如果有需要就自己修改.github/workflows/AutoSignin.yml中第12行的时间，时间遵循UTC时间，+8才是我们的时间

**请不要使用非master分支脚本，他们通常正在开发新功能，会有BUG出现**

关于签到失败返回的结果（[这里有实例](https://github.com/GamerNoTitle/wyycg-autocheckin/discussions/6)），如果你有解码的经验，可以前往[这里](https://github.com/GamerNoTitle/wyycg-autocheckin/discussions/6)提供帮助，Thanks♪(･ω･)ﾉ

## 赞助
点击下面的Badge其中一个就可以跳转到相应页面，感谢老板的支持！

<a href="https://afdian.net/@GamerNoTitle"><img src="https://img.shields.io/badge/%E7%88%B1%E5%8F%91%E7%94%B5-GamerNoTitle-%238e8cd8?style=for-the-badge" alt="前往爱发电赞助" width=auto height=auto border="0" /></a> <a href="https://cdn.jsdelivr.net/gh/GamerNoTitle/Picture-repo@master/img/Donate/WeChatPay.png"><img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1%E6%94%AF%E4%BB%98-GamerNoTitle-%2304BE02?style=for-the-badge" alt="使用微信赞助" width=auto height=auto border="0" /></a> <a href="https://cdn.jsdelivr.net/gh/GamerNoTitle/Picture-repo@master/img/Donate/AliPay.jpg"><img src="https://img.shields.io/badge/%E6%94%AF%E4%BB%98%E5%AE%9D%E6%94%AF%E4%BB%98-GamerNoTitle-%231678FF?style=for-the-badge" alt="使用支付宝赞助" width=auto height=auto border="0" /></a>

## 目录

- [使用方法](#使用方法)
- [保活策略](#保活策略)
- [变量获取](#变量内容获取)
- [脚本更新](#脚本更新)
- [Q&A](#qa)

## 使用方法

### 变量添加

1、Fork本仓库，按右上角的分支按钮（如图）

![](https://upimage.alexhchu.com/2020/11/22/e9b4bcf8e6a1d.png)

2、进入设置，设置变量`cookie`和`teleid` `teletoken` `SCKEY` `QQKEY` `PPKEY`（这五个可选，但是`teleid`和`teletoken`要用的话就得两个都要配置！）

**请注意：你无需在仓库的secrets内设置名为`GITHUB_TOKEN`的变量，该名称本身就是指定为自己账户下名为`GITHUB_TOKEN`的密钥，如果你在仓库的secrets内设置将会被Github提示无效**

**如果使用多用户，多个cookie请使用`#`分隔**

[如何获取变量内容？请点这里](#变量内容获取)

![](https://upimage.alexhchu.com/2020/11/22/988724b77ca62.png)

![](https://upimage.alexhchu.com/2020/11/22/a7958e9f5582f.png)

![](https://upimage.alexhchu.com/2020/11/22/7213627d41fc1.png)

### 测试脚本

**请在当天没有签到的情况下测试！！！**

我们先进入Action界面，启用Action

![](https://upimage.alexhchu.com/2020/11/22/70dd262ae54f0.png)

然后我们进入对应的脚本，启用脚本，并进行测试

![](https://upimage.alexhchu.com/2020/11/22/457403bb7d3bb.png)

除了点STAR进行启动以外，你也可以点击右边那个白白的按钮来启动

![](https://upimage.alexhchu.com/2021/01/09/49ef24f93434e.png)

**只要测试通过就是没问题，如果你配置了TELEGRAM还会收到你的BOT给你发送的消息**

测试通过后，你还需要创建保活需要用到的Github Token，详情可以看[保活策略](#保活策略)这一节（其实就在下面撒）

## 保活策略

因为Github Action在仓库60天内没有任何Push的时候会禁用你的Action，这时候我们就要进行保活

保活Action已经写好了，但是这里有一些步骤是需要你进行的，请看下面的图片生成GITHUB_TOKEN以便让脚本造成的更改能够正常推送入你的仓库

![](https://upimage.alexhchu.com/2020/12/27/dce7070ae625c.png)

![](https://upimage.alexhchu.com/2020/12/27/f82f6505503ed.png)

![](https://upimage.alexhchu.com/2020/12/27/9cff0436399b7.png)

到这里勾选完以后点绿绿的Generate token就可以了

**请注意：你无需在仓库的secrets内设置名为`GITHUB_TOKEN`的变量，该名称本身就是指定为自己账户下名为`GITHUB_TOKEN`的密钥，如果你在仓库的secrets内设置将会被Github提示无效**

## 变量内容获取

### cookie获取

首先我们进入[官网](https://cg.163.com)，进行登录，然后用<kbd>F12</kbd>打开开发者工具后使用<kbd>Ctrl</kbd>+<kbd>F5</kbd>进行刷新，会刷出很多结果

我们在里面找到`@me`这一项，然后在右边找到`Authorization`将冒号后面的内容复制下来就是我们所需要的Cookie

**如果使用多用户，多个cookie请使用`#`分隔**

![](https://upimage.alexhchu.com/2020/11/22/bfb0e2dbd347a.png)

### teleid获取

用你的Telegram找到@userinfobot，点个Start，会直接给你回复你的ID，复制下id后面的数字就是teleid了

![](https://upimage.alexhchu.com/2020/11/22/e4c50250626a6.png)

### teletoken获取

找@BotFather进行机器人的创建，按照提示创建即可，会给你一个API TOKEN，如果一不小心点过去了可以用命令`/mybots`管理自己的bot，找到自己想要使用的bot并获取API就可以了

![](https://upimage.alexhchu.com/2020/11/22/0428751a3925e.png)

### SCKEY获取

访问[ServerChanTurbo官网](https://sct.ftqq.com/)，并用你的微信扫码登陆，获取推送用的KEY即可（因为我没有使用这个推送方法所以没有图）

**请各位使用了SC推送服务的小伙伴尽快迁移到SCT，原服务将会在四月底下线**

### QQKEY获取

**不推荐使用此推送方式，因为其极不稳定！使用该推送方式无法收到QQ提醒的请不要开issue说这个问题，因为这是该服务的问题不是脚本问题**

访问[CoolPush官网](https://cp.xuthus.cc/)，使用任一方式登录，在`调用代码Skey`可以看到你的KEY

![](https://upimage.alexhchu.com/2021/01/25/dbfcd0cee03be.png)

### PPKEY获取

**此平台是ServerChan的替代平台，因为ServerChan发了个[通知](https://mp.weixin.qq.com/s/L4rONhZN2OCQ80cHxPAY0Q)，所以我就先把这个给更了

访问[PushPlus官网](http://pushplus.hxtrip.com/)，使用微信登录，直接在[一对一推送](http://pushplus.hxtrip.com/message)复制自己的Token填入变量即可！

![](https://upimage.alexhchu.com/2021/02/08/c8d1898ca8de5.png)

## 脚本更新

### 自动更新

[点击这里](https://github.com/apps/pull)安装插件，可以选择所有仓库，也可以指选择你Fork的仓库（当然至少要选择fork的仓库对吧，要不然怎么更新），然后不管它就好了

详细步骤可以看下面的图片

![](https://upimage.alexhchu.com/2020/12/26/4c0d02795a38c.png)

![](https://upimage.alexhchu.com/2020/12/26/1800e5609a365.png)

![](https://upimage.alexhchu.com/2020/12/26/29ffcfd4fd8b0.png)

如果你完成了上面的步骤，就可以不管它了，自动更新会自己进行（除非有`Merge Conflict`）

### 手动更新

在自己的仓库中，创建一个pull requests，上游（右边的选择本仓库（GamerNoTitle/wyycg-autocheckin）的master分支，左边选择自己的仓库，然后创建PR并Merge即可！

具体可以看下面的图片

![](https://upimage.alexhchu.com/2020/12/26/660bffa186f57.png)

![](https://upimage.alexhchu.com/2020/12/26/b90770108e301.png)

![](https://upimage.alexhchu.com/2020/12/26/da988092d8556.png)

![](https://upimage.alexhchu.com/2020/12/26/444ca5bc88093.png)

![](https://upimage.alexhchu.com/2020/12/26/db022886a1c5f.png)

## Q&A

## 返回值400并附带一串不知道什么鬼的字符串

例子：
```
    感谢使用来自GamerNoTitle的网易云游戏自动签到脚本！
    今日签到结果如下：
    成功数量：0/1
    失败数量：1/1
    具体情况如下：
    第1个账号签到失败，回显状态码为400，具体错误信息如下：GL8B/hH+v9cYGsm/Ag8PAAwBAr/XztPNzsm/Ag8PChAEv9e/EhACD70QBgQLvREMAf4Wv8m/Ag8PChAEAAu/17/5EtID0tD5EtLWz9b5EtIBA8/5EtT/1AL5EtLP0M2/Gqc=
    GamerNoTitle: https://bili33.top
    网易云游戏自动签到脚本: https://github.com/GamerNoTitle/wyycg-autocheckin
```

首先你需要确认你当天是否已经签到过了才运行的脚本，如果确实先签了到再运行脚本，网易确实会返回400

目前也只发现这种情况会返回400，如果有其他情况你可以在issue跟我提出

## 错误代码

### telepot.exception.TelegramError

#### Chat not found

请先用你要接受信息的账户发个`/start`给你的bot，或者检查用户ID是否正确！

#### Not found

请检查自己的Telebot Token是否正确！

### telepot.exception.UnauthorizedError

该错误显示如下：

```
Traceback (most recent call last):
File "main.py", line 185, in
send(teleid, teleinfomsg)
File "main.py", line 82, in send
bot.sendMessage(id, message, parse_mode=None, disable_web_page_preview=None, disable_notification=None,
File "/opt/hostedtoolcache/Python/3.8.9/x64/lib/python3.8/site-packages/telepot/init.py", line 513, in sendMessage
return self._api_request('sendMessage', _rectify(p))
File "/opt/hostedtoolcache/Python/3.8.9/x64/lib/python3.8/site-packages/telepot/init.py", line 491, in _api_request
return api.request((self._token, method, params, files), **kwargs)
File "/opt/hostedtoolcache/Python/3.8.9/x64/lib/python3.8/site-packages/telepot/api.py", line 155, in request
return _parse(r)
File "/opt/hostedtoolcache/Python/3.8.9/x64/lib/python3.8/site-packages/telepot/api.py", line 147, in _parse
raise e(description, error_code, data)
telepot.exception.UnauthorizedError: ('Unauthorized', 401, {'ok': False, 'error_code': 401, 'description': 'Unauthorized'})
```

解决方法：检查自己的Bot的Token是不是正确的！

### urllib3.exceptions

#### MaxRetryError

`HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /botxxxx/sendMessage`

出现这个错误，那就是Telegram的问题，Github连接不上Telegram服务器（大半是TG服务器炸了）

#### ReadTimeoutError

`HTTPSConnectionPool(host='api.telegram.org', port=443): Read timed out. (read timeout=30)`

出现这个错误，那就是Telegram的问题，Github连接不上Telegram服务器（大半是TG服务器炸了）~~（复制粘贴大法）~~

---

## 历史STAR

![](https://starchart.cc/GamerNoTitle/wyycg-autocheckin.svg)

## 免责声明

使用本脚本造成的封号或任何违反相关法律法规造成的任何责任，由使用者自行承担，开发者不担负任何责任！
