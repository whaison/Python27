Option Explicit
'WScript.Echo "WSH�̎��s�t�@�C�����F" & WScript.Name & vbCrLf & _
 '            "���s�t�@�C���̂���t�H���_�E�p�X�F" & WScript.Path & vbCrLf & _
 '            "���s�t�@�C���̃t���p�X�F" & WScript.FullName & vbCrLf & _
 '            "�o�[�W�����F" & WScript.Version
'---------------------------
'Windows Script Host
'---------------------------
'WSH�̎��s�t�@�C�����FWindows Script Host

'���s�t�@�C���̂���t�H���_�E�p�X�FC:\Windows\System32

'���s�t�@�C���̃t���p�X�FC:\Windows\System32\WScript.exe

'�o�[�W�����F5.812
'---------------------------
'OK   
'--------------------------
If False Then
  ' ���s�������Ȃ�����      VBScript�͕����s����x�ɃR�����g�A�E�g�ł��Ȃ�
  xx
  yy
End If
'-----------------------------Print("Hello  Windows Script Host")
'WScript.Echo "Hello  Windows Script Host"
'WScript.Echo "����ɂ��́@�I�@�E�B���h�E�Y�@�X�N���v�g�@�z�X�g����"
'---------------------------------------------------------------

'-------------------------------------[�t�@�C���ɉ��s�t���Ńf�[�^����������]------http://www.whitire.com/vbs/tips0067.html
On Error Resume Next

'--------------------------------------------------------------
Dim DebugLog___Data
Function DebugLog(strData)
   Dim objFSO      ' FileSystemObject
   Dim objFile     ' �t�@�C���������ݗp

   Set objFSO = WScript.CreateObject("Scripting.FileSystemObject")
   If Err.Number = 0 Then
       Set objFile = objFSO.OpenTextFile("ShowWSHInfo_sift_jis_00100___Log.txt", 2, True)
       If Err.Number = 0 Then
           'objFile.WriteLine("Hello VBScript World     123")
		   DebugLog___Data=DebugLog___Data + strData + vbCrLf
		   objFile.WriteLine(DebugLog___Data)
           objFile.Close
       Else
           WScript.Echo "�t�@�C���I�[�v���G���[: " & Err.Description
       End If
   Else
       WScript.Echo "�G���[: " & Err.Description
   End If
End Function
DebugLog("debug_txt")
DebugLog("debug_txt2")
DebugLog("debug_txt3")
