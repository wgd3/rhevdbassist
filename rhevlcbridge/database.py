'''
Created on Dec 27, 2013

@author: wallace
'''
import tarfile, os

class database():
	'''
	This class should be created by passing the sos_pgdump.tar file to it
	
	It will serve the purpose of pulling information from the tar file without the need to upload to a dbviewer
	'''

	''' Start declaring variables for the class'''
	dbDir = ""
	tarFile = ""
	dat_files = [] # this is a list for all the wanted dat files

	def __init__(self, dbFile):
		'''
		Constructor
		'''
		dbDir = os.path.dirname(dbFile)+"/"
		tarFile = tarfile.open(dbFile)
		self.unpack(tarFile, dbDir)
		
	def unpack(self, tarFile, dbDir):
		# Start with extraction
		tarFile.extractall(dbDir)
		
		# then set most of the needed variables for future functions
		dat_files = ["data_center_dat",
					 "storage_domain_dat",
					 "host_dat"]
		
		dat_files[0] = dat_files[0] +","+ self.findDat(" storage_pool ", dbDir+"restore.sql")
		dat_files[1] = dat_files[1] +","+ self.findDat(" storage_domain_static ", dbDir+"restore.sql")
		dat_files[2] = dat_files[2] +","+ self.findDat(" vds_static ", dbDir+"restore.sql")	
		
		
	def findDat(self,table,restFile):
		'''
		Subroutine to find the dat file name in restore.sql
		''' 
		openFile = open(restFile, "r")
		lines = openFile.readlines()
	
		# print "Looking for " + table
	
		for n in lines:
			if n.find(table) != -1:
				if n.find("dat") != -1:
					datInd = n.find("PATH")
					datFileName =  n[datInd+7:datInd+15]
					if datFileName.endswith("dat"):
						#print "Found dat line for " + table
						#logging.warning('Return dat file: ' +datFileName)
						return datFileName
	
	return -1

	def getDataCenters(self):
		'''
		This method returns a list of comma-separated details of the Data Center
		'''
		dc_list = []
		dat_file = dbDir+dat_files[0].split(",")[1]
		openDat = open(dat_file,"r")
		
		lines = openDat.readlines()
		
		for l in lines:
			dc_list.append(l.split("\t"))
			
		openDat.close()
		return dc_list
	