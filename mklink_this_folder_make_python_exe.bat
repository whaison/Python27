set BatchFileDirPath=%~dp0

::mklink python.exe mayapy.exe
set make_symbolic_link_file_path = %BatchFileDirPath%python.exe
set link_for = python.exe
mklink %make_symbolic_link_file_path% %link_for%
::閉じない
cmd /k