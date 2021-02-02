def needleman_wunsch(seq1, seq2):
    m, n = len(seq1), len(seq2)
    S, arrows = [], []
    for i in range(m + 1):
        S.append([0] * (n + 1))
        arrows.append([0] * (n + 1))
    
    for i in range(m + 1):
        S[i][0] = -i * 10
        arrows[i][0] = "top"
    for j in range(n + 1):
        S[0][j] = -j * 10
        arrows[0][j] = "left"

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            score_left = S[i][j - 1] - 10
            score_top = S[i - 1][j] - 10
            score_diag = S[i - 1][j - 1] + (5 if seq1[i - 1] == seq2[j - 1] else -4)
            if score_left >= score_top and score_left >= score_diag:
                S[i][j] = score_left
                arrows[i][j] = "left"
            elif score_top >= score_left and score_top >= score_diag:
                S[i][j] = score_top
                arrows[i][j] = "top"
            else:
                S[i][j] = score_diag
                arrows[i][j] = "diag"
    
    aln1, aln2 = "", ""
    i, j = m, n
    while i > 0 and j > 0:
        if arrows[i][j] == "diag":
            aln1 += seq1[i - 1]
            aln2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif arrows[i][j] == "left":
            aln1 += "-"
            aln2 += seq2[j - 1]
            j -= 1
        else:
            aln1 += seq1[i - 1]
            aln2 += "-"
            i -= 1

    aln1 = aln1[::-1]
    aln2 = aln2[::-1]
    print(aln1)
    print(aln2)
    print("Score = {}".format(S[-1][-1]))


needleman_wunsch("ATGAGTCTCT", "CTGTCTCCTG")
