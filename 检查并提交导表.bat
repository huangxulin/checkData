@echo off

::检查成功后的调用
set callForSuccess=call.bat

echo 开始检查导表...
echo.
echo.

python src/main.py 

if %errorlevel%==0 (
  echo 全部导表检查正常，开始提交...
  call %callForSuccess%
  echo 提交成功
) else (
  echo 导表检查有错误，提交中断！！！
)

pause