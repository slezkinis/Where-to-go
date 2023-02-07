# Where-to-go
 
Сайт, на котором показаны достопремичательности Москвы.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```powershell
pip install -r requirements.txt
```

### Как запустить
Перед запуском сайта нужно создать базу данных и применить к ней миграции. Это можно сделать командой:
```powershell
python3 manage.py migrate
```

Теперь можно запустить код с помощью команды:
```powershell
python3 managr.py runserver
```

### Использование админ панели

Для начала, нужно создать аккаунт суперпользователя. Это можно сделать командой:
```powershell
python3 manage.py createsuperuser
```
Теперь можно перейти по ссылке `/admin` и войти под логином и паролем, который Вы указали при регистрации.

### Настройка переменных окружений

Чтобы настроить переменные окружения нужно создать файл с названием `.env` и настраивать. Вот какие есть переменные окружения:
1. `ALLOWED_HOSTS` - домены, под которыми можно запускать сайт. По умолчанию: `['127.0.0.1', '.pythonanywhere.com']`.
2. `SECRET_KEY` - секретный ключ приложения. По умолчанию созданный Django ключ.
3. `DEBUG` - режим отладки. По умолчанию: `True`.
Вот пример файла `.env`:
```
DEBUG=True
ALLOWED_HOSTS=[]
SECRET_KEY='REPLACE_ME'
```


### Загрузка данных в базу данных

Для загрузки данных в базу данных можно использовать команду:
```powershell
python3 manage.py load_place https://ссылка_на_json_файл
```
Вот пример, как должен выглядить json файл:
```
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения.Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```
### Сайт

Как выглядит сайт можно посмотреть по [по ссылке](https://peachivan.pythonanywhere.com/)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
