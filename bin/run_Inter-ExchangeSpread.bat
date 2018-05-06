rem 1、先将下面PYTHONPATH的路径改为你本机上wequantstrategy_sample路径，如 PYTHONPATH=E:\wequantstrategy_sample
rem 2、将Python3.5的路径改为你本机路径，就是python.exe 所在路径如C:\Python\Python35

@set PYTHONPATH=D:\python\d_anaylse
@set PythonDirectory=C:\Users\WangZW\AppData\Local\Programs\Python\Python36-32

cd %PYTHONPATH%
%PythonDirectory%\python.exe app.py


pause