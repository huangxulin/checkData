@echo off

::���ɹ���ĵ���
set callForSuccess=call.bat

echo ��ʼ��鵼��...
echo.
echo.

python src/main.py 

if %errorlevel%==0 (
  echo ȫ����������������ʼ�ύ...
  call %callForSuccess%
  echo �ύ�ɹ�
) else (
  echo �������д����ύ�жϣ�����
)

pause