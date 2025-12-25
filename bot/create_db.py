import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "professions.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS professions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    energy TEXT,
    goal TEXT,
    description TEXT
)
""")

# Очистка таблицы (чтобы не дублировалось при повторном запуске)
cursor.execute("DELETE FROM professions")

# Данные профессий (БЕЗ manual)
professions = [
    # CREATIVE
    ("Frontend-разработчик", "creative", "medium", "freedom",
     "Создаёт интерфейсы сайтов и приложений."),
    ("UX/UI дизайнер", "creative", "low", "creativity",
     "Проектирует удобные и понятные интерфейсы."),
    ("Графический дизайнер", "creative", "low", "creativity",
     "Создаёт визуальные материалы и брендинг."),
    ("3D-моделлер", "creative", "medium", "creativity",
     "Делает 3D-модели для игр и визуализаций."),
    ("Game-дизайнер", "creative", "medium", "freedom",
     "Разрабатывает игровые механики и концепции."),
    ("Motion-дизайнер", "creative", "medium", "creativity",
     "Создаёт анимации и видеоэффекты."),
    ("Видеомонтажёр", "creative", "medium", "freedom",
     "Монтирует видео и клипы."),
    ("Копирайтер", "creative", "low", "freedom",
     "Пишет тексты для сайтов и рекламы."),
    ("SMM-специалист", "creative", "medium", "freedom",
     "Ведёт соцсети и общается с аудиторией."),
    ("Контент-менеджер", "creative", "low", "stability",
     "Управляет контентом на сайтах и платформах."),

    # NUMBERS
    ("Backend-разработчик", "numbers", "medium", "money",
     "Отвечает за серверную логику и базы данных."),
    ("Fullstack-разработчик", "numbers", "high", "money",
     "Работает и с фронтендом, и с бэкендом."),
    ("Аналитик данных", "numbers", "medium", "money",
     "Анализирует данные и строит отчёты."),
    ("Финансовый аналитик", "numbers", "high", "money",
     "Работает с финансовыми показателями."),
    ("QA-тестировщик", "numbers", "low", "stability",
     "Проверяет качество программ."),
    ("DevOps-инженер", "numbers", "high", "money",
     "Автоматизирует деплой и инфраструктуру."),
    ("Data Scientist", "numbers", "high", "money",
     "Работает с большими данными и ML."),
    ("Системный аналитик", "numbers", "medium", "stability",
     "Анализирует требования и процессы."),
    ("Бухгалтер", "numbers", "low", "stability",
     "Ведёт финансовый учёт."),
    ("Экономист", "numbers", "medium", "stability",
     "Анализирует экономические показатели."),

    # PEOPLE
    ("Проектный менеджер", "people", "high", "stability",
     "Организует работу команды."),
    ("Продуктовый менеджер", "people", "high", "money",
     "Отвечает за развитие продукта."),
    ("HR-специалист", "people", "medium", "stability",
     "Работает с персоналом."),
    ("Маркетолог", "people", "high", "money",
     "Продвигает продукты и услуги."),
    ("Бизнес-аналитик", "people", "medium", "money",
     "Анализирует бизнес-процессы."),
    ("Менеджер по продажам", "people", "high", "money",
     "Продаёт товары и услуги."),
    ("Аккаунт-менеджер", "people", "medium", "stability",
     "Работает с клиентами."),
    ("PR-специалист", "people", "medium", "freedom",
     "Отвечает за имидж компании."),
    ("Коуч", "people", "low", "freedom",
     "Помогает людям развиваться."),
    ("Преподаватель онлайн", "people", "medium", "stability",
     "Обучает людей через интернет.")
]

cursor.executemany("""
INSERT INTO professions (name, category, energy, goal, description)
VALUES (?, ?, ?, ?, ?)
""", professions)

conn.commit()
conn.close()

print("✅ База professions.db создана и заполнена")
