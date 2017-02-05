from fbx import *
import FbxCommon
import sys
print("hello fbx   FbxCommon.py")

import DebugLogger00100

class FbxCommon00100:
	#SingleTon==========================START
	__instance = None;#SingleTon==========================START
	__instanceSingleName = "FbxCommon00100py_IamSingleTon_instanceSingleName"
	FbxManager = None;
	FbxInOutSettings = None;
	FbxScene = None;
	#FbxManager = None;
	def __new__(self):
		print(" FbxCommon00100.py >> MySingleton class  -------__new__ ------ ")
		if self.__instance is None:
			self.__instance = object.__new__(self);
		return self.__instance;
	def getInstance(self):
		print("FbxCommon00100.py >> MySingleton class  -------getInstance ------ ")
		if self.__instance is None:
			self.__instance = object.__new__(self);
			print("FbxCommon00100.py  >>  MySingleton class  ------- getInstance()   self.__instance="+self.__instanceSingleName)
		else :
			print("FbxCommon00100.py  >>   MySingleton class  ------- getInstance()   if  self.__instance is  Have="+str(self.__instance))
		return self.__instance;
	def __init__(self):
		print("FbxCommon00100.py  MySingleton.py    MySingleton class  -------__init__ ------ "+ str(self.getInstance))
		#return self.getInstance;
	def getName(self):
		return self.__instanceSingleName
		#SingleTon==========================END

	def Samething(self):
		print("014 FbxCommon00100 Samething()")
	def GetFbxManager(self):
		print("FbxCommon00100.py method GetFbxManager()")
		lSdkManager = FbxManager.Create()
		print("FbxCommon00100.py method GetFbxManager()   lSdkManager= "+str(lSdkManager))
		#self.__instance.FbxManager=lSdkManager
		self.FbxManager=lSdkManager
		print("FbxCommon00100.py method GetFbxManager()  self.FbxManager= "+str(self.FbxManager))
		#print("FbxCommon00100.py method GetFbxManager()  self.__instance.FbxManager= "+str(self.__instance.FbxManager))
		return lSdkManager;
	def GetFbxInOutSettings(self):
		print("FbxCommon00100.py method self.FbxInOutSettings()")
		myFbxInOutSettings = FbxIOSettings.Create(self.FbxManager, IOSROOT)
		
		print("FbxCommon00100.py method self.FbxInOutSettings()   myFbxInOutSettings= "+str(myFbxInOutSettings))
		self.FbxInOutSettings=myFbxInOutSettings
		print("FbxCommon00100.py method self.FbxInOutSettings()   self.FbxInOutSettings= "+str(self.FbxInOutSettings))
		#self.FbxManager=lSdkManager
		return myFbxInOutSettings;

	def GetFbxScene(self):
		print("FbxCommon00100.py method self.GetFbxScene()")
		#myScene = FbxScene.Create(lSdkManager, "")
		myScene = FbxScene.Create(self.FbxManager, "")
		print("FbxCommon00100.py method self.GetFbxScene()   myScene= "+str(myScene))
		self.FbxScene=myScene
		print("FbxCommon00100.py method self.GetFbxScene()   self.FbxScene= "+str(self.FbxScene))
		#self.FbxManager=lSdkManager
		return myScene;

	def InitializeSdkObjects(self):
		print("FbxCommon00100.py method InitializeSdkObjects()")
		lSdkManager = FbxManager.Create()
		print("FbxCommon00100.py method InitializeSdkObjects()   lSdkManager= "+str(lSdkManager))
		#//////////////////////////////////////////////////////////////////////////////////////////////////
		#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
		#//////////////////////////////////////////////////////////////////////////////////////////////////		
	def getClassName(self):
		print( u"className= " + self.__class__.__name__)
		return self.__class__.__name__

#=============================Code Start===============================================
print(" Code Start="+__name__)
#FbxCommon00100_Instance = FbxCommon00100.FbxCommon00100()
FbxCommon00100_Instance = FbxCommon00100()
Debug_Instance=DebugLogger00100.DebugLogger00100()
def DebugLogStart():
	#print("DebugStr = "+ DebugStr)
	Debug_Instance.DebugLogStart()
	
def DebugLog(DebugStr):
	print("DebugStr = "+ DebugStr)
	Debug_Instance.DebugLog(" 88 Logger >>>>>>>>"+DebugStr);
	

#FBX_trans_z_Instance = FbxImport_WriteReadTrans_Z_00610()  # Class  export  instance.


#GetKeyCurve_Instance = GetKeyCurve00110.GetKeyCurve00110()  # Class  export  instance.

#print(" FbxImport_WriteReadTrans_Z_00610 Class  __name__="+__name__)
#WriteReadTrans_ZInstance=WriteReadTrans_Z_00310.WriteReadTrans_Z_00310()
#WriteReadTrans_ZInstance.fileDataZeroReset()
def StartMainLine(Debug_Instance,FbxCommon00100_Instance):
	print(">>>>>>>>>>>>>>StratMainLine>>>>>>>>>>>>>>>>>>>")
	FbxCommon00100_Instance.Samething()
	FbxCommon00100_Instance.InitializeSdkObjects()
	FbxCommon00100_Instance.GetFbxManager()
	FbxCommon00100_Instance.GetFbxInOutSettings()
	FbxCommon00100_Instance.GetFbxScene()
	
#//////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////	
if(__name__ == FbxCommon00100_Instance.getClassName()):
	print (u"============= 01 Simple Single Class Unit Test Start==== Instance.getClassName() =  "+FbxCommon00100_Instance.getClassName()+" =====")
	#StartMainLine(Debug_Instance,WriteReadTrans_ZInstance,FBX_trans_z_Instance)
elif(__name__ == "FbxCommon00100"):
	print (u"============= 02 Simple Single Class Unit Test Start===== StartMainLine =====")
	#StartMainLine(Debug_Instance,WriteReadTrans_ZInstance,FBX_trans_z_Instance)	
	#Instance.loadFile(FBX_FILE_PATH_AND_NAME_AND_EXT)
elif(__name__ == "__main__"):
	print (u"============= 03 Simple Single Class Unit Test Start===== __main__ =====")
	StartMainLine(Debug_Instance,FbxCommon00100_Instance)
else:
	print (u"==============04    __name__!=self.__class__.__name__  Othor File Import")
	