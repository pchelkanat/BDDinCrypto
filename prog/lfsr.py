def LFSR(seed, taps, m):
    regs = seed
    out= []

    if len(seed)<taps[len(taps)-1]:
        return "Ошибка: Длина последовательности меньше номера последнего регистра"
    else:
        for i in range(m):
            tapsum = 0
            for tap in taps:
                tapsum += regs[tap-1]
            nextin = tapsum % 2

            out.append(regs[0])
            regs = [nextin]+regs[:-1]
        out=str(out)
        return out

#seed=[1,1,0,0,0,1,0,0,0,1]
#taps=[2,4,5,7]
#m=20
#print(LFSR(seed,taps,m))
#print(LFSR([1,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0], [16,14,13,11], 15))