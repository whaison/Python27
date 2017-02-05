Option Explicit
'WScript.Echo "WSHの実行ファイル名：" & WScript.Name & vbCrLf & _
 '            "実行ファイルのあるフォルダ・パス：" & WScript.Path & vbCrLf & _
 '            "実行ファイルのフルパス：" & WScript.FullName & vbCrLf & _
 '            "バージョン：" & WScript.Version
'---------------------------
'Windows Script Host
'---------------------------
'WSHの実行ファイル名：Windows Script Host

'実行ファイルのあるフォルダ・パス：C:\Windows\System32

'実行ファイルのフルパス：C:\Windows\System32\WScript.exe

'バージョン：5.812
'---------------------------
'OK   
'--------------------------
If False Then
  ' 実行したくない処理      VBScriptは複数行を一度にコメントアウトできない
  xx
  yy
End If
'-----------------------------Print("Hello  Windows Script Host")
'WScript.Echo "Hello  Windows Script Host"
'WScript.Echo "こんにちは　！　ウィンドウズ　スクリプト　ホストさん"
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
       Set objFile = objFSO.OpenTextFile("ShowWSHInfo_sift_jis_00100___Log.txt", 2, True)
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
DebugLog("debug_txt")
DebugLog("debug_txt2")
DebugLog("debug_txt3")
