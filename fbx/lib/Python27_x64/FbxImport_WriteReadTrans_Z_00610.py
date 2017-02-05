# -*- coding: utf-8 -*-
#from fbx import *
import DebugLogger00100
import WriteReadTrans_Z_00310
import GetKeyCurve00110
#===================class Node=========================
import FbxCommon
#===================class Node=========================
class Node() :
	def __init__(self, name, parent) :
		self.name = name
		self.parent = parent
		self.children = None
		self.type = None
	def addChild(self, child) :
		if not self.children : self.children = list()
		self.children.append(child)

def getTypeName(fbxNode) :
	DebugLog("190      getTypeName(fbxNode= "+str(fbxNode)  )
	nodeAttr = fbxNode.GetNodeAttribute()
	e = nodeAttr.GetAttributeType()
	sType = "Unknown"
	if FbxNodeAttribute.eNull == e : sType = "Null"
	elif FbxNodeAttribute.eMarker == e : sType = "Marker"
	elif FbxNodeAttribute.eSkeleton == e : sType = "Skeleton"
	elif FbxNodeAttribute.eMesh == e : sType = "Mesh"
	elif FbxNodeAttribute.eNurbs == e : sType = "Nurbs"
	elif FbxNodeAttribute.ePatch == e : sType = "Patch"
	elif FbxNodeAttribute.eCamera == e : sType = "Camera"
	elif FbxNodeAttribute.eLight == e : sType = "Light"
	return sType

def getHierarchy(fbxNode, node) :
	num = fbxNode.GetChildCount()
	DebugLog("205   getHierarchy(fbxNode= "+str(fbxNode)+", node.name= "+str(node.name)+")")
	if 0 == num : return
	for i in range(num) :
		fbxChild = fbxNode.GetChild(i)
		nodeChild = Node(fbxChild.GetName(), node)
		nodeChild.type = getTypeName(fbxChild)
		node.addChild(nodeChild)
		getHierarchy(fbxChild, nodeChild)

