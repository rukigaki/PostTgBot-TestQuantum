Склонируйте репозиторий локально себе на компьютер в виртуальное окружение 

bash:
git clone https://github.com/rukigaki/PostTgBot-TestQuantum.git

python -m venv venv

source .venv/bin/activate #UNIX-подобные системы

.venv\Scripts\activate #Windows


Запустите deamon БД PostgreSQL

В телеграмме с помощью бота BotFather (адрес в тг: @BotFather) создайте бота, оттуда необходимо будет взять его token

Далее в корне проекта создайте файл .env со следующими параметрами 





DB_HOST=localhost

DB_PORT=Порт, на котором у вас прослушивается postgresql(скорее всего 5432)

DB_USER=Ваш юзернейм

DB_PASS=Пароль от вашей бд

DB_NAME=Ваша бд, в которой будет создаваться модель Post ( см. /PostTgBot(TestQuantum) /app/models.py)

API_TOKEN=Ваш Token для Бота Телеграм(см. BotFather @BotFather)






Установите зависимости в проекте из файла requirements.txt

pip install -r requirements.txt


Создайте конфигурация запуска для файла run.py, который находистя в корне проекта.

############
Проверяющий, заходит на http://localhost:8000/docs - Swagger UI для того, чтобы подергать endpoints на Создание/Удаление/Обновление данных
Endpoints должны также синхронизироваться с Telegram Ботом, по команде /posts вы увидите message с inline кнопками, к каждой из которых привязан соответствующий callback
текст на кнопках соответствует колонке title из модели Post(SqlAlchemy), а вывод соответствует полям content и created_at. Для валидации использовались Pydantic схемы


My Telegram: @rukigaki
email: rukigaki@gmail.com

 



