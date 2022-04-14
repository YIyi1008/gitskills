# test_register.py
import unittest
from register import register	#从register中导入register函数


class TestRegister(unittest.TestCase):
	"""注册接口测试用例，只有继承unittest里面的TestCase类之后我们才是真正的使用unittest框架去写测试用例"""
	def test_register_success(self):
		"""注册成功"""
		data = ("testuser1","test123456","test123456")	#测试成功的数据
		expected = {"code": 1,"msg" : "注册成功"}	 #预期结果
		result = register(*data)	#将data中的数据传入导入的register函数
		self.assertEqual(expected,result)	#断言，判断实际结果和预期结果是否一致

	def test_register_isnull(self):
		"""注册失败，用户名为空"""
		data = ("","test123456","test123456")	#测试用户名为空的数据
		expected = {"code": 0,"msg" : "所有参数不能为空"}	 #预期结果
		result = register(*data)	#将data中的数据传入导入的register函数
		self.assertEqual(expected,result)	#断言，判断实际结果和预期结果是否一致

	def test_register_isMAX(self):
		"""注册失败，用户名为空"""
		data = ("qwertyuiopasdfghjklzxcvbnm","test123456","test123456")	#测试用户名为 大于18位的数据
		expected = {"code": 0,"msg" : "用户名和密码必须在6-18位之间"}	 #预期结果
		result = register(*data)	#将data中的数据传入导入的register函数
		self.assertEqual(expected,result)	#断言，判断实际结果和预期结果是否一致

	def test_register_fpsd(self):
		"""注册失败，用户名为空"""
		data = ("testuser2","test123456","test888888")	#测试用户名为 大于18位的数据
		expected = {"code": 0,"msg" : "用户名和密码必须在6-18位之间"}	 #预期结果
		result = register(*data)	#将data中的数据传入导入的register函数
		self.assertEqual(expected,result)	#断言，判断实际结果和预期结果是否一致



# 如果直接运行这个文件，需要使用unitest中的main函数来执行测试用例
if __name__ == '_main_':
	unittest.main()
