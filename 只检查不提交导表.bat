@echo off

echo ��ʼ��鵼��...
echo.
echo.

python src/main.py 

if %errorlevel%==0 (
  echo ȫ������������
) else (
  echo �����鲻������������ص����ĵ�������
)

pause