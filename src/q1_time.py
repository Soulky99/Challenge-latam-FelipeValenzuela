from typing import List, Tuple
from datetime import datetime
from collections import defaultdict
import json


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    users = defaultdict(lambda: defaultdict(int))
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            date = datetime.fromisoformat(tweet['date']).date()
            user = tweet['user']
            username = user['username']
            users[date][username] += 1
    top_date = sorted(users.keys(),key=lambda x: sum(users[x].values()),reverse=True)[:10]

    results = []

    for date in top_date:
        top_username = max(users[date], key=users[date].get)
        results.append((date,top_username))
        
    return results