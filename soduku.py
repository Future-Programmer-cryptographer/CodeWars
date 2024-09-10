num = [1,2,3,4,5,6,7,8,9]

sodukuGrid = []
for row in range(0,9):
    row = [] 
    for col in range(0,9):
        row.append(num[:])
sodukuGrid.append(row)

# inputGrid = [
#     [None, 7 None, None, None, 5, 4, None, None]
# ]

print(sodukuGrid) 