import math

DATABASE = {
  "Ваня": "Москва",
  "Денис": "Краснодар",
  "Вова": "Сочи",
  "Андрей": "Питер",
  "Влад": "Москва"
}

def format_friends(friends_count):
  if friends_count == 1:
    return "У тебя один друг"
  elif friends_count >= 2 and friends_count <= 4:
    return f"У тебя {friends_count} друга"
  elif friends_count > 4:
    return f"У тебя {friends_count} друзей"

def process_query(query):
  if query == "кто все мои друзья?":
    friends = ", ".join(DATABASE.keys())
    return f"Твои друзья: {friends}"
  elif query.split(" из")[0] == "корень":
    return math.sqrt(int(query.split("из ")[1]))
  elif query == "где все мои друзья?":
    city = ", ".join(set(DATABASE.values()))
    return f"Твои друзья в городах: {city}"
  elif query == "сколько у меня друзей?":
    count = len(DATABASE)
    return f"{format_friends (count)}!"
  else:
    return "<Неизвестный запрос>"

def check_query(query):
  a = query.split(",")
  if a[0] == "Алиса":
    return process_query(a[1].strip(" "))
  else:
    return "Запрос к кому-то еще"

queries = [
  "Алиса, сколько у меня друзей?",
  "Алиса, какой сегодня день недели?",
  "Алиса, кто все мои друзья?",
  "Алиса, корень из 4",
  "Алиса, корень из 25"
]

def runner(queries):
  for q in queries:
    print(check_query(q))

runner(queries)
