# -*- coding: utf-8 -*-
import os, sys
import re
#===================class Node=========================
class DebugLogger00100() :
	Yen="\\"
	FileName= "DebugLogger00100__Log.txt"
	#print("HD FULL PATH =")
	#HD_FULL_PATH=os.path.abspath(__file__)
	#print("os.path.abspath(__file__)    =     " + HD_FULL_PATH)
	FullPass_DustDataTextFile_TXT= "D:"+Yen+"vs"+Yen+"py"+Yen+FileName
	FullPass_DustDataTextFile_TXT= "C:"+Yen+"vs"+Yen+"py"+Yen+FileName
	FullPass_DustDataTextFile_TXT= "C:"+Yen+"vs"+Yen+"py"+Yen+"fbx"+Yen+"lib"+Yen+"Python27_x64"+Yen+FileName
	#fbx\lib\Python27_x64
	def DebugLogger00100(self):
		print("   DebugLogger00100.py   _Start.............")
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
			mystr=mystr+"\n"
			escapedStrData=self.escape(mystr)
			self.fileReWrite(self.FullPass_DustDataTextFile_TXT,escapedStrData)
			#fileReWrite(FullPass_DustDataTextFile_TXT,mystr)
			#fileWrite(FullPass_DustDataTextFile_TXT,mystr)
			#fileWrite("C:\Users\akiyaman\AppData\Roaming\Adobe\Common","ABC")
			#----------------ファイルを作る------------------
	def DebugLogStart(self):
		self.fileWrite(self.FullPass_DustDataTextFile_TXT,"-------DebugLogStart-------\n")
	def fileWrite(self,fullPass,DataStr):
		print("fileWrite fullPass= "+fullPass)
		print("fileWrite DataStr= "+DataStr)
		f = open(fullPass, 'w') # 書き込みモードで開く
    		#str = "This Data is Temp Please Delete"  # 書き込む文字列
    		#f = open('text.txt', 'w') # 書き込みモードで開く
    		#f.write(str) # 引数の文字列をファイルに書き込む
		f.write(DataStr) # 引数の文字列をファイルに書き込む
		f.close() # ファイルを閉じる

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

Instance = DebugLogger00100()  # Class  export  instance.
print(" DebugLogger00100 Class  __name__="+__name__)

#//////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////	
def StartMainLine(Instance):
	print("StartMainLine")
	Yen="\\"
	FileName=Instance.getClassName() +"__Log.txt"
	print("HD FULL PATH =")
	HD_FULL_PATH=os.path.abspath(__file__)
	print("os.path.abspath(__file__)    =     " + HD_FULL_PATH)
	FullPass_DustDataTextFile_TXT= "D:"+Yen+"vs"+Yen+"py"+Yen+FileName
	FullPass_DustDataTextFile_TXT= "C:"+Yen+"vs"+Yen+"py"+Yen+FileName
	FullPass_DustDataTextFile_TXT= "C:"+Yen+"vs"+Yen+"py"+Yen+"fbx"+Yen+"lib"+Yen+"Python27_x64"+Yen+FileName
	print("FullPass_DustDataTextFile_TXT="+FullPass_DustDataTextFile_TXT)
	#===========================最初のプロジェクト
	Instance.fileWrite(FullPass_DustDataTextFile_TXT,"none...\n")
	
	Instance.DebugLog("77 DabugLog White Data ");
	Instance.DebugLog("77 DabugLog White Data ");
	Instance.DebugLog("78 DabugLog White Data ");
	Instance.DebugLog("78 DabugLog White Data ");
	#DebugLog (u"__name__==self.__class__.__name__  Same!! File Test")
	#DebugLog (u"=============Simple Single Class Unit Test Start==========")
	#Instance.DebugLogger00100() #Call Method
#//////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////	

if(__name__ == Instance.getClassName()):
	print (u"=============Simple Single Class Unit Test Start====Instance.getClassName() =  "+Instance.getClassName()+" =====")
	#StartMainLine(Instance)
elif(__name__ == "DebugLogger00100"):
	print (u"=============Simple Single Class Unit Test Start===== StartMainLine =====")
	StartMainLine(Instance)	
	#Instance.loadFile(FBX_FILE_PATH_AND_NAME_AND_EXT)
elif(__name__ == "__main__"):
	print (u"=============Simple Single Class Unit Test Start===== __main__ =====")
	StartMainLine(Instance)
else:
	print (u"__name__!=self.__class__.__name__  Othor File Import")
	
