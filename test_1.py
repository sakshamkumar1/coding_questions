arr = [12, 2, 6, 7, 11]

k = arr[0]
occ = arr[1:]
ways = 0
seats = list(range(1, k+1))
count = 0
if k - len(occ) == 1:
    ways = 0
else:
    for ele in occ:
        seats.remove(ele)
    for i in range(len(seats)-1):
        for j in range(i+1, len(seats)):
            lower_seat = seats[i]
            higher_seat = seats[j]
            if lower_seat % 2 == 1:
                if higher_seat == lower_seat + 1 or higher_seat == lower_seat + 2:
                    count += 1
            elif lower_seat % 2 == 0:
                if higher_seat == lower_seat + 2:
                    count += 1


print(count)
