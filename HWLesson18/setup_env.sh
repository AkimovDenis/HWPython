# Напишите скрипт, который будет создавать виртуальное окружение и 
# устанавливать туда библиотеку python-docx

echo "Создаем виртуальное окружение..."
python -m venv my_env

echo "Активируем виртуальное окружение..."
source my_env/bin/activate

echo "Устанавливаем библиотеку python-docx..."
pip install python-docx

echo "Библиотека python-docx успешно установлена в виртуальное окружение 'my_env'."
