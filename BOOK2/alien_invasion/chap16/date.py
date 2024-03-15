import datetime
from datetime import datetime 

today = datetime.strptime('2024-03-15','%Y-%m-%d')

print(today ,type(today), type('2024-03-15'))

new = today + datetime.timedelta(days=100)
print(new)