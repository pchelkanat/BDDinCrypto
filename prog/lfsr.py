def LFSR(seed, taps, m):
    regs = seed[::-1]
    print(regs)
    out= []

    if len(seed)<taps[len(taps)-1]:
        return "Ошибка: Длина последовательности меньше номера последнего регистра"
    else:
        for i in range(m):
            tapsum = 0
            for tap in taps:
                tapsum += regs[tap-1]
            nextin = tapsum % 2

            out.append(regs[len(regs)-1])
            print(out)
            regs = [nextin]+regs[:-1]
        out=str(out)
        return out

#seed=[1,1,1,0,1,1]
#taps=[2,3]
#m=6
#print(LFSR(seed,taps,m))
#print(LFSR([1,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0], [16,14,13,11], 15))