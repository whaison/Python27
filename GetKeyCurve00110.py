# -*- coding: utf-8 -*-
import os, sys
import re
#===================class Node=========================
import DebugLogger00110
from fbx import *
import FbxCommon
from fbx import FbxAnimStack
import inspect
#===================class Node=========================
import WriteReadTrans_Z_00310


class GetKeyCurve00110() :
	#===================GetKeyCurve=========================	
	#===================GetKeyCurve=========================	
	#===================GetKeyCurve=========================	
	#===================GetKeyCurve=========================	
	def GetKeyCurve(self,fbxImporter,pScene):
			
		print ("===========GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )===========")
		print ("GetKeyCurve(pScene= "+str(fbxImporter)+"  pScene="+str(pScene)+" )")
		
		self.WriteReadTrans_ZInstance=WriteReadTrans_Z_00310.WriteReadTrans_Z_00310()
		self.WriteReadTrans_ZInstance.fileDataZeroReset()
		self.WriteReadTrans_ZInstance.fileDataZeroReset()
		#self.WriteReadTrans_ZInstance.ExportWrite( 0.987654321 );
		
		#==========================================
		self.ref_Root_TransZ_AnimCurve_List = [0]
		#指定のインデックスの要素を削除する
		self.ref_Root_TransZ_AnimCurve_List.pop(0)
		#----------------------------------------------
		#==========================================
		self.ref_C_Pelvis_TransZ_AnimCurve_List = [0]
		#指定のインデックスの要素を削除する
		self.ref_C_Pelvis_TransZ_AnimCurve_List.pop(0)
		#----------------------------------------------
		
		#==SDKの1シーンであるFbxScene sceneをルートとして次のようにします：
		#==① アニメーションスタック数取得
		#int nbAnimStacks = pScene->GetSrcObjectCount<FbxAnimStack>()

		print ("----GetKeyCurve( fbxImporter.GetAnimStackCount()= "+str(fbxImporter.GetAnimStackCount())+" -------------------")
		intAnimStacks=0
		intAnimStacks=fbxImporter.GetAnimStackCount()
		print ("----GetKeyCurve------ intAnimStacks= "+str(intAnimStacks)+" -------------------")
		print ("----GetKeyCurve( fbxImporter.GetActiveAnimStackName()= "+str(fbxImporter.GetActiveAnimStackName())+" -------------------")
		#int intAnimStacks = fbxImporter.GetAnimStackCount()
		#print ("nbAnimStacks= "+str(nbAnimStacks))
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
		
			#fbxAnimStack = fbxImporter.GetAnimStackCount(i)
			#DebugLog("for  fbxAnimStack="+str(fbxAnimStack));
			TakeInfoList.append(pTakeInfo);
		
		TakeInfoListLen=len(TakeInfoList)
		i=0
		DebugLog("TakeInfoListLen= "+str(TakeInfoListLen))


		for i in range(0, TakeInfoListLen):
			strTakeInfoList_i_mName = TakeInfoList[i].mName
			print("strTakeInfoList_i_mName= "+strTakeInfoList_i_mName);
			str_A="strTakeInfoList_i_mName="+strTakeInfoList_i_mName
			#DebugLog(str_A)
			TakeInfo=TakeInfoList[i]
			print ("===========GetAnimationLayer ===========")
	
			#==③ アニメーションレイヤー数を取得
			#int nbAnimLayers = pAnimStack->GetMemberCount<FbxAnimLayer>();
			DebugLog("TakeInfo="+str(TakeInfo))
			DebugLog("TakeInfo.mName="+str(TakeInfo.mName))
			DebugLog("TakeInfo.mCurrentLayer="+str(TakeInfo.mCurrentLayer))
			if(TakeInfo.mCurrentLayer==-1):
				DebugLog("TakeInfo.mLayerInfoList=	   AnimLayer	is  None  Or Just One Take1 Time Line	is  This FBX is None Animation File  !!!!!!!")
			else:
				DebugLog("TakeInfo.mLayerInfoList="+str(TakeInfo.mLayerInfoList))
		
		self.DisplayAnimation(pScene)
		

	def DisplayAnimation(self,pScene):
		DebugLog("=====075 def DisplayAnimation.py===DisplayAnimation(pScene = "+ str(pScene)+")==================================")
		DebugLog("=====076 def DisplayAnimation.py===DisplayAnimation(pScene = "+ str(pScene)+")==================================")
		DebugLog("=====077 def DisplayAnimation.py===DisplayAnimation(pScene = "+ str(pScene)+")==================================")

		DebugLog("FbxAnimStack.ClassId="+str(FbxAnimStack.ClassId))
		pFbxAnimStackClassID=FbxAnimStack.ClassId
	
		DebugLog("=====322 def DisplayAnimation.py===  pFbxAnimStackClassID="+str(pFbxAnimStackClassID))
	
		pFbxCriteriaFbxAnimStackClassID=FbxCriteria.ObjectType(FbxAnimStack.ClassId)
		DebugLog("=====322 def DisplayAnimation.py===  pFbxCriteriaFbxAnimStackClassID="+str(pFbxCriteriaFbxAnimStackClassID))
		#pFbxCriteriaFbxAnimStackClassID=
		#loopCount=pScene.GetSrcObjectCount(pFbxAnimStackClassID)
		intSceneAllObjCount=pScene.GetSrcObjectCount(pFbxCriteriaFbxAnimStackClassID)
		DebugLog("=====322 def DisplayAnimation.py===  intSceneAllObjCount=  ____ "+str(intSceneAllObjCount)+" ____")
		#for i in range(pScene.GetSrcObjectCount(FbxAnimStack.ClassId)):
		for i in range(intSceneAllObjCount):
			DebugLog("=====322 def DisplayAnimation.py=== for     DisplayAnimation  i="+str(i))
			lAnimStack = pScene.GetSrcObject(pFbxCriteriaFbxAnimStackClassID, i)
		
			DebugLog("=====322 def DisplayAnimation.py=== lAnimStack  ="+str(lAnimStack)+"=====================AnimStack===OK  >>>>>>>>>>>>>  AnimLayyers")
		
			lOutputString = "======341      Animation Stack Name  is  ==== "
			lOutputString +=str( lAnimStack.GetName())
			lOutputString += "  ================== "
			print(str(lOutputString))
			DebugLog(str(lOutputString))
			self.DisplayAnimationStack(lAnimStack, pScene.GetRootNode(), True)
		
		
		"""
		for i in range(pScene.GetSrcObjectCount(FbxAnimStack.ClassId)):
			lAnimStack = pScene.GetSrcObject(FbxAnimStack.ClassId, i)

			lOutputString = "Animation Stack Name: "
			lOutputString += lAnimStack.GetName()
			lOutputString += "\n"
			print(lOutputString)

			DisplayAnimationStack(lAnimStack, pScene.GetRootNode(), False)
		"""
	def DisplayAnimationStack(self,pAnimStack, pNode, isSwitcher):
		DebugLog("============  361 DisplayAnimationStack======================")
		DebugLog("============  361 DisplayAnimationStack ===   pAnimStack = "+str(pAnimStack)+" ======================")
		DebugLog("============  361 DisplayAnimationStack=== pScene.GetRootNode()    is    pNode = "+str(pNode)+" ======================")
		DebugLog("============  361 DisplayAnimationStack===   isSwitcher = "+str(isSwitcher)+" ======================")
		DebugLog("============  361 DisplayAnimationStack======================")


		pFbxCriteria_FbxAnimLayer=FbxCriteria.ObjectType(FbxAnimLayer.ClassId)
		DebugLog("pFbxCriteria_FbxAnimLayer="+str(pFbxCriteria_FbxAnimLayer))
		nbAnimLayers = pAnimStack.GetSrcObjectCount(pFbxCriteria_FbxAnimLayer)

		lOutputString = "============  361 DisplayAnimationStack========Animation stack contains   nbAnimLayers =  "
		lOutputString += str(nbAnimLayers)
		lOutputString += " Animation Layer"
		lOutputString += " Count is    ___  "
		lOutputString += str(nbAnimLayers)
		lOutputString += "    ____    Animation Layer(s)"
	
		print(lOutputString)
		DebugLog(str(lOutputString))
		for layerCount in range(nbAnimLayers):
		
			lAnimLayer = pAnimStack.GetSrcObject(pFbxCriteria_FbxAnimLayer, layerCount)

			lOutputString = "============  361 DisplayAnimationStack     nbAnimLayers     for  ========  layerCount   == "
			lOutputString += str(layerCount)
			lOutputString = "  lAnimLayer   == "
			lOutputString += str(lAnimLayer)
			print(lOutputString)
		
			DebugLog(str(lOutputString))
		
			DebugLog( "391 ============  361 DisplayAnimationStack     nbAnimLayers     for  == layerCount   == "+str(layerCount))
			DebugLog( "392 ============  361 DisplayAnimationStack     nbAnimLayers     for  == lAnimLayer   == "+str(lAnimLayer))

		self.DisplayAnimationLayer(lAnimLayer, pNode, isSwitcher)

	def DisplayAnimationLayer(self,pAnimLayer, pNode, isSwitcher=False):
		DebugLog("============  398 DisplayAnimationLayer======================")
		DebugLog("============  398 DisplayAnimationLayer ===   pAnimLayer = "+str(pAnimLayer)+" ======================")
		DebugLog("============  398 DisplayAnimationLayer=== pScene.GetRootNode()    is    pNode = "+str(pNode)+" ======================")
		DebugLog("============  398 DisplayAnimationLayer===   isSwitcher = "+str(isSwitcher)+" ======================")
		DebugLog("============  398 DisplayAnimationLayer======================")





		pNodeName=pNode.GetName() 
	
		lOutputString = "============  398 DisplayAnimationLayer=====	 Node Name: "
		lOutputString += pNodeName
		lOutputString += "\n"
		print(lOutputString)
		DebugLog(str(lOutputString))
	
		DebugLog("============  408 DisplayAnimationLayer ===   pNodeName = "+str( pNodeName )+" ======================")
		DebugLog("============  409 DisplayAnimationLayer ===   pAnimLayer = "+str(pAnimLayer)+" ======================")
		#DisplayCurve
		#DisplayCurveKeys(pCurve)
		pDisplayCurveKeys=self.DisplayCurveKeys
		#DebugLog(u"表示カーブキー")
		DebugLog("============  417 DisplayAnimationLayer ===   Function Pointa  pDisplayCurveKeys= "+str(pDisplayCurveKeys))
		#DebugLog("  ??????     pDisplayCurveKeys= "+str(DisplayCurveKeys))
		#======================================================================================================
		#======================================================================================================
		
		#======================================================================================================
		#======================================================================================================
		DebugLog("============  426 DisplayAnimationLayer ===   N e x t L a y e r      !!!!!!!!!!!! "+pNodeName+"    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Start   Get AnimCurve  _")
		DebugLog("============  426 DisplayAnimationLayer ===   N e x t L a y e r      !!!!!!!!!!!! "+pNodeName+"    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Start   Get AnimCurve  _")
		DebugLog("============  426 DisplayAnimationLayer ===   N e x t L a y e r      !!!!!!!!!!!! "+pNodeName+"    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Start   Get AnimCurve  _")
		#======================================================================================================
		#======================================================================================================
		if pNodeName=="C_Pelvis":
			DebugLog("============  426 DisplayAnimationLayer ===   F o u n d      !!!!!!!!!!!! C_Pelvis    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Start   Get AnimCurve  _")
			DebugLog("============  426 DisplayAnimationLayer ===   F o u n d      !!!!!!!!!!!! C_Pelvis    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Start   Get AnimCurve  _")
			DebugLog("============  426 DisplayAnimationLayer ===   F o u n d      !!!!!!!!!!!! C_Pelvis    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Start   Get AnimCurve  _")
			#DisplayChannels_00100(pNode, pAnimLayer, DisplayCurveKeys, DisplayListCurveKeys, isSwitcher) #DisplayChannels がpythonで使えてない事実
			self.DisplayChannels_00050(pNode, pAnimLayer, isSwitcher) 
			DebugLog("============  426 DisplayAnimationLayer ===   F o u n d      !!!!!!!!!!!! C_Pelvis    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!END  Get AnimCurve  _")
			DebugLog("============  426 DisplayAnimationLayer ===   F o u n d      !!!!!!!!!!!! C_Pelvis    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!END  Get AnimCurve  _")
			DebugLog("============  426 DisplayAnimationLayer ===   F o u n d      !!!!!!!!!!!! C_Pelvis    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!END  Get AnimCurve  _")
		#======================================================================================================
		#======================================================================================================
		#======================================================================================================
		if pNodeName=="Root":
			DebugLog("============  426 DisplayAnimationLayer ===   F o u n d      !!!!!!!!!!!! Root    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Start   Get AnimCurve  _")
			DebugLog("============  426 DisplayAnimationLayer ===   F o u n d      !!!!!!!!!!!! Root    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Start   Get AnimCurve  _")
			DebugLog("============  426 DisplayAnimationLayer ===   F o u n d      !!!!!!!!!!!! Root    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Start   Get AnimCurve  _")
			self.DisplayChannels_00050(pNode, pAnimLayer, isSwitcher) 
			self.Root_pNode=pNode
			self.Root_pAnimLayer=pAnimLayer
			self.Root_isSwitcher=isSwitcher
			DebugLog("============  426 DisplayAnimationLayer ===   F o u n d      !!!!!!!!!!!! Root    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!END  Get AnimCurve  _")
			DebugLog("============  426 DisplayAnimationLayer ===   F o u n d      !!!!!!!!!!!! Root    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!END  Get AnimCurve  _")
			DebugLog("============  426 DisplayAnimationLayer ===   F o u n d      !!!!!!!!!!!! Root    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!END  Get AnimCurve  _")
			#self.ref_Root_TransZ_AnimCurve_List
		#====================================いったんコメント====================================================
		#======================================================================================================
		#======================================================================================================
		#======================================================================================================
		#======================================================================================================
		pNode_ChildCount=pNode.GetChildCount()
	
		DebugLog("240 ============  434 DisplayAnimationLayer ===   pNode_ChildCount= _____ "+str(pNode_ChildCount)+" ______")
	
		for lModelCount in range(pNode_ChildCount):
			pNodeChild=pNode.GetChild(lModelCount)
			pNodeChild_Name=pNodeChild.GetName() 
			DebugLog("  ============  439 DisplayAnimationLayer === for  loop=  ____ " +str(pNodeChild_Name)+" __ "+str(lModelCount)+"/"+str(pNode_ChildCount)+"____"+pNodeName+"____")
		
		try:
			self.DisplayAnimationLayer(pAnimLayer, pNodeChild, isSwitcher)
		except NameError, IndexError:
			print IndexError
			print ("250  !!!!!!!!!!!!!!!!!!!!!!!!!      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        UnboundLocalError: local variable 'pNodeChild' referenced before assignment")
			DebugLog ("250  !!!!!!!!!!!!!!!!!!!!!!!!!      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        UnboundLocalError: local variable 'pNodeChild' referenced before assignment")
			DebugLog ("250  !!!!!!!!!!!!!!!!!!!!!!!!!      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        UnboundLocalError: local variable 'pNodeChild' referenced before assignment")
		DebugLog ("257  !!!!!!!!!!!!!!D i s p l a y  A n i m a t i o n   L a y e r  E N D >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>      ")
		DebugLog ("257  !!!!!!!!!!!!!!D i s p l a y  A n i m a t i o n   L a y e r  E N D >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    !!!!!!!!!! "+pNodeName+"    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!!   pNode_ChildCount= _____ "+str(pNode_ChildCount)+" ____!!!!!  ")
		DebugLog ("257  !!!!!!!!!!!!!!D i s p l a y  A n i m a t i o n   L a y e r  E N D >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>      ")
		DebugLog ("257  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DisplayAnimationLayer END !!!!!!!!!! "+pNodeName+"    !!!!  joint   = ___pNodeName__ "+str(pNodeName)+" _____!!!!   pNode_ChildCount= _____ "+str(pNode_ChildCount)+" ____!!!!!! ")
	"""
	class DisplayChannels_Set_Method:
		def DisplayChannels_class_00100_method(self,pNode, pAnimLayer, DisplayCurve, DisplayListCurve, isSwitcher):
			DebugLog("360  DisplayChannels_00100(pNode ="+str(pNode)+", pAnimLayer="+str(pAnimLayer)+", DisplayCurve="+str(DisplayCurve)+", DisplayListCurve="+str(DisplayListCurve)+", isSwitcher="+str(isSwitcher)+")")
			DebugLog("361  DisplayChannels_00100()    end")
			lAnimCurve = None
			DisplayChannels_00200_isSwitcher(pNode, pAnimLayer, isSwitcher)
		
	
	"""
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#====================================DisplayChannels_00050==============================================
	#======================================================================================================
	#======================================================================================================


	def DisplayChannels_00050(self,pNode, pAnimLayer, isSwitcher):	
		DebugLog("462  DisplayChannels_00050()")
		DebugLog("462  DisplayChannels_00050()")
		DebugLog("462  DisplayChannels_00050()")
		pNode_Name=pNode.GetName()
		DebugLog("465  DisplayChannels_00050               pNode_Name    =      "+str(pNode_Name)+"           !!!!!!!!           )")
		DebugLog("465  DisplayChannels_00050(pNode ="+str(pNode)+")")
		DebugLog("466  DisplayChannels_00050(pAnimLayer="+str(pAnimLayer)+")")
		DebugLog("467  DisplayChannels_00050(isSwitcher="+str(isSwitcher)+")")
		lAnimCurve = None
		lAnimCurve= self.DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_(pNode, pAnimLayer, isSwitcher,lAnimCurve)
	
		DebugLog("470  DisplayChannels_00050()    end      pNode_Name=    "+pNode_Name+"                ==============>>>>>                         AnimCurve   =  "+str(lAnimCurve))
		if lAnimCurve==None:
			DebugLog("DisplayChannels_00050!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   N o t A n i m C u r v e !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		else:
			DebugLog("292 DisplayChannels_00050!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   G e t A n i m C u r v e !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
			DebugLog("292 DisplayChannels_00050!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   G e t A n i m C u r v e !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
			DebugLog("292 DisplayChannels_00050!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   G e t A n i m C u r v e !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
			DebugLog("292 DisplayChannels_00050!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   G e t A n i m C u r v e !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
			DebugLog("292 DisplayChannels_00050!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   G e t A n i m C u r v e !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		lNodeAttribute = pNode.GetNodeAttribute()
		self.DisplayChannels_00300_is_lNodeAttribute_00100_Color_X_Red_Y_Green_Z_Blue_(pNode, pAnimLayer,lAnimCurve,lNodeAttribute)
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!DisplayChannels_00300_is_lNodeAttribute_00100_Color_X_Red_Y_Green_Z_Blue_     END=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )

		self.DisplayChannels_00400_is_lNodeAttribute_00200_Light_LightPowerIntensity__LightConeAngle__LightMinusFog_(pNode, pAnimLayer,lAnimCurve,lNodeAttribute)
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!DisplayChannels_00400_is_lNodeAttribute_00200_Light_LightPowerIntensity__LightConeAngle__LightMinusFog_    END=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		self.DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__(pNode, pAnimLayer,lAnimCurve,lNodeAttribute)
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__    END=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		self.DisplayChannels_00600_is_lNodeAttribute_00400_GeometryBlendShapeDeformer__(pNode, pAnimLayer,lAnimCurve,lNodeAttribute)
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!DisplayChannels_00600_is_lNodeAttribute_00400_GeometryBlendShapeDeformer__    END=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		# Display curves specific to properties
		lProperty = pNode.GetFirstProperty()
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!  lProperty = pNode.GetFirstProperty()    END=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		GoWhileLoop=lProperty.IsValid()
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!  GoWhileLoop=lProperty.IsValid()    END=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("427 DisplayChannels_00050                   lProperty.IsValid()==GoWhileLoop=="+str(GoWhileLoop))
		self.DisplayChannels_00850_is__CurvesProperties_(pNode, pAnimLayer,lAnimCurve,lNodeAttribute,lProperty)
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!  GoWhileLoop=DisplayChannels_00850_is__CurvesProperties_.IsValid()    END=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   E N D  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   E N D  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   E N D  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!!!!DisplayChannels_00050 > 850 !!!!!!!!!!   E N D  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   E N D  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		DebugLog("483 DisplayChannels_00050() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   E N D  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>    pNode_Name=    "+pNode_Name+"                                 AnimCurve   =  "+str(lAnimCurve)   )
		
		
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#====================================DisplayCurve_00100_==============================================
	#======================================================================================================
	#======================================================================================================

	def DisplayCurve_00100_(self,pCurve,pNode):
		DebugLog("938                             >>>>>>>>>>>>>>>>>>>>>>>>>>>DisplayCurve(pCurve= "+str(pCurve)+")")
		#DisplayCurve_00100_(pCurve)
		self.DisplayCurveKeys(pCurve,pNode)

	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================

	def DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_(self,pNode, pAnimLayer, isSwitcher,_AnimCurve_):
		
		DebugLog(" 444          DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_    Swich    Swich   Swich     End ")
		DebugLog(" 445          DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_    Swich    Swich   Swich     End ")
		lAnimCurve = _AnimCurve_
		pNode_Name=pNode.GetName()
		DebugLog("448  DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_(pNode_Name ="+str(pNode_Name)+")")
		DebugLog("448  DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_(pNode ="+str(pNode)+")")
		DebugLog("449  DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_(pAnimLayer="+str(pAnimLayer)+")")
		DebugLog("450  DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_(isSwitcher="+str(isSwitcher)+")")
		DebugLog("451  DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_(lAnimCurve="+str(lAnimCurve)+")")
	
		KFCURVENODE_T_X = "X"
		KFCURVENODE_T_Y = "Y"
		KFCURVENODE_T_Z = "Z"

		KFCURVENODE_R_X = "X"
		KFCURVENODE_R_Y = "Y"
		KFCURVENODE_R_Z = "Z"
		KFCURVENODE_R_W = "W"

		KFCURVENODE_S_X = "X"
		KFCURVENODE_S_Y = "Y"
		KFCURVENODE_S_Z = "Z"
	
		# Display general curves.
		#if not isSwitcher:
		if isSwitcher:
			lAnimCurve = pNode.LclTranslation.GetCurve(pAnimLayer, KFCURVENODE_T_X)
			DebugLog("321 DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_!!!!!!!!!!!!!!!!   G e t A n i m C u r v e !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>   pNode_Name=    "+pNode_Name+"                           AnimCurve   =  "+str(lAnimCurve)   )
			DebugLog("321 DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_!!!!!!!!!!!!!!!!   G e t A n i m C u r v e !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>   pNode_Name=    "+pNode_Name+"                           AnimCurve   =  "+str(lAnimCurve)   )
			DebugLog("321 DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_!!!!!!!!!!!!!!!!   G e t A n i m C u r v e !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>   pNode_Name=    "+pNode_Name+"                           AnimCurve   =  "+str(lAnimCurve)   )
			DebugLog("321 DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_!!!!!!!!!!!!!!!!   G e t A n i m C u r v e !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>   pNode_Name=    "+pNode_Name+"                           AnimCurve   =  "+str(lAnimCurve)   )
			DebugLog("321 DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_!!!!!!!!!!!!!!!!   G e t A n i m C u r v e !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=>>>>>   pNode_Name=    "+pNode_Name+"                           AnimCurve   =  "+str(lAnimCurve)   )
			if lAnimCurve:
				DebugLog("327  Transform X!!!!!!!!!!!!!!!!!!!!=>>>>>                         AnimCurve   =  "+str(lAnimCurve) )
				#self.DisplayCurve_00100_(lAnimCurve)
			lAnimCurve = pNode.LclTranslation.GetCurve(pAnimLayer, KFCURVENODE_T_Y)
			if lAnimCurve:
				DebugLog("331  Transform Y!!!!!!!!!!!!!!!!!!!!=>>>>>                         AnimCurve   =  "+str(lAnimCurve) )
				#self.DisplayCurve_00100_(lAnimCurve)
			lAnimCurve = pNode.LclTranslation.GetCurve(pAnimLayer, KFCURVENODE_T_Z)
			if lAnimCurve:
				
				DebugLog("335  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    ")
				DebugLog("336  Transform Z!!!!!!!!!!!!!!!!!!!!=>>>>>        pNode_Name   "+pNode_Name+"     AnimCurve   =  "+str(lAnimCurve) )
				if  pNode_Name=="Root":
					self.DisplayCurve_00100_(lAnimCurve,pNode)
					self.ref_Root_TransZ_AnimCurve_List.append(lAnimCurve)
				if pNode_Name=="C_Pelvis":
					self.DisplayCurve_00100_(lAnimCurve,pNode)
					self.ref_C_Pelvis_TransZ_AnimCurve_List.append(lAnimCurve)
					#self.DisplayCurve_00100_KeysEdit_(lAnimCurve)
					#self.DisplayCurve_00100_(lAnimCurve)
				DebugLog("340  DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_!!!!  DisplayCurve_00100_ END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    ")
				DebugLog("341  DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_!!!!  DisplayCurve_00100_ END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    ")
				DebugLog("342  DisplayChannels_00200_isSwitcher_Transform_XYZ_Rotation_XYZ_Scale_XYZ_!!!!  DisplayCurve_00100_ END  !!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    ")

			lAnimCurve = pNode.LclRotation.GetCurve(pAnimLayer, KFCURVENODE_R_X)
			if lAnimCurve:
				DebugLog("		Rotation X")
				#self.DisplayCurve_00100_(lAnimCurve)
			lAnimCurve = pNode.LclRotation.GetCurve(pAnimLayer, KFCURVENODE_R_Y)
			if lAnimCurve:
				DebugLog("		Rotation Y")
				#self.DisplayCurve_00100_(lAnimCurve)
			lAnimCurve = pNode.LclRotation.GetCurve(pAnimLayer, KFCURVENODE_R_Z)
			if lAnimCurve:
				DebugLog("		Rotation Z")
				#self.DisplayCurve_00100_(lAnimCurve)

			lAnimCurve = pNode.LclScaling.GetCurve(pAnimLayer, KFCURVENODE_S_X)
			if lAnimCurve:
				DebugLog("		Scale X")
				#self.DisplayCurve_00100_(lAnimCurve)
			lAnimCurve = pNode.LclScaling.GetCurve(pAnimLayer, KFCURVENODE_S_Y)
			if lAnimCurve:
				DebugLog("		Scale Y")
				#self.DisplayCurve_00100_(lAnimCurve)
			lAnimCurve = pNode.LclScaling.GetCurve(pAnimLayer, KFCURVENODE_S_Z)
			if lAnimCurve:
				DebugLog("		Scale Z")
				#self.DisplayCurve_00100_(lAnimCurve)
			
		
		#else:
		
		
		
	
		print(" 415          DisplayChannels_00200_isSwitcher          End ")
		return lAnimCurve


	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============           DisplayChannels_00300_is_lNodeAttribute_00100_Color_X_Red_Y_Green_Z_Blue_                                 ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================


	def DisplayChannels_00300_is_lNodeAttribute_00100_Color_X_Red_Y_Green_Z_Blue_(self,pNode, pAnimLayer,_AnimCurve_,_lNodeAttribute_):
		DebugLog(" 484          DisplayChannels_00300_is_lNodeAttribute_00100_Color_X_Red_Y_Green_Z_Blue_    lNodeAttribute    lNodeAttribute   lNodeAttribute     End ")
		DebugLog(" 485          DisplayChannels_00300_is_lNodeAttribute_00100_Color_X_Red_Y_Green_Z_Blue_    lNodeAttribute    lNodeAttribute   lNodeAttribute     End ")
	
		lNodeAttribute = _lNodeAttribute_
		lAnimCurve = _AnimCurve_
		DebugLog("488  DisplayChannels_00300_is_lNodeAttribute_00100_Color_X_Red_Y_Green_Z_Blue_(pNode ="+str(pNode)+")")
		DebugLog("489  DisplayChannels_00300_is_lNodeAttribute_00100_Color_X_Red_Y_Green_Z_Blue_(pAnimLayer="+str(pAnimLayer)+")")
		DebugLog("490  DisplayChannels_00300_is_lNodeAttribute_00100_Color_X_Red_Y_Green_Z_Blue_(lAnimCurve="+str(lAnimCurve)+")")
		DebugLog("491  DisplayChannels_00300_is_lNodeAttribute_00100_Color_X_Red_Y_Green_Z_Blue_(lNodeAttribute="+str(lNodeAttribute)+")")
		# Display curves specific to a light or marker.
		#lNodeAttribute = pNode.GetNodeAttribute()
	
	
		KFCURVENODE_COLOR_RED = "X"
		KFCURVENODE_COLOR_GREEN = "Y"
		KFCURVENODE_COLOR_BLUE = "Z"
	
		if lNodeAttribute:
			lAnimCurve = lNodeAttribute.Color.GetCurve(pAnimLayer, KFCURVENODE_COLOR_RED)
			if lAnimCurve:
				DebugLog("	X	Red")
				self.DisplayCurve_00100_(lAnimCurve)
			lAnimCurve = lNodeAttribute.Color.GetCurve(pAnimLayer, KFCURVENODE_COLOR_GREEN)
			if lAnimCurve:
				DebugLog("	Y	Green")
				self.DisplayCurve_00100_(lAnimCurve)
			lAnimCurve = lNodeAttribute.Color.GetCurve(pAnimLayer, KFCURVENODE_COLOR_BLUE)
			if lAnimCurve:
				DebugLog("	Z	Blue")
				self.DisplayCurve_00100_(lAnimCurve)


	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#============= DisplayChannels_00400_is_lNodeAttribute_00200_Light_LightPowerIntensity__LightConeAngle__LightMinusFog_    ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================

	def DisplayChannels_00400_is_lNodeAttribute_00200_Light_LightPowerIntensity__LightConeAngle__LightMinusFog_(self,pNode, pAnimLayer,_AnimCurve_,_lNodeAttribute_):
		DebugLog(" 516          DisplayChannels_00400_is_lNodeAttribute_00200_Light_LightPowerIntensity__LightConeAngle__LightMinusFog_    lNodeAttribute    lNodeAttribute   lNodeAttribute     End ")
		DebugLog(" 517          DisplayChannels_00400_is_lNodeAttribute_00200_Light_LightPowerIntensity__LightConeAngle__LightMinusFog_    lNodeAttribute    lNodeAttribute   lNodeAttribute     End ")
	
		lNodeAttribute = _lNodeAttribute_
		lAnimCurve = _AnimCurve_
		DebugLog("521 DisplayChannels_00400_is_lNodeAttribute_00200_Light_LightPowerIntensity__LightConeAngle__LightMinusFog_(pNode ="+str(pNode)+")")
		DebugLog("522  DisplayChannels_00400_is_lNodeAttribute_00200_Light_LightPowerIntensity__LightConeAngle__LightMinusFog_(pAnimLayer="+str(pAnimLayer)+")")
		DebugLog("523  DisplayChannels_00400_is_lNodeAttribute_00200_Light_LightPowerIntensity__LightConeAngle__LightMinusFog_(lAnimCurve="+str(lAnimCurve)+")")
		DebugLog("524  DisplayChannels_00400_is_lNodeAttribute_00200_Light_LightPowerIntensity__LightConeAngle__LightMinusFog_(lNodeAttribute="+str(lNodeAttribute)+")")
		if lNodeAttribute:
			# Display curves specific to a light.
			light = pNode.GetLight()
			if light:
				lAnimCurve = light.Intensity.GetCurve(pAnimLayer)
				if lAnimCurve:
					DebugLog("  Light Power watts lumens	Intensity")
					self.DisplayCurve_00100_(lAnimCurve)

				lAnimCurve = light.OuterAngle.GetCurve(pAnimLayer)
				if lAnimCurve:
					DebugLog("	 Light Cone Angle")
					self.DisplayCurve_00100_(lAnimCurve)

				lAnimCurve = light.Fog.GetCurve(pAnimLayer)
				if lAnimCurve:
					DebugLog("	 light  Power Down Minus-- Value like a Fog")
					self.DisplayCurve_00100_(lAnimCurve)
	

	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#============= DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__  ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================

	def DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__(self,pNode, pAnimLayer,_AnimCurve_,_lNodeAttribute_):
		DebugLog(" 516          DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__    lNodeAttribute    lNodeAttribute   lNodeAttribute     End ")
		DebugLog(" 517          DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__    lNodeAttribute    lNodeAttribute   lNodeAttribute     End ")
	
		lNodeAttribute = _lNodeAttribute_
		lAnimCurve = _AnimCurve_
		DebugLog("521 DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__(pNode ="+str(pNode)+")")
		DebugLog("522  DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__(pAnimLayer="+str(pAnimLayer)+")")
		DebugLog("523  DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__(lAnimCurve="+str(lAnimCurve)+")")
		DebugLog("524  DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__(lNodeAttribute="+str(lNodeAttribute)+")")
		if lNodeAttribute:
			# Display curves specific to a camera.
			camera = pNode.GetCamera()
			if camera:
				lAnimCurve = camera.FieldOfView.GetCurve(pAnimLayer)
				if lAnimCurve:
					DebugLog("	      Camera    Field of View Angles")
					self.DisplayCurve_00100_(lAnimCurve)

				lAnimCurve = camera.FieldOfViewX.GetCurve(pAnimLayer)
				if lAnimCurve:
					DebugLog("      Camera    Field of View Wide X")
					self.DisplayCurve_00100_(lAnimCurve)

				lAnimCurve = camera.FieldOfViewY.GetCurve(pAnimLayer)
				if lAnimCurve:
					DebugLog("      Camera    Field of View Height Y")
					self.DisplayCurve_00100_(lAnimCurve)

				lAnimCurve = camera.OpticalCenterX.GetCurve(pAnimLayer)
				if lAnimCurve:
					DebugLog("      Camera    Optic_eyeScreen =StudyOfLight  360 No-parallax point Camera Lens Center X")
					self.DisplayCurve_00100_(lAnimCurve)

				lAnimCurve = camera.OpticalCenterY.GetCurve(pAnimLayer)
				if lAnimCurve:
					DebugLog("      Camera    Optical eyeScreen =StudyOfLight  360 No-parallax point Camera Lens Center Y")
					self.DisplayCurve_00100_(lAnimCurve)

				lAnimCurve = camera.Roll.GetCurve(pAnimLayer)
				if lAnimCurve:
					DebugLog("      Camera    Roll")
					self.DisplayCurve_00100_(lAnimCurve)

		DebugLog("591  DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__")


	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	def DisplayChannels_00600_is_lNodeAttribute_00400_GeometryBlendShapeDeformer__(self,pNode, pAnimLayer,_AnimCurve_,_lNodeAttribute_):
		DebugLog(" 516          DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__    lNodeAttribute    lNodeAttribute   lNodeAttribute     End ")
		DebugLog(" 517          DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__    lNodeAttribute    lNodeAttribute   lNodeAttribute     End ")
	
		lNodeAttribute = _lNodeAttribute_
		lAnimCurve = _AnimCurve_
		DebugLog("521 DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__(pNode ="+str(pNode)+")")
		DebugLog("522  DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__(pAnimLayer="+str(pAnimLayer)+")")
		DebugLog("523  DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__(lAnimCurve="+str(lAnimCurve)+")")
		DebugLog("524  DisplayChannels_00500_is_lNodeAttribute_00300_Camera_float_FieldOfViewAngle_FieldOfView_WideX_HeightY_360LensCenterXY_Roll__(lNodeAttribute="+str(lNodeAttribute)+")")
		if lNodeAttribute:
			# Display curves specific to a geometry.
			intBool_GeometryBlendShapeDeformer=0;
		
			if lNodeAttribute.GetAttributeType() == FbxNodeAttribute.eMesh :
				intBool_GeometryBlendShapeDeformer=1;
			if lNodeAttribute.GetAttributeType() == FbxNodeAttribute.eNurbs :
				intBool_GeometryBlendShapeDeformer=1;
			if lNodeAttribute.GetAttributeType() == FbxNodeAttribute.ePatch :
				intBool_GeometryBlendShapeDeformer=1;
			
			if intBool_GeometryBlendShapeDeformer==1:
				DebugLog("  intBool_GeometryBlendShapeDeformer =1    is   Autodesk Bug !!!!!!!!!    UnUse  Or  Bake  Deform")
			
			"""
		
			if lNodeAttribute.GetAttributeType() == FbxNodeAttribute.eMesh or \
				lNodeAttribute.GetAttributeType() == FbxNodeAttribute.eNurbs or \
				lNodeAttribute.GetAttributeType() == FbxNodeAttribute.ePatch:
				lGeometry = lNodeAttribute

				lBlendShapeDeformerCount = lGeometry.GetDeformerCount(FbxDeformer.eBlendShape)
				for lBlendShapeIndex in range(lBlendShapeDeformerCount):
					lBlendShape = lGeometry.GetDeformer(lBlendShapeIndex, FbxDeformer.eBlendShape)
					lBlendShapeChannelCount = lBlendShape.GetBlendShapeChannelCount()
					for lChannelIndex in range(lBlendShapeChannelCount):
						lChannel = lBlendShape.GetBlendShapeChannel(lChannelIndex)
						lChannelName = lChannel.GetName()
						lAnimCurve = lGeometry.GetShapeChannel(lBlendShapeIndex, lChannelIndex, pAnimLayer, True)
						if lAnimCurve:
							DebugLog("		Shape %s" % lChannelName)
							DisplayCurve(lAnimCurve)
			"""
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	def DisplayChannels_00850_is__CurvesProperties_(self,pNode, pAnimLayer,_AnimCurve_,_lNodeAttribute_,_lProperty_):
		DebugLog(" 663          DisplayChannels_00850_is__CurvesProperties_    CurveProperties    CurveProperties   CurveProperties     End ")
		DebugLog(" 664          DisplayChannels_00850_is__CurvesProperties_    CurveProperties    CurveProperties   CurveProperties     End ")
	
		lNodeAttribute = _lNodeAttribute_
		lAnimCurve = _AnimCurve_
		DebugLog("668 DisplayChannels_00850_is__CurvesProperties_(pNode ="+str(pNode)+")")
		DebugLog("669  DisplayChannels_00850_is__CurvesProperties_(pAnimLayer="+str(pAnimLayer)+")")
		DebugLog("670  DisplayChannels_00850_is__CurvesProperties_(lAnimCurve="+str(lAnimCurve)+")")
		DebugLog("671  DisplayChannels_00850_is__CurvesProperties_(lNodeAttribute="+str(lNodeAttribute)+")")
		# Display curves specific to properties
		#lProperty = pNode.GetFirstProperty()
		lProperty = _lProperty_
	
		GoWhileLoop=lProperty.IsValid()
		lPropertyIs_OK=lProperty.IsValid()
		DebugLog("681    ------------------------   DisplayChannels_00850_is__CurvesProperties_    lProperty.IsValid()==lPropertyIs_OK=="+str(lPropertyIs_OK))
		#「while」文では、条件式が真(true)の間繰り返しを行います。
		#======================================================================================================
		intWhileCount=0
		#while GoWhileLoop:
		for var in range(0, 10):
			self.DisplayChannels_00850_is_Loop_inside(pNode, lProperty)
	
		if lPropertyIs_OK:
			DebugLog("687   lPropertyIs_OK             DisplayChannels_00850_is__CurvesProperties_            inside                   if              ----------------------------------------")
		#======================================================================================================
			#DebugLog("GO While Loop")
			if lProperty.GetFlag(FbxPropertyFlags.eUserDefined):
				lFbxFCurveNodeName  = lProperty.GetName()
				lCurveNode = lProperty.GetCurveNode(pAnimLayer)

				if not lCurveNode:
					lProperty = pNode.GetNextProperty(lProperty)
					#continue

				lDataType = lProperty.GetPropertyDataType()
				self.DisplayChannels_00850_is_DataType_Checker_if_Bool_Double_Float_FbxInt_(lAnimCurve,lCurveNode,lDataType)
				self.DisplayChannels_00850_is_DataType_Checker_if_Double3_Double4_FbxColor3DT_FbxColor4DT_(lAnimCurve,lCurveNode,lDataType)
				self.DisplayChannels_00850_is_DataType_Checker_if_Enum_(lAnimCurve,lCurveNode,lDataType)
	
			lProperty = pNode.GetNextProperty(lProperty)
			GoWhileLoop=lProperty.IsValid()
			intWhileCount=intWhileCount+1
			if intWhileCount>1000:
				print("while loop 1000 Over Times  Get Out This Loop   intWhileCount="+str(intWhileCount) )
				GoWhileLoop=False
			DebugLog("772   lPropertyIs_OK                         inside                   if       end       ----------------------------------------")
		#while Loop END Indent.
		#while GoWhileLoop:
		#======================================================================================================
	
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	def DisplayChannels_00850_is_Loop_inside(self,_pNode_,lProperty):
		DebugLog(" 682          DisplayChannels_00850_is_Loop_inside    CurveProperties    CurveProperties   CurveProperties     End ")
		pNode=_pNode_
		#lAnimCurve=_AnimCurve_
		#lCurveNode=_CurveNode_
		#lDataType = _lDataType_
		lPropertyIs_OK=lProperty.IsValid()
		DebugLog("718    ------------------------   DisplayChannels_00850_is_Loop_insideDisplayChannels_00850_is_Loop_inside    lProperty.IsValid()==lPropertyIs_OK=="+str(lPropertyIs_OK))
		#「while」文では、条件式が真(true)の間繰り返しを行います。
		#======================================================================================================
		intWhileCount=0
		#while GoWhileLoop:
	
	
		if lPropertyIs_OK:
			DebugLog("726  DisplayChannels_00850_is_Loop_inside                         inside                   if              ----------------------------------------")
			#======================================================================================================
			#DebugLog("GO While Loop")
			if lProperty.GetFlag(FbxPropertyFlags.eUserDefined):
				lFbxFCurveNodeName  = lProperty.GetName()
				lCurveNode = lProperty.GetCurveNode(pAnimLayer)

				if not lCurveNode:
					lProperty = pNode.GetNextProperty(lProperty)
					#continue

				lDataType = lProperty.GetPropertyDataType()
				self.DisplayChannels_00850_is_DataType_Checker_if_Bool_Double_Float_FbxInt_(lAnimCurve,lCurveNode,lDataType)
				self.DisplayChannels_00850_is_DataType_Checker_if_Double3_Double4_FbxColor3DT_FbxColor4DT_(lAnimCurve,lCurveNode,lDataType)
				self.DisplayChannels_00850_is_DataType_Checker_if_Enum_(lAnimCurve,lCurveNode,lDataType)
	
			lProperty = pNode.GetNextProperty(lProperty)
			GoWhileLoop=lProperty.IsValid()
			intWhileCount=intWhileCount+1
			if intWhileCount>1000:
				print(" 746  while loop 1000 Over Times  Get Out This Loop   intWhileCount="+str(intWhileCount) )
				GoWhileLoop=False
			DebugLog("748   lPropertyIs_OK                         inside                   if       end       ----------------------------------------")
	
	

	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	def DisplayChannels_00850_is_DataType_Checker_if_Bool_Double_Float_FbxInt_(self,_AnimCurve_,_CurveNode_,_lDataType_):
		lAnimCurve=_AnimCurve_
		lCurveNode=_CurveNode_
		lDataType = _lDataType_
		DebugLog("773 DisplayChannels_00850_is_DataType_Checker_if_Bool_Double_Float_FbxInt_          lDataType= "+str(lDataType) )
		if lDataType.GetType() == eFbxBool or lDataType.GetType() == eFbxDouble or lDataType.GetType() == eFbxFloat or lDataType.GetType() == eFbxInt:
			DebugLog("779 >>>>>>>>>>>>>>>>Propaty_DataType_is_Bool_Double_Float_FbxInt_          lDataType= "+str(lDataType.GetType() ) )
			lMessage =  "780		  Property     "
			lMessage += lProperty.GetName()
			if lProperty.GetLabel().GetLen() > 0:
				lMessage += "    (Label: "
				lMessage += lProperty.GetLabel()
				lMessage += ")"

			self.DisplayString(lMessage)
				
			self.DisplayChannels_00850_is__CurvesProperties_00100_CurveNode_CurveCount_For_Loop_(lAnimCurve,lCurveNode)

	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	def DisplayChannels_00850_is_DataType_Checker_if_Double3_Double4_FbxColor3DT_FbxColor4DT_(self,_AnimCurve_,_CurveNode_,_lDataType_):
		lAnimCurve=_AnimCurve_
		lCurveNode=_CurveNode_
		lDataType = _lDataType_
		DebugLog("795 DisplayChannels_00850_is_DataType_Checker_if_Double3_Double4_FbxColor3DT_FbxColor4DT_          lDataType= "+str(lDataType) )
		if lDataType.GetType() == eFbxDouble3 or lDataType.GetType() == eFbxDouble4 or lDataType.Is(FbxColor3DT) or lDataType.Is(FbxColor4DT):
			if lDataType.Is(FbxColor3DT) or lDataType.Is(FbxColor4DT):
				lComponentName1 = KFCURVENODE_COLOR_RED
				lComponentName2 = KFCURVENODE_COLOR_GREEN
				lComponentName3 = KFCURVENODE_COLOR_BLUE					
			else:
				lComponentName1 = "X"
				lComponentName2 = "Y"
				lComponentName3 = "Z"
				
			lMessage =  "		Property "
			lMessage += lProperty.GetName()
			if lProperty.GetLabel().GetLen() > 0:
				lMessage += " (Label: "
				lMessage += lProperty.GetLabel()
				lMessage += ")"
			self.DisplayString(lMessage)
				
			CurveNum=0
			DisplayComponentName=lComponentName1
			self.DisplayChannels_00850_is__CurvesProperties_00600_For_Loop_CurveNum_DisplayComponentName_(lAnimCurve,lCurveNode,CurveNum,DisplayComponentName)
			
			CurveNumber=1
			DisplayComponentName=lComponentName2
			self.DisplayChannels_00850_is__CurvesProperties_00600_For_Loop_CurveNum_DisplayComponentName_(lAnimCurve,lCurveNode,CurveNum,DisplayComponentName)

			CurveNumber=2
			DisplayComponentName=lComponentName3
			self.DisplayChannels_00850_is__CurvesProperties_00600_For_Loop_CurveNum_DisplayComponentName_(lAnimCurve,lCurveNode,CurveNum,DisplayComponentName)

	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	def  DisplayChannels_00850_is_DataType_Checker_if_Enum_(self,_AnimCurve_,_CurveNode_,_lDataType_):
		lAnimCurve=_AnimCurve_
		lCurveNode=_CurveNode_
		lDataType = _lDataType_
		if lDataType.GetType() == eFbxEnum:
			lMessage =  "		Property "
			lMessage += lProperty.GetName()
			if lProperty.GetLabel().GetLen() > 0:
				lMessage += " (Label: "
				lMessage += lProperty.GetLabel()
				lMessage += ")"
			self.DisplayString(lMessage)
		
			self.DisplayChannels_00850_is__CurvesProperties_00500_CurveNode_CurveCount_For_Loop_DisplayListCurve_(lAnimCurve,lCurveNode)

	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================

	def DisplayChannels_00850_is__CurvesProperties_00100_CurveNode_CurveCount_For_Loop_(self,_AnimCurve_,_CurveNode_):
		lAnimCurve=_AnimCurve_
		lCurveNode=_CurveNode_
		CurveCount=lCurveNode.GetCurveCount(0)
		DebugLog("780 DisplayChannels_00850_is__CurvesProperties_00100_CurveNode_CurveCount_For_Loop_          CurveCount= "+str(CurveCount) )
		for c in range(CurveCount):
			DebugLog("782  Curve  c  = "+str(c) )
			lAnimCurve = lCurveNode.GetCurve(0, c)
			if lAnimCurve:
				DebugLog("785  >>>>>>>>>>>>>>>>>>>>   lAnimCurve  c  = "+str(lAnimCurve) )
				self.DisplayCurve_00100_(lAnimCurve)
			

	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================

	def DisplayChannels_00850_is__CurvesProperties_00500_CurveNode_CurveCount_For_Loop_DisplayListCurve_(self,_AnimCurve_,_CurveNode_):
		lAnimCurve=_AnimCurve_
		lCurveNode=_CurveNode_
		CurveCount=lCurveNode.GetCurveCount(0)
		DebugLog("793 DisplayChannels_00850_is__CurvesProperties_00100_CurveNode_CurveCount_For_Loop_          CurveCount= "+str(CurveCount) )
		for c in range(CurveCount):
			DebugLog("795  Curve  c  = "+str(c) )
			lAnimCurve = lCurveNode.GetCurve(0, c)
			if lAnimCurve:
				DebugLog("798  >>>>>>>>>>>>>>>>>>>>   lAnimCurve  c  = "+str(lAnimCurve) )
				#DisplayListCurve(lAnimCurve, lProperty)
				self.DisplayListCurve_00100_(lAnimCurve, lProperty)

	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================

	def DisplayChannels_00850_is__CurvesProperties_00600_For_Loop_CurveNum_DisplayComponentName_(self,_AnimCurve_,_CurveNode_,_CurveNum_,_DisplayComponentName_):
		lAnimCurve=_AnimCurve_
		lCurveNode=_CurveNode_
		CurveNum=_CurveNum_
		DisplayComponentName=_DisplayComponentName_
		CurveCount=lCurveNode.GetCurveCount(CurveNum)
		DebugLog("803 DisplayChannels_00850_is__CurvesProperties_00100_CurveNode_CurveCount_For_Loop_          CurveCount= "+str(CurveCount) )
		for c in range(CurveCount):
			lAnimCurve = lCurveNode.GetCurve(CurveNum, c)
			if lAnimCurve:
				DisplayString("		Component ", DisplayComponentName)
				self.DisplayCurve_00100_(lAnimCurve)

	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================



	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================

	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================




	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================




	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================




	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================




	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	def InterpolationFlagToIndex(self,flags):
		#if (flags&KFCURVE_INTERPOLATION_CONSTANT)==KFCURVE_INTERPOLATION_CONSTANT:
		#	return 1
		#if (flags&KFCURVE_INTERPOLATION_LINEAR)==KFCURVE_INTERPOLATION_LINEAR:
		#	return 2
		#if (flags&KFCURVE_INTERPOLATION_CUBIC)==KFCURVE_INTERPOLATION_CUBIC:
		#	return 3
		return 0

	def ConstantmodeFlagToIndex(self,flags):
		#if (flags&KFCURVE_CONSTANT_STANDARD)==KFCURVE_CONSTANT_STANDARD:
		#	return 1
		#if (flags&KFCURVE_CONSTANT_NEXT)==KFCURVE_CONSTANT_NEXT:
		#	return 2
		return 0

	def TangeantmodeFlagToIndex(self,flags):
		#if (flags&KFCURVE_TANGEANT_AUTO) == KFCURVE_TANGEANT_AUTO:
		#	return 1
		#if (flags&KFCURVE_TANGEANT_AUTO_BREAK)==KFCURVE_TANGEANT_AUTO_BREAK:
		#	return 2
		#if (flags&KFCURVE_TANGEANT_TCB) == KFCURVE_TANGEANT_TCB:
		#	return 3
		#if (flags&KFCURVE_TANGEANT_USER) == KFCURVE_TANGEANT_USER:
		#	return 4
		#if (flags&KFCURVE_GENERIC_BREAK) == KFCURVE_GENERIC_BREAK:
		#	return 5
		#if (flags&KFCURVE_TANGEANT_BREAK) ==KFCURVE_TANGEANT_BREAK:
		#	return 6
		return 0

	def TangeantweightFlagToIndex(self,flags):
		#if (flags&KFCURVE_WEIGHTED_NONE) == KFCURVE_WEIGHTED_NONE:
		#	return 1
		#if (flags&KFCURVE_WEIGHTED_RIGHT) == KFCURVE_WEIGHTED_RIGHT:
		#	return 2
		#if (flags&KFCURVE_WEIGHTED_NEXT_LEFT) == KFCURVE_WEIGHTED_NEXT_LEFT:
		#	return 3
		return 0

	def TangeantVelocityFlagToIndex(self,flags):
		#if (flags&KFCURVE_VELOCITY_NONE) == KFCURVE_VELOCITY_NONE:
		#	return 1
		#if (flags&KFCURVE_VELOCITY_RIGHT) == KFCURVE_VELOCITY_RIGHT:
		#	return 2
		#if (flags&KFCURVE_VELOCITY_NEXT_LEFT) == KFCURVE_VELOCITY_NEXT_LEFT:
		#	return 3
		return 0


	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	def DisplayCurveKeys_pProperty(self,pCurve,pProperty):
		interpolation = [ "?", "constant", "linear", "cubic"]
		constantMode =  [ "?", "Standard", "Next" ]
		cubicMode =	 [ "?", "Auto", "Auto break", "Tcb", "User", "Break", "User break" ]
		tangentWVMode = [ "?", "None", "Right", "Next left" ]

		lKeyCount = pCurve.KeyGetCount()

		for lCount in range(lKeyCount):
			lTimeString = ""
			lKeyValue = pCurve.KeyGetValue(lCount)
			lKeyTime  = pCurve.KeyGetTime(lCount)
			lKeyTimeStr=lKeyTime.GetTimeString(lTimeString)
			#FbxProperty
			lKeyValueStr=pProperty.GetEnumValue(lKeyValue)
			lOutputString = "			Key Time: "
			#lOutputString += lKeyTime.GetTimeString(lTimeString)
			lOutputString += str(KeyTimeStr)
			lOutputString += ".... Key Value: "
			lOutputString += str(lKeyValueStr)
			lOutputString += " [ "
			lOutputString += self.interpolation[ InterpolationFlagToIndex(pCurve.KeyGetInterpolation(lCount)) ]
			#if (pCurve.KeyGetInterpolation(lCount)&KFCURVE_INTERPOLATION_CONSTANT) == KFCURVE_INTERPOLATION_CONSTANT:
			#	lOutputString += " | "
			#	lOutputString += constantMode[ ConstantmodeFlagToIndex(pCurve.KeyGetConstantMode(lCount)) ]
			#elif (pCurve.KeyGetInterpolation(lCount)&KFCURVE_INTERPOLATION_CUBIC) == KFCURVE_INTERPOLATION_CUBIC:
			#	lOutputString += " | "
			#	lOutputString += cubicMode[ TangeantmodeFlagToIndex(pCurve.KeyGetTangeantMode(lCount)) ]
			#	lOutputString += " | "
			#	lOutputString += tangentWVMode[ TangeantweightFlagToIndex(pCurve.KeyGetTangeantWeightMode(lCount)) ]
			#	lOutputString += " | "
			#	lOutputString += tangentWVMode[ TangeantVelocityFlagToIndex(pCurve.KeyGetTangeantVelocityMode(lCount)) ]
			
			lOutputString += " ]"
			DebugLog(lOutputString)

	def DisplayCurveDefault(self,pCurve):
		lOutputString = "1030 DisplayCurveDefault()		Default Value:     pCurve=   "
		lOutputString += pCurve.GetValue()
	
		DebugLog(lOutputString)

	
	def DisplayListCurve_00100_(self,pCurve, pProperty):
		DebugLog ("1270                DisplayListCurve_00100_  (pCurve"+str(pCurve)+", pProperty="+str(pProperty)+")=================")
		lKeyCount = pCurve.KeyGetCount()
		DebugLog ("1272                DisplayListCurve_00100_   =============lKeyCount="+str(lKeyCount)+"=================")
		self.DisplayListCurveKeys(self,pCurve, pProperty)

	
	def DisplayListCurveKeys(pCurve, pProperty):
		DebugLog ("1277     DisplayListCurveKeys(pCurve"+str(pCurve)+", pProperty="+str(pProperty)+")=================")
		lKeyCount = pCurve.KeyGetCount()
		DebugLog ("1277     DisplayListCurveKeys                           lKeyCount="+str(lKeyCount)+"=================")
	
		for lCount in range(lKeyCount):
			lOutputString = "			Key Time: "
			lKeyValue = int(pCurve.KeyGetValue(lCount))
			lKeyTime  = pCurve.KeyGetTime(lCount)
			#lKeyTimeString
			#lKeyValue = static_cast<int>(pCurve.KeyGetValue(lCount))
			lOutputString = "			Key Time: "
			#lOutputString += str(lKeyTime.GetTimeString(lTimeString))
			lOutputString += str(lKeyTime)
			lOutputString += ".... Key Value: "
			lOutputString +=str( lKeyValue)
			lOutputString += " ("
			lOutputString += str(pProperty.GetEnumValue(lKeyValue))
			lOutputString += ")"

			DebugLog(lOutputString)
	
	def DisplayListCurveDefault(self,pCurve, pProperty):
		DisplayCurveDefault(pCurve)
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=============   ==============================================
	#======================================================================================================
	#======================================================================================================
	#======================================================================================================



	def DisplayString(self,pHeader, pValue="" , pSuffix=""):
		lString = "005 DisplayString() "
		lString += " pHeader = "
		lString += pHeader
		lString += " pValue = "
		lString += str(pValue)
		lString += " pSuffix = "
		lString += pSuffix
		#print(lString)
		DebugLog(str(lString))
	"""
	// Notepad++: 
	#   File "<string>", line 9, in <module>
	# エラー: No module named DisplayAnimation_fbxsdk_00920_FbxImported_Log_Exported_FbxExported_DisplayChannel00900_SetCurveValue.py <type 'exceptions.ImportError'> # 

	2013/07/17
	Pythonで「ImportError: No module named …」が出た時の3つの対処法
	http://yak-shaver.blogspot.jp/2013/07/pythonimporterror-no-module-named-3.html
	"""
	def DisplayBool(self,pHeader, pValue, pSuffix=""):
		lString = "016 DisplayBool() "
		lString += " pHeader = "
		lString +=  pHeader
		lString += " pValue = "
		if pValue:
			lString += "true"
		else:
			lString += "false"
		lString += " pSuffix = "
		lString += pSuffix
		#print(lString)
		DebugLog(str(lString))

	def DisplayInt(self,pHeader, pValue, pSuffix=""):
		lString = "016 DisplayBool() "
		lString += " pHeader = "
		lString +=  pHeader
		lString += " pValue = "
		lString += str(pValue)
		lString += " pSuffix = "
		lString += pSuffix
		#print(lString)
		DebugLog(str(lString))

	def DisplayDouble(self,pHeader, pValue, pSuffix=""):
		DebugLog("%s%f%s" % (pHeader, pValue, pSuffix))

	def Display2DVector(self,pHeader, pValue, pSuffix=""):
		DebugLog("%s%f, %f%s" % (pHeader, pValue[0], pValue[1], pSuffix))

	def Display3DVector(self,pHeader, pValue, pSuffix=""):
		DebugLog("%s%f, %f, %f%s" % (pHeader, pValue[0], pValue[1], pValue[2], pSuffix))

	def Display4DVector(self,pHeader, pValue, pSuffix=""):
		DebugLog("%s%f, %f, %f, %f%s" % (pHeader, pValue[0], pValue[1], pValue[2], pValue[3], pSuffix))

	def DisplayColor(self,pHeader, pValue, pSuffix=""):
		DebugLog("%s%f (red), %f (green), %f (blue)%s" % (pHeader, pValue.mRed, pValue.mGreen, pValue.mBlue, pSuffix))




	#======================================================================================================
	#======================================================================================================
	#======================================================================================================
	#=====================================DisplayCurveKeys==============================================
	#======================================================================================================
	#======================================================================================================
	def DisplayCurveKeys(self,pCurve,pNode):
		DebugLog("1088                              >>>>>>>>>>>>>>>>>>>>>>>>>>>>DisplayCurveKeys(pCurve= "+str(pCurve)+")")
		pNode_Name=pNode.GetName()
		DebugLog("1090                              >>>>>>>>>>>>>>>>>>>>>>>>>>>>DisplayCurveKeys(pNode_Name= "+str(pNode_Name)+")")
		interpolation = [ "1054?", "constant", "linear", "cubic"]
		constantMode =  [ "1055?", "Standard", "Next" ]
		cubicMode =	[ "1056?", "Auto", "Auto break", "Tcb", "User", "Break", "User break" ]
		tangentWVMode = [ "1057?", "None", "Right", "Next left" ]

		lKeyCount = pCurve.KeyGetCount()
	
	
		DebugLog(" 540  DisplayCurveKeys       lKeyCount=    ___ " +str(lKeyCount)+" _____")
		DebugLog(" 541  DisplayCurveKeys       lKeyCount=    ___ " +str(lKeyCount)+" _____")
		
		for lCount in range(lKeyCount):
			DebugLog(" 943  DisplayCurveKeys      lCount   =  "+str(lCount)+"  _/_lKeyCount= " +str(lKeyCount)+" _____")
			lTimeString = ""
			lKeyValue = pCurve.KeyGetValue(lCount)
			lKeyValueStr=str(lKeyValue)
			#==================================================================================================
			#==================================================================================================
			#==================================================================================================
			if(pNode_Name=="C_Pelvis"):
				self.WriteReadTrans_ZInstance.ExportWrite( lKeyValue );
				DebugLog(" 1077  DisplayCurveKeys      lKeyValueStr   =  "+str(   lKeyValueStr    ) +"  >>>> >>>>>>>>>>>>>  File   Write Z Data.   " +str(   lKeyValueStr    )     +"     " )
				DebugLog("1112 C_Pelvis")
			if(pNode_Name=="Root"):
				DebugLog("1113 Root")
				DebugLog(" 1077  DisplayCurveKeys      lKeyValueStr   =  "+str(   lKeyValueStr    ) +"  >>>> >>>>>>>>>>>>>  File   UnWrite Z Data.   " +str(   lKeyValueStr    )     +"     " )
			#==================================================================================================
			#==================================================================================================
			#==================================================================================================
			#==================================================================================================
			DebugLog(" 1077  DisplayCurveKeys      lKeyValueStr   =  "+str(   lKeyValueStr    ) +"  >>>> >>>>>>>>>>>>>  File   Write Z Data.   " +str(   lKeyValueStr    )     +"     " )
			lKeyTime  = pCurve.KeyGetTime(lCount)
			lKeyTimeStr=lKeyTime.GetTimeString(lTimeString)
			DebugLog(" 947  DisplayCurveKeys      lKeyTimeStr   =  "+str(   lKeyTimeStr    )   )
			
			lOutputString = ""
			"""
			#FbxProperty
			#lKeyValueStr=pProperty.GetEnumValue(lKeyValue)
						Key Time: "
			#lOutputString += lKeyTime.GetTimeString(lTimeString)
			lOutputString += str(lKeyTimeStr)
			lOutputString += ".... Key Value: "
			lOutputString += str(lKeyValueStr)
			lOutputString += " [ "
			"""
			pCurve_KeyGetInterpolation__lCount=pCurve.KeyGetInterpolation(lCount)
			DebugLog(" 1086  DisplayCurveKeys      pCurve_KeyGetInterpolation__lCount   =  "+str(   pCurve_KeyGetInterpolation__lCount    )   )

			InterpolationFlagToIndex_____pCurve_KeyGetInterpolation__lCount_=self.InterpolationFlagToIndex(pCurve_KeyGetInterpolation__lCount)
			DebugLog(" 1090  DisplayCurveKeys      InterpolationFlagToIndex_____pCurve_KeyGetInterpolation__lCount_   =  "+str(   InterpolationFlagToIndex_____pCurve_KeyGetInterpolation__lCount_    )   )
			
			interpolation_List__InterpolationFlagToIndex_____pCurve_KeyGetInterpolation__lCount_ =interpolation[InterpolationFlagToIndex_____pCurve_KeyGetInterpolation__lCount_ ] 
			DebugLog(" 1093  DisplayCurveKeys      interpolation_List__InterpolationFlagToIndex_____pCurve_KeyGetInterpolation__lCount_   =  "+str(   interpolation_List__InterpolationFlagToIndex_____pCurve_KeyGetInterpolation__lCount_    )   )
			

			#interpolationStr=str(  interpolation[InterpolationFlagToIndex_____pCurve_KeyGetInterpolation__lCount_ ]  )
			#interpolationStr=str(  interpolation[ InterpolationFlagToIndex(pCurve.KeyGetInterpolation(lCount)) ]  )
			#lOutputString += interpolationStr
		
			#DebugLog(" 1100  DisplayCurveKeys      interpolationStr   =  "+str(   interpolationStr    )   )
			#pGettedCurveHandle=pCurve.GetCurveHandle(lCount)
			#DebugLog("562  pGettedCurveHandle  = "+str(pGettedCurveHandle)  )
		
			#if (pCurve.KeyGetInterpolation(lCount)&KFCURVE_INTERPOLATION_CONSTANT) == KFCURVE_INTERPOLATION_CONSTANT:
			#	lOutputString += " | "
			#	lOutputString += constantMode[ ConstantmodeFlagToIndex(pCurve.KeyGetConstantMode(lCount)) ]
			#elif (pCurve.KeyGetInterpolation(lCount)&KFCURVE_INTERPOLATION_CUBIC) == KFCURVE_INTERPOLATION_CUBIC:
			#	lOutputString += " | "
			#	lOutputString += cubicMode[ TangeantmodeFlagToIndex(pCurve.KeyGetTangeantMode(lCount)) ]
			#	lOutputString += " | "
			#	lOutputString += tangentWVMode[ TangeantweightFlagToIndex(pCurve.KeyGetTangeantWeightMode(lCount)) ]
			#	lOutputString += " | "
			#	lOutputString += tangentWVMode[ TangeantVelocityFlagToIndex(pCurve.KeyGetTangeantVelocityMode(lCount)) ]
			
			#lOutputString += " ]"
			#DebugLog(lOutputString)
		DebugLog("1117       END                >>>>>>>>>>>>>>>>>>>>>>>>>>>>DisplayCurveKeys(pCurve= "+str(pCurve)+")")
	
	def DisplayCurve_00100_KeysEdit_(self,pCurve,pNode):
		DebugLog("942                              >>>>>>>>>>>>>>>>>>>>>>>>>>>>DisplayCurveKeys(pCurve= "+str(pCurve)+")")
		interpolation = [ "?", "constant", "linear", "cubic"]
		constantMode =  [ "?", "Standard", "Next" ]
		cubicMode =	[ "?", "Auto", "Auto break", "Tcb", "User", "Break", "User break" ]
		tangentWVMode = [ "?", "None", "Right", "Next left" ]

		lKeyCount = pCurve.KeyGetCount()
		DebugLog(" 578  DisplayCurve_00100_KeysEdit_       lKeyCount=    ___ " +str(lKeyCount)+" _____")
	
		for lCount in range(lKeyCount):
			lTimeString = ""
			lKeyValue = pCurve.KeyGetValue(lCount)
			lKeyValueStr=str(lKeyValue)
			lKeyTime  = pCurve.KeyGetTime(lCount)
			lKeyTimeStr=lKeyTime.GetTimeString(lTimeString)
			#FbxProperty
			#lKeyValueStr=pProperty.GetEnumValue(lKeyValue)
			lOutputString = "			Key Time: "
			#lOutputString += lKeyTime.GetTimeString(lTimeString)
			lOutputString += str(lKeyTimeStr)
			lOutputString += ".... Key Value: "
			lOutputString += str(lKeyValueStr)
			lOutputString += " [ "
			lOutputString += interpolation[ InterpolationFlagToIndex(pCurve.KeyGetInterpolation(lCount)) ]
		
		
			KeyValue=pCurve.KeyGetValue(lCount)
			DebugLog("KeyValue= "+str(KeyValue))
			OldlKeyValue=KeyValue
			DebugLog("OldlKeyValue= "+str(OldlKeyValue))
		
		
			FbxAnimUtilities_Instance = FbxAnimUtilities()  # Class  export  instance.
			#FbxAnimUtilities_Instance_Class_Method_List=FbxAnimUtilities_Instance.dir()
			FbxAnimUtilities_Instance_Class_Method_List=inspect.getmembers(FbxAnimUtilities_Instance)
			FbxAnimUtilities_Instance_Class_Method_List_long=len(FbxAnimUtilities_Instance_Class_Method_List)
			DebugLog("    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   FbxAnimUtilities_Instance_Class_Method_List_long    ="+  str(FbxAnimUtilities_Instance_Class_Method_List_long)+"        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			for classInt in range(0, FbxAnimUtilities_Instance_Class_Method_List_long):
				classmember=FbxAnimUtilities_Instance_Class_Method_List[ classInt]
				DebugLog("    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   FbxAnimUtilities_Instance_   __ "+str(classInt)+" _    classmember   ="+  str(classmember)+"        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			
			
			
			FbxAnimCurve_Instance = pCurve  # Class  export  instance.
			#FbxAnimUtilities_Instance_Class_Method_List=FbxAnimUtilities_Instance.dir()
			FbxAnimCurve_Instance_Class_Method_List=inspect.getmembers(FbxAnimCurve_Instance)
			FbxAnimCurve_Instance_Class_Method_List_long=len(FbxAnimCurve_Instance_Class_Method_List)
			DebugLog("    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   FbxAnimCurve_Instance_Class_Method_List_long    ="+  str(FbxAnimCurve_Instance_Class_Method_List_long)+"        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			for classInt in range(0, FbxAnimCurve_Instance_Class_Method_List_long):
				classmember=FbxAnimCurve_Instance_Class_Method_List[ classInt]
				DebugLog("    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   FbxAnimCurve_Instance_  __ "+str(classInt)+" _    classmember   ="+  str(classmember)+"        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			#FbxAnimUtilities_Instance_Class_Method_List
			#FbxAnimUtilities_Instance.SetValue (newSetValue, lCount)
		
			DebugLog("KeyValue= "+str(KeyValue))
			newSetValue=KeyValue*-1
			DebugLog("newSetValue= "+str(newSetValue)+"--------------------")
			#FbxAnimCurve.KeySetValue(int, float): argument 1 has unexpected type 'NoneType' <type 'exceptions.TypeError'> # 
			DebugLog("lCount= "+str(lCount)+"--------------------")
			DebugLog("newSetValue= "+str(newSetValue)+"--------------------")
			pCurve.KeySetValue (lCount,newSetValue)
		
		
		
			DebugLog("       pCurve.SetValue     end")
			KeyValue=pCurve.KeyGetTime(lCount)
			DebugLog("KeyValue= "+str(KeyValue))
		
			#if (pCurve.KeyGetInterpolation(lCount)&KFCURVE_INTERPOLATION_CONSTANT) == KFCURVE_INTERPOLATION_CONSTANT:
			#	lOutputString += " | "
			#	lOutputString += constantMode[ ConstantmodeFlagToIndex(pCurve.KeyGetConstantMode(lCount)) ]
			#elif (pCurve.KeyGetInterpolation(lCount)&KFCURVE_INTERPOLATION_CUBIC) == KFCURVE_INTERPOLATION_CUBIC:
			#	lOutputString += " | "
			#	lOutputString += cubicMode[ TangeantmodeFlagToIndex(pCurve.KeyGetTangeantMode(lCount)) ]
			#	lOutputString += " | "
			#	lOutputString += tangentWVMode[ TangeantweightFlagToIndex(pCurve.KeyGetTangeantWeightMode(lCount)) ]
			#	lOutputString += " | "
			#	lOutputString += tangentWVMode[ TangeantVelocityFlagToIndex(pCurve.KeyGetTangeantVelocityMode(lCount)) ]
			
			lOutputString += " ]"
			DebugLog(lOutputString)






















		#//////////////////////////////////////////////////////////////////////////////////////////////////
		#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
		#//////////////////////////////////////////////////////////////////////////////////////////////////		
	def getClassName(self):
		print( u"className= " + self.__class__.__name__)
		return self.__class__.__name__
#==================================================================================================
#================================  Code Start ==================================================
#====================================================================================================
Instance = GetKeyCurve00110()  # Class  export  instance.
print(" GetKeyCurve00110 Class  __name__="+__name__)

Debug_Instance=DebugLogger00110.DebugLogger00100()
def DebugLogStart():
	#print("DebugStr = "+ DebugStr)
	Debug_Instance.DebugLogStart()
	
def DebugLog(DebugStr):
	print("DebugStr = "+ DebugStr)
	Debug_Instance.DebugLog(" 72 Logger >>>>>>>>"+DebugStr);
	


#//////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////	
def StartMainLine(Instance):
	print("StartMainLine")
	
#//////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////// Class Unit Test /////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////	

if(__name__ == Instance.getClassName()):
	print (u"=============Simple Single Class Unit Test Start====Instance.getClassName() =  "+Instance.getClassName()+" =====")
	#StartMainLine(Instance)
elif(__name__ == "GetKeyCurve00110"):
	print (u"=============Simple Single Class Unit Test Start===== StartMainLine =====")
	StartMainLine(Instance)	
	#Instance.loadFile(FBX_FILE_PATH_AND_NAME_AND_EXT)
elif(__name__ == "__main__"):
	print (u"=============Simple Single Class Unit Test Start===== __main__ =====")
	StartMainLine(Instance)
else:
	print (u"__name__!=self.__class__.__name__  Othor File Import")
	
