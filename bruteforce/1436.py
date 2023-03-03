n = int(input())

version = 0
now = 665
while version < n:
    version += 1
    found_666 = False
    while not found_666:
        now += 1
        if str(now).__contains__("666"):
            found_666 = True

print(now)