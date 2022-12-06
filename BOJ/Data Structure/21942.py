n, duration, fine_per_minute = input().split()
n, fine_per_minute = map(int, [n, fine_per_minute])
base_day, base_time = duration.split("/")
base_day = int(base_day)
base_hour, base_minute = map(int, base_time.split(":"))

rental_book = {}
day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
answer = {}

for _ in range(n):
    calendar, time, item, userid = input().split()
    year, month, day = map(int, calendar.split("-"))
    hour, minute = map(int, time.split(":"))
    item = item.upper()

    minute_from_zero = (sum(day_of_month[:month]) + day - 1) * 24 * 60 + hour * 60 + minute
    if item + userid in rental_book:
        rental_time = minute_from_zero - rental_book[item + userid]
        over_time = rental_time - (base_day * 24 * 60 + base_hour * 60 + base_minute)
        if over_time > 0:
            answer[userid] = answer.get(userid, 0) + over_time * fine_per_minute
        rental_book.pop(item + userid)
    else:
        rental_book[item + userid] = minute_from_zero

if not answer:
    print(-1)
else:
    for key, val in sorted(answer.items()):
        print(key, val)
