#-*- coding: gbk -*-
import requests
from threading import Thread, activeCount
import Queue
from proxy import get_proxy as gp

queue = Queue.Queue()
dir_file=raw_input("dictionary:")

@gp.RequestWithProxy
def scan_target_url_exists(target_url, proxy):
	headers={
	        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
	        'Accept-Encoding': 'gzip, deflate',
	        'Referer': 'http://www.google.com'
	}
	status_codes = [200]
	try:
		req=requests.head(target_url.strip(),timeout=8,headers=headers, proxies = proxy)
		if req.status_code in status_codes:
			print 'CODE:%s,URL:%s'%(str(req.status_code),target_url.strip('\n').strip('\r'))
			open('exist_target.txt','a').write(target_url)
	except:
		pass
def open_pathfile(file):
	all_lines=open(file,'r').readlines()
	for line in all_lines:
		if target_url.endswith('/'):
			if line.startswith('/'):
				queue.put(target_url+line[1:])
			else:
				queue.put(target_url + line)
		else:
			if line.startswith('/'):
				queue.put(target_url + line)
			else:
				queue.put(target_url + '/' + line)

if __name__ == '__main__':
	print '''
 ____  _      ____                  
|  _ \(_)_ __/ ___|  ___ __ _ _ __  
| | | | | '__\___ \ / __/ _` | '_ \ 
| |_| | | |   ___) | (_| (_| | | | |
|____/|_|_|  |____/ \___\__,_|_| |_|
 
    '''
	target_url=raw_input('Please input your target:')
	threadnum = raw_input('Please input your threadnum:')
	if target_url.startswith('http://') or target_url.startswith('https://'):
		pass
	else:
		target_url = 'http://' + target_url
		print 'The number of threads is %s' % threadnum
		print 'Matching.......'
	open_pathfile(dir_file)
	while queue.qsize() > 0:
		if activeCount() <= int(threadnum):
			Thread(target=scan_target_url_exists,args=(queue.get(),)).start()