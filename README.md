recommendation_bot/
│
├── bot/
│   ├── handlers.py        # Telegram-логика
│   ├── keyboards.py
│   └── bot.py
│
├── recommender/
│   ├── model.py           # TF-IDF, косинусное сходство     
│   └── cleaning.py     # подготовка датасета
│
├── data/
│   └── movies_clean.csv # очищенный датасет
│
├── config.py
├── requirements.txt
├── README.md
└── main.py
Датасет может быть любым csv файлом с колонками name, description. 
Развернуть на своем компьютере:

git clone https://github.com/youngkaalamo/tbot.git
cd tbot
python -m venv venv # не обязательно, но рекомендуется виртуальное окружение
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
setx BOT_TOKEN "ВАШ_ТОКЕН"   # Windows
export BOT_TOKEN="ВАШ_ТОКЕН" # Linux / macOS
python main.py

/start - приветствие и меню
/help - справка
/recommend <название> - рекомендации по фильму
/random - случайный фильм

