# -*- coding: utf-8 -*-
import os, sys
import re
#===================class Node=========================
class WriteReadTrans_Z_00310() :
	Yen="\\"
	FileName= "WriteReadTrans_Z_00310__Log.csv"
	#print("HD FULL PATH =")
	#HD_FULL_PATH=os.path.abspath(__file__)
	#print("os.path.abspath(__file__)    =     " + HD_FULL_PATH)
	FullPass_DustDataTextFile_TXT= "D:"+Yen+"vs"+Yen+"py"+Yen+FileName
	FullPass_DustDataTextFile_TXT= "C:"+Yen+"vs"+Yen+"py"+Yen+FileName
	def WriteReadTrans_Z_00310(self):
		print("WriteReadTrans_Z_00310_Start.............  filepath  = "+str(filepath))
		#self.FullPass_DustDataTextFile_TXT=filepath
		#文字をエスケープする／エスケープを外す   ///////////////////////http://lightson.dip.jp/zope/ZWiki/053_e6_96_87_e5_ad_97_e3_82_92_e3_82_a8_e3_82_b9_e3_82_b1_e3_83_bc_e3_83_97_e3_81_99_e3_82_8b_ef_bc_8f_e3_82_a8_e3_82_b9_e3_82_b1_e3_83_bc_e3_83_97_e3_82_92_e5_a4_96_e3_81_99
	def escape(self,s, quoted=u'\'"\\', escape=u'\\'):
		return re.sub(u'[%s]' % re.escape(quoted),lambda mo: escape + mo.group(),s)
	def unescape(self,s, quoted=u'\'"\\', escape=u'\\'):
		return re.sub(ur'%s([%s])' % (re.escape(escape), re.escape(quoted)),ur'\1',s)
	def DebugLog(self,strData):
		mystr=strData
		print(mystr)
		if mystr=="":
			print("DebugLog    (mystr )  is empty....................")
		else:
			mystr=str(mystr)+","
			#mystr=mystr+"\n"
			escapedStrData=self.escape(mystr)
			self.fileReWrite(self.FullPass_DustDataTextFile_TXT,escapedStrData)
			#fileReWrite(FullPass_DustDataTextFile_TXT,mystr)
			#fileWrite(FullPass_DustDataTextFile_TXT,mystr)
			#fileWrite("C:\Users\akiyaman\AppData\Roaming\Adobe\Common","ABC")
			#----------------ファイルを作る------------------
	def ExportWrite(self,strData):
		self.DebugLog(strData)
	def fileWrite(self,fullPass,DataStr):
		print("fileWrite fullPass= "+fullPass)
		print("fileWrite DataStr= "+DataStr)
		f = open(fullPass, 'w') # 書き込みモードで開く
    		#str = "This Data is Temp Please Delete"  # 書き込む文字列
    		#f = open('text.txt', 'w') # 書き込みモードで開く
    		#f.write(str) # 引数の文字列をファイルに書き込む
		f.write(DataStr) # 引数の文字列をファイルに書き込む
		f.close() # ファイルを閉じる
	def fileDataZeroReset(self):
		self.fileWrite(self.FullPass_DustDataTextFile_TXT,"")
	def fileReWrite(self,fullPass,DataStr):
		print("fileWrite fullPass= "+fullPass)#///////////////////////////////////////////////////////////////////////////////////////////////////////////
		print("fileWrite DataStr= "+DataStr)
		f = open(fullPass, 'a') # 追記書き込みモードで開く
		#str = "This Data is Temp Please Delete"  # 書き込む文字列
    		#f = open('text.txt', 'w') # 書き込みモードで開く
    		#f.write(str) # 引数の文字列をファイルに書き込む
		f.write(DataStr) # 引数の文字列をファイルに書き込む
		f.close() # ファイルを閉じる	
		
	def fileWriteTemp(self,fullPass):
		fileWrite(fullPass,"DustDataTextFile")

		#//////////////////////////////////////////////////////////////////////////////////////////////////
		#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
		#//////////////////////////////////////////////////////////////////////////////////////////////////		
	def getClassName(self):
		print( u"className= " + self.__class__.__name__)
		return self.__class__.__name__

class FbxReaderTrans_Z_00320() :
	def fileRead(self,filepath):
		print("088 fileRead()  filepath = "+str(filepath))
		returnData=""
		f = open(filepath, 'r')
		#returnData = f
		
		poolStr=""
		for row in f:
			print row
			poolStr=poolStr+row

		f.close()
		print("099 fileRead()  poolStr = "+poolStr)
		returnData=str(poolStr)
		print("101 fileRead()  returnData = "+returnData)
		return returnData
	def ReadTransFile(self):
		returnData=""
		FBX_trans_z_Instance = WriteReadTrans_Z_00310()
		returnData =self.fileRead(FBX_trans_z_Instance.FullPass_DustDataTextFile_TXT)
		print("107 ReadSimple() returnData = "+ str(returnData))
		return returnData
		#//////////////////////////////////////////////////////////////////////////////////////////////////
		#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
		#//////////////////////////////////////////////////////////////////////////////////////////////////		
	def getClassName(self):
		print( u"className= " + self.__class__.__name__)
		return self.__class__.__name__


