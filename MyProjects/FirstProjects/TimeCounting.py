time_ex = 10000  # seconds

hours = time_ex // 3600
minutes = (time_ex % 3600) // 60
seconds = time_ex % 60

hours = str(hours).rjust(2, "0")
minutes = str(minutes).rjust(2, "0")
seconds = str(seconds).rjust(2, "0")

print("H:M:S")
print(f"{hours}:{minutes}:{seconds}")
