::@echo off
::@echo on
::set BatchFileDirPath=%~dp0
::echo %BatchFileDirPath%
::Cドライブ直下フォルダに
::cd \
::mklink python.exe mayapy.exe
::set make_symbolic_link_file_path = python.exe
::echo %make_symbolic_link_file_path%
::set link_for = %BatchFileDirPath%python.exe
::echo %link_for%

::mklink %make_symbolic_link_file_path% %link_for%
mklink python.exe C:\Python27\Scripts\python.exe
::閉じない
cmd /k