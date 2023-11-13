ms = 1000123

msperhour = 3600000
msperminute = 600000
mspersecond = 1000
hours = int(ms / msperhour)
ms = ms - (hours * msperhour)
minutes = int(ms / msperminute)
ms = ms - (minutes * msperminute)
seconds = int(ms / mspersecond)
ms = ms - (seconds * mspersecond)

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
print("Milliseconds:", ms)
