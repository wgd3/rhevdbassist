'''
Created on Dec 27, 2013

@author: wallace
'''

class Host():
	'''
	This class will represent hosts in an environment
	'''
	
	uuid = ""
	name = ""
	host_dc_uuid = ""
	ip_addr = ""
	host_name = ""
	
	def __init__(self, csvList):
		'''
		This constructor assumes it is being passed a comma separated list consisting of all elements in a line from the dat file
		'''
		details = []
		
		for d in csvList:
			details.append(d)
		
		self.uuid = details[0]
		self.name = details[1]
		self.host_dc_uuid = details[6]
		self.ip_addr = details[2]
		self.host_name = details[4]

	def get_uuid(self):
		return self.__uuid


	def get_name(self):
		return self.__name


	def get_host_dc_uuid(self):
		return self.__host_dc_uuid


	def get_ip_addr(self):
		return self.__ip_addr


	def get_host_name(self):
		return self.__host_name


	def set_uuid(self, value):
		self.__uuid = value


	def set_name(self, value):
		self.__name = value


	def set_host_dc_uuid(self, value):
		self.__host_dc_uuid = value


	def set_ip_addr(self, value):
		self.__ip_addr = value


	def set_host_name(self, value):
		self.__host_name = value


	def del_uuid(self):
		del self.__uuid


	def del_name(self):
		del self.__name


	def del_host_dc_uuid(self):
		del self.__host_dc_uuid


	def del_ip_addr(self):
		del self.__ip_addr


	def del_host_name(self):
		del self.__host_name

	uuid = property(get_uuid, set_uuid, del_uuid, "uuid's docstring")
	name = property(get_name, set_name, del_name, "name's docstring")
	host_dc_uuid = property(get_host_dc_uuid, set_host_dc_uuid, del_host_dc_uuid, "host_dc_uuid's docstring")
	ip_addr = property(get_ip_addr, set_ip_addr, del_ip_addr, "ip_addr's docstring")
	host_name = property(get_host_name, set_host_name, del_host_name, "host_name's docstring")
		
	
		