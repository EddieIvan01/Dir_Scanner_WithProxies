# Dir Scan With Proxies


**用途**

扫描后台时能挂着代理，避免频繁404被服务器ban掉

原来在i春秋看到的别人写的后台扫描脚本，python2.7

脚本逻辑真的很烂，多线程扫描时：判断队列不为空，接着判断当前active线程 <= MAXTHREAD，接着启动线程。

这样写扫描多少URL就创建多少线程...很多资源都用在了线程创建销毁开销，而且既然每个线程处理一个URL那就完全没必要创建任务队列，直接遍历一遍任务启动函数就可以了。
有queue明明可以创建线程池或者创建单个任务线程死循环中当队列不为空就get，为空则return

但我不想改，看别人的代码改写真的很痛苦（╯－＿－）╯╧╧ 

***

**Scan With Proxies**

为了在扫描时走代理避免被封IP，我写了个装饰器函数，在原脚本中加两句

```python
#导入包
from proxy import get_proxy as gp
.
.
.
#装饰请求函数
@gp.RequestWithProxy
def scan_target_url_exists(target_url, proxy):
```

***

/dictionary目录下是原来在github上找的字典，但我忘记地址了，不能在这儿贴出来，抱歉
