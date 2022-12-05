import os

# just build some directories and placeholder files for daily puzzles
for i in np.arange(1,26):
    day = f'd{str(i).zfill(2)}'
    if not os.path.exists(day):
        os.makedirs(day, exist_ok=True)
        os.system(f'touch {day}/{day}.py')
        os.system(f'touch {day}/{day}_test.txt')
        os.system(f'touch {day}/{day}.txt')