# tbot
my first tg bot 

structure:
recommendation_bot/
│
├── bot/
│   ├── handlers.py        # Telegram-логика
│   ├── keyboards.py
│   └── bot.py
│
├── recommender/
│   ├── model.py           # TF-IDF + similarity
│   ├── preprocess.py     # очистка данных
│   └── data_loader.py
│
├── data/
│   └── movies.csv
│
├── config.py
├── requirements.txt
├── README.md
└── main.py
