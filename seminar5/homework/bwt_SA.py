# BWT and suffix array
x = "ATATATTAG"
x += "$"
shifts = [x]
for i in range(1, len(x)):
    previous = shifts[i - 1]
    new = previous[1:] + previous[0]
    shifts.append(new)

sorted_shifts = sorted(shifts)
bwt = "".join([shift[-1] for shift in sorted_shifts])
suffix_array = [len(shift) - shift.index("$") for shift in sorted_shifts]
print(bwt)
print(suffix_array)
