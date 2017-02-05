Option Explicit
'---------------------------
'Windows Script Host
'---------------------------
'-----------------------------Print("Hello  Windows Script Host")
'WScript.Echo "Hello  Windows Script Host"
WScript.Echo "こんにちは　！　ウィンドウズ　スクリプト　ホストさん日本語"
'---------------------------------------------------------------
'-------------------------------------[ファイルに改行付きでデータを書き込む]------http://www.whitire.com/vbs/tips0067.html
On Error Resume Next

'--------------------------------------------------------------
Dim DebugLog___Data
Function DebugLog(strData)
   Dim objFSO      ' FileSystemObject
   Dim objFile     ' ファイル書き込み用

   Set objFSO = WScript.CreateObject("Scripting.FileSystemObject")
   If Err.Number = 0 Then
       Set objFile = objFSO.OpenTextFile("ShowWSHInfo_sift_jis_00200____Log.txt", 2, True)
       If Err.Number = 0 Then
           'objFile.WriteLine("Hello VBScript World     123")
		   DebugLog___Data=DebugLog___Data + strData + vbCrLf
		   objFile.WriteLine(DebugLog___Data)
           objFile.Close
       Else
           WScript.Echo "ファイルオープンエラー: " & Err.Description
       End If
   Else
       WScript.Echo "エラー: " & Err.Description
   End If
End Function
DebugLog("debug_txt_1")
DebugLog("debug_txt_2")
DebugLog("debug_txt_3")

DebugLog("WSH exe File Name     =     " + WScript.Name )
DebugLog("WSH exe WScript Full Path  =  "+ WScript.Path)
DebugLog("WSH version   =  "+ WScript.Version)
