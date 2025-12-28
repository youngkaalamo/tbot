import csv
import pandas as pd
from config import DATA_PATH_OLD
# Чистим данные, очень грязный csv, при запуске бота не используется,
# этот файл запускается для создания датасета один раз
clean_data = []
with open(DATA_PATH_OLD, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        title = row.get("title")
        description = row.get("summary")
        if not title:
            continue
        clean_data.append({
            "title": title.strip(),
            "description": description.strip() if description else ""
        })

df = pd.DataFrame(clean_data)
CLEAN_PATH = "data/movies_clean.csv"
df.to_csv(CLEAN_PATH, index=False, encoding="utf-8")
