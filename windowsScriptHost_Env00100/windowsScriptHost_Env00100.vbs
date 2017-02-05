'*********************************************************
' Purpose:配列 UserList 内で指定したユーザーに最初に
'          該当するユーザーを検索します。
' Inputs: strUserList():検索対象のユーザーのリスト。
'         strTargetUser:検索するユーザーの名前。
' Returns:配列 strUserList 内で strTargetUser に最初に
'          該当したユーザーのインデックス番号。
'          該当するユーザーが見つからない場合は、-1 を返します。
'*********************************************************
Function intFindUser (strUserList(), strTargetUser)
WScript.Echo("ネットワーク ドライブ割り当て :");
Dim i   ' ループ カウンタ
   Dim blnFound   ' 対象が見つかったかどうかを示すフラグ
   intFindUser = -1
   i = 0   ' ループ カウンタを初期化します。
   Do While i <= Ubound(strUserList) and Not blnFound
      If strUserList(i) = strTargetUser Then 
         blnFound = True   ' フラグに True を設定します。
         intFindUser = i   ' ループ カウンタに戻り値を設定します。
      End If
      i = i + 1   ' ループ カウンタの値に 1 を加算します。
   Loop
End Function