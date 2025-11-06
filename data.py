from datetime import datetime, timedelta
user_input = input("enter a date (YYY-MM-DD):")
today = datetime.strptime(user_input, "%Y-%M-%d").date()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)

print("yesterday:", yesterday)
print("Today:", today)
print("tomorrow:", tomorrow)
~       
