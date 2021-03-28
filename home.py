#coding:utf-8
import requests,json

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self,):
		self.headers = {"Content-Type":"application/json","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
	def py_post(self,api,data):
		r = requests.post(api,data=json.dumps(data),headers=self.headers,verify=False)
		print(r.json())
		return r.json()

if __name__ == '__main__':
	ClassName().py_post('https://tpaprod.ikandy.cn/api/txtechnology/login',{"loginName":"yzc","password":"123456"})
