# tbot
my first tg bot 

structure:
recommendation_bot/
│
├── bot/
│   ├── handlers.py        # Telegram-logic
│   ├── keyboards.py
│   └── bot.py
│
├── recommender/
│   ├── model.py           # TF-IDF, similarity     
│   └── cleaning.py     # clean data
│
├── data/
│   └── movies_clean.csv
│
├── config.py
├── requirements.txt
├── README.md
└── main.py
