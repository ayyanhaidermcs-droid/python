meetings = [[9, 11], [13, 15], [16, 17], [18, 19], [8, 9]]

overlap_meetings = 0

for i in range(len(meetings)):
    for j in range(i + 1, len(meetings)):
        if meetings[i][0] < meetings[j][1] and meetings[j][0] < meetings[i][1]:
            overlap_meetings += 1

print("Total overlaps_meetings today:", overlap_meetings)                                          