FBX_trans_z_Instance = WriteReadTrans_Z_00310()  # Class  export  instance.
print(" WriteReadTrans_Z_00310 Class  __name__="+__name__)

#//////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////	
def StartMainLine(FBX_trans_z_Instance):
	print("StartMainLine")
	Yen="\\"
	#FileName=FBX_trans_z_Instance.getClassName() +"__Log.csv"
	#print("HD FULL PATH =")
	#HD_FULL_PATH=os.path.abspath(__file__)
	#print("os.path.abspath(__file__)    =     " + HD_FULL_PATH)
	#FullPass_DustDataTextFile_TXT= "D:"+Yen+"vs"+Yen+"py"+Yen+FileName

	#print("FullPass_DustDataTextFile_TXT="+FullPass_DustDataTextFile_TXT)
	#===========================最初のプロジェクト
	#FBX_trans_z_Instance.fileWrite(FullPass_DustDataTextFile_TXT,"")
	FBX_trans_z_Instance.fileDataZeroReset()

	#FBX_trans_z_Instance.ExportWrite("0.111");
	#FBX_trans_z_Instance.ExportWrite("0.222");
	#FBX_trans_z_Instance.ExportWrite("0.333");
	#FBX_trans_z_Instance.ExportWrite("0.444");
	
	#=============================================================================
	print("========================= Write Start==========================")
	floatList = [1.111, 1.222, 1.333, 1.444, 1.555]
	floatListLength=len(floatList)
	for i in range(0, floatListLength):
		print( str(i) )
		print(floatList[i])
		floatNum=floatList[i]
		floatNumstr=str(floatNum)
		#FBX_trans_z_Instance.ExportWrite("0.111");
		FBX_trans_z_Instance.ExportWrite( floatNumstr );
		

	#=============================================================================
	print("========================= Read Start==========================")
	
	FBX_trans_z_Instance2 = FbxReaderTrans_Z_00320()  # Class  export  instance.
	TransZstrData = FBX_trans_z_Instance2.ReadTransFile()
	TransZstr=str(TransZstrData)
	print("TransZstr = _ "+str(TransZstr)+" _ END ")
	
	print("========================= add list Start==========================")
	TransZstrList=TransZstr.split(",")    # 「,」を区切り文字としてリストを返す	
	print("TransZstrList = _ "+str(TransZstrList)+" _ END ")
	TransZstrListLength=len(TransZstrList)
	print("TransZstrListLength = "+str(TransZstrListLength))
	#==========================================
	#==========================================
	TransZ_list = [0]
	#指定のインデックスの要素を削除する
	TransZ_list.pop(0)
	#----------------------------------------------
	for j in range(0, TransZstrListLength):
		print( "TransZ Loop  "+str(j) )
		print(TransZstrList[j])
		TransZnumStr=TransZstrList[j]
		print("TransZnumStr= "+TransZnumStr)
		if(TransZnumStr == ""):
			print("TransZ  empty string  ")
		else:
			TransZnumFloat=float(TransZnumStr)
			TransZ_list.append(TransZnumFloat)
	
	
	#===================TransZ_list debug==============================
	print("========================= =TransZ_list debug      Start==========================")
	TransZ_listLength=len(TransZ_list)
	for d in range(0, TransZ_listLength):
		print( "TransZ_list Loop  Debug "+str(d) )
		TransZnumFloat_d=TransZ_list[d]
		TransZnumStr_d = str(TransZnumFloat_d)
		print("TransZnumStr_d = "+TransZnumStr_d)

	#DebugLog (u"__name__==self.__class__.__name__  Same!! File Test")
	#DebugLog (u"=============Simple Single Class Unit Test Start==========")
	#Instance.WriteReadTrans_Z_00310() #Call Method
#//////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////FBX_trans_z_Instance Class Unit Test /////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////	

if(__name__ == FBX_trans_z_Instance.getClassName()):
	print (u"=============Simple Single Class Unit Test Start====Instance.getClassName() =  "+FBX_trans_z_Instance.getClassName()+" =====")
	#StartMainLine(FBX_trans_z_Instance)
elif(__name__ == "WriteReadTrans_Z_00310"):
	print (u"=============Simple Single Class Unit Test Start===== StartMainLine =====")
	StartMainLine(FBX_trans_z_Instance)	
	#Instance.loadFile(FBX_FILE_PATH_AND_NAME_AND_EXT)
elif(__name__ == "__main__"):
	print (u"=============Simple Single Class Unit Test Start===== __main__ =====")
	StartMainLine(FBX_trans_z_Instance)
else:
	print (u"__name__!=self.__class__.__name__  Othor File Import")
	




