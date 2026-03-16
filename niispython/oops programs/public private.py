class Demo:
	def _show(self):#private
		print("hi")
	def disp(self):#public
	    self._show()
ob=Demo()
ob._show()	    