import FbxCommon
import FbxCommon00100
class FbxImport_WriteReadTrans_Z_00610() :
	Yen="\\"
	FileName= "FbxImport_WriteReadTrans_Z_00610__Log.csv"
	#print("HD FULL PATH =")
	#HD_FULL_PATH=os.path.abspath(__file__)
	#print("os.path.abspath(__file__)    =     " + HD_FULL_PATH)
	FullPass_DustDataTextFile_TXT= "D:"+Yen+"vs"+Yen+"py"+Yen+FileName
	Yen="\\"
	FullPass_DustDataTextFile_TXT= "C:"+Yen+"vs"+Yen+"py"+Yen+FileName
	Yen="\\"

	#IMPORT_FBX_FileName="Solder_Model_ASCII_2016_2017_motion00200.fbx"
	IMPORT_FBX_FileName="walkTest_00200_Only_Root_And_C_Pelvis_ASCII.fbx"
	FBX_FILE_PATH_AND_NAME_AND_EXT= "D:"+Yen+"vs"+Yen+"py"+Yen+IMPORT_FBX_FileName
	FBX_FILE_PATH_AND_NAME_AND_EXT= "C:"+Yen+"vs"+Yen+"py"+Yen+IMPORT_FBX_FileName


	EXPORT_FBX_FILENAME="walkTest_00200_Only_Root_And_C_Pelvis_ASCII_Fbx_Trans_Z_00510_.fbx"
	FullPass_EXPORT_FBX_FILENAME=  "D:"+Yen+"vs"+Yen+"py"+Yen+EXPORT_FBX_FILENAME
	FullPass_EXPORT_FBX_FILENAME=  "C:"+Yen+"vs"+Yen+"py"+Yen+EXPORT_FBX_FILENAME


	#TransZwriteReader
	# Propaty End========================================

	# Method Start========================================
		
	def FbxImport_WriteReadTrans_Z_00610(self):
		print ("==========================FbxImport_WriteReadTrans_Z_00610()=========================================")
		#DebugLog_init(FullPass_DustDataTextFile_TXT,"--------none--------"):
		#DebugLog_init()
	def loadFile(self, filename,TransZwriteReader,GetKeyCurve_Instance,FbxCommon00100_Instance) :
		self.ref_TransZwriteReader_instance=TransZwriteReader
		#self.ref_TransZwriteReader_instance.ExportWrite( floatNumstr );
		#self.ref_TransZwriteReader_instance.ExportWrite( 0.123456789 );
		self.filename = filename
		self.root = None
		self.load()
	def load(self) :
		print ("loading ... self.filename= "+self.filename)
		#print "loading : %s"%self.filename
		#manager = FbxManager.Create()
		manager=FbxCommon00100_Instance.GetFbxManager()
		#ios = FbxIOSettings.Create(manager, IOSROOT)
		inOutSetting=FbxCommon00100_Instance.GetFbxInOutSettings()
		#manager.SetIOSettings(ios)
		importer = FbxImporter.Create(manager, "")
		fbxImportSuccesBool=importer.Initialize(self.filename, -1, manager.GetIOSettings()) 
		DebugLog("fbxImportSuccesBool="+str(fbxImportSuccesBool))
		if not fbxImportSuccesBool:
			print ("==============Failed to load file.=============="+self.filename)
			return
		scene = FbxScene.Create(manager, "MyScene")
		importer.Import(scene)
		#importer.Initialize()
		
		fbxRoot = scene.GetRootNode()
		self.root = Node(fbxRoot.GetName(), None)
		
		getHierarchy(fbxRoot, self.root)
			
		######GetMesh(self.root)
		
		#GetKeyCurve(importer,scene)#198  200 Line
		GetKeyCurve_Instance.GetKeyCurve(importer,scene)#198  200 Line
		
		print ("==============Succeeded to load file.========="+self.filename)
		DebugLog ("104 FbxImport_WriteReadTrans_Z_00610 def load() ==============Succeeded to load file.=========")
		DebugLog ("104 FbxImport_WriteReadTrans_Z_00610 def load() ==============Succeeded to load file.=========")
		DebugLog ("104 FbxImport_WriteReadTrans_Z_00610 def load() ==============Succeeded to load file.=========")
		DebugLog ("104 FbxImport_WriteReadTrans_Z_00610 def load() ==============Succeeded to load file.=========")
		DebugLog ("104 FbxImport_WriteReadTrans_Z_00610 def load() ==============Succeeded to load file.=========")
		DebugLog ("104 FbxImport_WriteReadTrans_Z_00610 def load() ==============Succeeded to load file.=========")
		DebugLog ("104 FbxImport_WriteReadTrans_Z_00610 def load() ==============Succeeded to load file.=========")
		
		DebugLog ("#==========================================================================================================================")
		DebugLog ("#113 FbxImport_WriteReadTrans_Z_00610 def load()    Root_TransZ_AnimCurve_Kye_Value_List Loop ============================")
		DebugLog ("#==========================================================================================================================")
		
		self.Root_TransZ_AnimCurve_Kye_Value_List = GetKeyCurve_Instance.Root_TransZ_AnimCurve_Kye_Value_List
		self.Root_TransZ_AnimCurve_Kye_Value_List_Count=len(  self.Root_TransZ_AnimCurve_Kye_Value_List )
		DebugLog ("#118 104 FbxImport_WriteReadTrans_Z_00610 def load()  self.Root_TransZ_AnimCurve_Kye_Value_List_Count =_ "+str(self.Root_TransZ_AnimCurve_Kye_Value_List_Count)+"===")
		self.ref_TransZwriteReader_instance.DebugLog("\n""\n")
		for R in range(0, self.Root_TransZ_AnimCurve_Kye_Value_List_Count):
			lKeyValue= self.Root_TransZ_AnimCurve_Kye_Value_List[R]
			DebugLog("self.Root_TransZ_AnimCurve_Kye_Value_List["+str(R)+"] = "+str(lKeyValue) )
			
			self.ref_TransZwriteReader_instance.ExportWrite( str(lKeyValue) );
		DebugLog ("#==========================================================================================================================")
		DebugLog ("#113 FbxImport_WriteReadTrans_Z_00610 def load()    _C_Pelvis_TransZ_AnimCurve_Kye_Value_List Loop ============================")
		DebugLog ("#==========================================================================================================================")
		
		self._C_Pelvis_TransZ_AnimCurve_Kye_Value_List = GetKeyCurve_Instance._C_Pelvis_TransZ_AnimCurve_Kye_Value_List
		self._C_Pelvis_TransZ_AnimCurve_Kye_Value_List_Count=len(  self._C_Pelvis_TransZ_AnimCurve_Kye_Value_List )
		DebugLog ("#118 104 FbxImport_WriteReadTrans_Z_00610 def load()  self._C_Pelvis_TransZ_AnimCurve_Kye_Value_List_Count =_ "+str(self._C_Pelvis_TransZ_AnimCurve_Kye_Value_List_Count)+"===")


		DebugLog ("#==========================================================================================================================")
		DebugLog ("#==========================================   Save  EXPORT  F B X =========================================================")
		DebugLog ("#==========================================================================================================================")
		#==========================================================================================================================
		#=================================================== EXPORT ========================================================
		#==========================================================================================================================
				


		Export_Result = FbxCommon.SaveScene(manager, scene, self.FullPass_EXPORT_FBX_FILENAME)
		if Export_Result==0:
			print("Export_Result==0    NG !!!!!!!!!!!!!!!!!!!!!!!!!!!cant out file!!!!!!!!!!!!!!!!!!!!!   ")
			DebugLog("Export_Result==0    NG !!!!!!!!!!!!!!!!!!!!!!!!!!!cant out file!!!!!!!!!!!!!!!!!!!!!   ")
			DebugLog("Export_Result==0    NG !!!!!!!!!!!!!!!!!!!!!!!!!!!cant out file!!!!!!!!!!!!!!!!!!!!!   ")
		else:
			print("Export_Result==1   OK !!!!!!!!!!!!!!!!!!!!!!!!!! out put File               self.FullPass_EXPORT_FBX_FILENAME= "+self.FullPass_EXPORT_FBX_FILENAME)
			DebugLog("Export_Result==1   OK !!!!!!!!!!!!!!!!!!!!!!!!!! out put File  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			DebugLog("Export_Result==1   OK !!!!!!!!!!!!!!!!!!!!!!!!!! out put File  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			DebugLog("Export_Result==1   OK !!!!!!!!!!!!!!!!!!!!!!!!!! out put File  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			DebugLog("Export_Result==1   OK !!!!!!!!!!!!!!!!!!!!!!!!!! out put File  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			DebugLog("Export_Result==1   OK !!!!!!!!!!!!!!!!!!!!!!!!!! out put File  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		#=============================================================================================================================
		#=============================================================================================================================
		#=============================================================================================================================
		print ("==============Destroy All=========")
		importer.Destroy()
		
	def FbxImport_WriteReadTrans_Z_00610(self):
		print("FbxImport_WriteReadTrans_Z_00610_Start.............  filepath  = "+str(filepath))
	def Samething(self):
		print("014 FbxImport_WriteReadTrans_Z_00610 Samething()")
		#//////////////////////////////////////////////////////////////////////////////////////////////////
		#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
		#//////////////////////////////////////////////////////////////////////////////////////////////////		
	def getClassName(self):
		print( u"className= " + self.__class__.__name__)
		return self.__class__.__name__


#=============================Code Start===============================================
print(" Code Start="+__name__)
Debug_Instance=DebugLogger00100.DebugLogger00100()
FbxCommon00100_Instance = FbxCommon00100.FbxCommon00100()
def DebugLogStart():
	#print("DebugStr = "+ DebugStr)
	Debug_Instance.DebugLogStart()
	
def DebugLog(DebugStr):
	print("DebugStr = "+ DebugStr)
	Debug_Instance.DebugLog(" 88 Logger >>>>>>>>"+DebugStr);
	

FBX_trans_z_Instance = FbxImport_WriteReadTrans_Z_00610()  # Class  export  instance.


GetKeyCurve_Instance = GetKeyCurve00110.GetKeyCurve00110()  # Class  export  instance.

print(" FbxImport_WriteReadTrans_Z_00610 Class  __name__="+__name__)
WriteReadTrans_ZInstance=WriteReadTrans_Z_00310.WriteReadTrans_Z_00310()
WriteReadTrans_ZInstance.fileDataZeroReset()

#//////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////	
def StartMainLine(Debug,WriteReadTrans_Z_Instance,FBX_trans_z_Instance,GetKeyCurve_Instance,FbxCommon00100_Instance):
	print(" ========================== StartMainLine ========================== ")
	print(" ========================== StartMainLine ========================== ")
	print(" ========================== StartMainLine ========================== ")	
	DebugLogStart()
	FBX_trans_z_Instance.Samething()
	FBX_trans_z_Instance.loadFile(FBX_trans_z_Instance.FBX_FILE_PATH_AND_NAME_AND_EXT,WriteReadTrans_Z_Instance,GetKeyCurve_Instance,FbxCommon00100_Instance)
	
	print(" ========================== END StartMainLine ========================== ")
	print(" ========================== END StartMainLine ========================== ")
	print(" ========================== END StartMainLine ========================== ")
	print(" ========================== END StartMainLine ========================== ")
	#DebugLog (u"__name__==self.__class__.__name__  Same!! File Test")
	#DebugLog (u"=============Simple Single Class Unit Test Start==========")
	#Instance.FbxImport_WriteReadTrans_Z_00610() #Call Method
#//////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////	
if(__name__ == FBX_trans_z_Instance.getClassName()):
	print (u"============= 01 Simple Single Class Unit Test Start==== Instance.getClassName() =  "+FBX_trans_z_Instance.getClassName()+" =====")
	#StartMainLine(Debug_Instance,WriteReadTrans_ZInstance,FBX_trans_z_Instance)
elif(__name__ == "FbxImport_WriteReadTrans_Z_00610"):
	print (u"============= 02 Simple Single Class Unit Test Start===== StartMainLine =====")
	#StartMainLine(Debug_Instance,WriteReadTrans_ZInstance,FBX_trans_z_Instance)	
	#Instance.loadFile(FBX_FILE_PATH_AND_NAME_AND_EXT)
elif(__name__ == "__main__"):
	print (u"============= 03 Simple Single Class Unit Test Start===== __main__ =====")
	StartMainLine(Debug_Instance,WriteReadTrans_ZInstance,FBX_trans_z_Instance,GetKeyCurve_Instance,FbxCommon00100_Instance)
else:
	print (u"__name__!=self.__class__.__name__  Othor File Import")
	
#===================GetKeyCurve=========================	
#===================GetKeyCurve=========================	
#===================GetKeyCurve=========================	
#===================GetKeyCurve=========================	
def GetKeyCurve(fbxImporter,pScene):
	print ("===========GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )===========")
	print ("===========GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )===========")
	print ("===========GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )===========")
	print ("===========GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )===========")
	#===================GetKeyCurve=========================	
	#===================GetKeyCurve=========================	
	#===================GetKeyCurve=========================	
	#===================GetKeyCurve=========================
	print ("GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )")
	#==SDKの1シーンであるFbxScene sceneをルートとして次のようにします：
	#==① アニメーションスタック数取得
	#int nbAnimStacks = pScene->GetSrcObjectCount<FbxAnimStack>()


	print ("----GetKeyCurve( fbxImporter.GetAnimStackCount()= "+str(fbxImporter.GetAnimStackCount())+" -------------------")
	intAnimStacks=0
	intAnimStacks=fbxImporter.GetAnimStackCount()
	print ("----GetKeyCurve------ intAnimStacks= "+str(intAnimStacks)+" -------------------")
	print ("----GetKeyCurve( fbxImporter.GetActiveAnimStackName()= "+str(fbxImporter.GetActiveAnimStackName())+" -------------------")


	#==② アニメーションスタック取得
	#for ( int i = 0; i < nbAnimStacks; i++ )
	#FbxAnimStack* lAnimStack = pScene->GetSrcObject<FbxAnimStack>(i);
	TakeInfoList= [0 for i in range(1)]
	del TakeInfoList[0]
	for i in range(0, intAnimStacks):
		DebugLog("for  i="+str(i))
		pTakeInfo=fbxImporter.GetTakeInfo(i);
		DebugLog("for  pTakeInfo="+str(pTakeInfo))
		pTakeName = pTakeInfo.mName;
		DebugLog("for  pTakeName="+str(pTakeName))
		mImportName = pTakeInfo.mImportName;
		DebugLog("for  mImportName="+str(mImportName))
	#===========END=====GetKeyCurve=========================	
	#===========END=====GetKeyCurve=========================
	#===========END=====GetKeyCurve=========================
	#===========END=====GetKeyCurve=========================
	#===========END=====GetKeyCurve=========================
	print ("==== END ==GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )===========")
	print ("==== END ==GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )===========")
	print ("==== END ==GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )===========")
	print ("==== END ==GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )===========")
	print ("==== END ==GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )===========")


