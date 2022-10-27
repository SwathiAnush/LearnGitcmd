Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import unittrst
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import unittrst
ModuleNotFoundError: No module named 'unittrst'
>>> import unittest
>>> class Sample(unittest.Testcase):
	def mul_string(self):
		self.assertEqual('Anu'*2,'AnuAnuAnuAnu')
    if __name__=='__main__':
print("hello")	    
SyntaxError: unindent does not match any outer indentation level
>>> if __name__=='__main__':
	unittest.main().floor().help()


----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
>>> class Sample(unittest.Testcase):
	def mul_string(self):
		self.assertEqual('Anu'*2,'AnuAnu')
    if __name__=='__main__':
	    
SyntaxError: unindent does not match any outer indentation level
>>> if __name__=='__main__':
	unittest.main()
	


----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
>>> 
>>> 
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
i
SyntaxError: invalid syntax
>>> if __name=='__main__':
	unittest.main()

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    if __name=='__main__':
NameError: name '__name' is not defined
>>> if __name__=='__main__':
	unittest.main()
	
