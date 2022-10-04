Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import unittest
>>> class Pain(unittest.Testcase):
	def test_check(self):
		self.assertTrue('a12A'.isalnum())
		self.assertTrue('123'.isalpha())
	def test_spit(self):
		s='Anushuya Devi'
		self.assertEqual(s.split(),['Anushuya','Devi'])
		with self.assertRaises(TypeError):
			s.split(3)
			
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> import unittest
>>> class Pain(unittest.Testcase):
	def test_check(self):
		self.assertTrue('a12A'.isalnum())
		self.assertTrue('123'.isalpha())
	def test_spit(self):
		s='Anushuya Devi'
		self.assertEqual(s.split(),['Anushuya','Devi'])
		with self.assertRaises(TypeError):
			s.split(3)
#this is second branch change
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    class Pain(unittest.Testcase):
AttributeError: module 'unittest' has no attribute 'Testcase'
>>> if __name__=='__main__':
	unittest.main()
