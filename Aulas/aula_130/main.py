from datetime import datetime, time, timedelta

# data = datetime(2019, 4, 20, 10, 53, 20)
# print(data.strftime("%d/%m/%Y %:%M:%S"))

# data = datetime.strptime("20/04/2019", "%d/%m/%Y")
# print(data.timestamp())

# Cria a data com o timestamp
# data = datetime.fromtimestamp(1555729200.0)
# print(data)

# data = datetime.strptime("20/04/1987 20:00:00", "%d/%m/%Y %H:%M:%S")
# data = data + timedelta(seconds=59*60)

# print(data.strftime("%d/%m/%Y %H:%M:%S"))

d1 = datetime.strptime("20/04/1987 20:00:00", "%d/%m/%Y %H:%M:%S")
d2 = datetime.strptime("25/04/1987 22:33:00", "%d/%m/%Y %H:%M:%S")
dif = d2 - d1

print(dif)