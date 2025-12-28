import csv
import pandas as pd
from config import DATA_PATH
# clean_data = []

# with open(DATA_PATH, encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if "title" in row and "description" in row:
#             clean_data.append({
#                 "title": row["title"].strip(),
#                 "description": row["description"].strip()
#             })

# df = pd.DataFrame(clean_data)
# df.to_csv(DATA_PATH, index=False)

# print(df.head())
import csv
import pandas as pd
from config import DATA_PATH

clean_data = []

with open(DATA_PATH, encoding="utf-8") as f:
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

# ⚠️ ВАЖНО: сохраняем в НОВЫЙ файл
CLEAN_PATH = "data/movies_clean.csv"
df.to_csv(CLEAN_PATH, index=False, encoding="utf-8")
