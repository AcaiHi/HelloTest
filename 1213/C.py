COLUMNS = 3

def magic():
    lo_shu_square = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]
    for r in lo_shu_square:
        for c in range (COLUMNS):
            if sum(r) == sum (lo_shu_square[c][c] for c in range(COLUMNS)):
                if sum(r)== sum(r[c] for r in lo_shu_square):
                    answer_output = str('a Lo Shu Magic Square')
            else:
                answer_output = str('not a Lo Shu Magic Square')

    print("The inputs are", answer_output)

magic()