@echo off

echo 开始检查导表...
echo.
echo.

python src/main.py 

if %errorlevel%==0 (
  echo 全部导表检查正常
) else (
  echo 导表检查不正常，请检查相关导表文档！！！
)

pause