total_minutes = int(input("Enter the number of minutes to convert: "))

hours = total_minutes // 60
minutes = total_minutes % 60

if minutes == 1:
    minute_word = "minute"
else:
    minute_word = "minutes"

if hours == 1:
    hour_word = "hour"
else:
    hour_word = "hours"

if total_minutes ==1:
    total_words = "minute"
else:
    total_words = "minutes"

print(f"{total_minutes} {total_words} = {hours} {hour_word} and {minutes} {minute_word}.")