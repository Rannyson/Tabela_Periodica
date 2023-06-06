# TABELA PERIÓDICA
print('{:=^80}'.format(' TABELA PERIÓDICA '))
s = 0
while not s:
    n = int(input('Digite o  número do elemento químico: '))

    # LISTA
    ma = [3,11,19,37,55,87]
    mat = [4,12,20,38,56,88]
    mt = [21,22,23,24,25,26,27,28,29,30,39,40,41,42,43,44,45,46,47,48,72,73,74,75,76,77,78,79,80,104,105,106,107,108,109,110,111,112]
    lan = [57,58,59,60,61,62,63,64,65,66,67,68,69,70,71]
    act = [89,90,91,92,93,94,95,96,97,98,99,100,101,102,103]
    mr = [13,31,49,50,81,82,83,113,114,115,116]
    sm = [5,14,32,33,51,52,84]
    nm = [1,6,7,8,15,16,34]
    ha = [9,17,35,53,85,117]
    gn = [2,10,18,36,54,86,118]

    # 1 A 118:
    # METAL ALCALINO
    if n in ma:
            print('O elemento {} é um metal alcalino e seu nome é  '.format(n),end='')
            if n == 3:
                print('Lítio (Li).')        
            elif n == 11:
                print('Sódio (Na).')
            elif n == 19:
                print('Potássio (K).')
            elif n == 37:
                print('Rubídio (Rb).')
            elif n == 55:
                print('Césio (Cs).')
            elif n == 87:
                print('Frâncio (Fr).')
            print(' ')
    # METAL DE TRANSIÇÃO
    elif n in mt:
        print('O elemento {} é um metal de transição e seu nome é '.format(n),end='')
        if n == 21:
            print('Escândio (Sc).')
        elif n == 22:
            print('Titânio (Ti).')
        elif n == 23:
            print('Vanádio (V).')
        elif n == 24:
            print('Cromo (Cr).')
        elif n == 25:
            print('Manganês (Mn).')
        elif n == 26:
            print('Ferro (Fe).')
        elif n == 27:
            print('Cobalto (Co).')
        elif n == 28:
            print('Níquel (Ni).')
        elif n == 29:
            print('Cobre (Cu).')
        elif n == 30:
            print('Zinco (Zn).')
        elif n == 39:
            print('Ítrio (Y).')
        elif n == 40:
            print('Zircônio (Zr).')
        elif n == 41:
            print('Nióbio (Nb).')
        elif n == 42:
            print('Molibdênio (Mo).')
        elif n == 43:
            print('Tecnécio (Tc).')
        elif n == 44:
            print('Rutênio (Ru)')
        elif n == 45:
            print('Ródio (Rh).')
        elif n == 46:
            print('Paládio (Pd).')
        elif n == 47:
            print('Prata (Ag).')
        elif n == 48:
            print('Cádmio (Cd).')
        elif n == 72:
            print('Háfnio (Hf).')
        elif n == 73:
            print('Tântalo (Ta).')
        elif n == 74:
            print('Tungstênio (W)')
        elif n == 75:
            print('Rênio (Re).')
        elif n == 76:
            print('Osmio (Os).')
        elif n == 77:
            print('Irídio (Ir).')
        elif n == 78:
            print('Platina (Pt).')
        elif n == 79:
            print('Ouro (Au).')
        elif n == 80:
            print('Mercúrio (HG).\nObservação: Em temperatura ambiente o mercúrio se torna líquido e é o único metal que tem forma líquida.')
        elif n == 104:
            print('Rutherfórdio (Rf).\nDESCONHECIDO') 
        elif n == 105:
            print('Dúbnio (Db).\nDESCONHECIDO')
        elif n == 106:
            print('Seabórgio (Sg).\nDESCONHECIDO') 
        elif n == 107:
            print('Bóhrio (Bh).\nDESCONHECIDO')
        elif n == 108:
            print('Hássio (HS).\nDESCONHECIDO')
        elif n == 109:
            print('Meitnério (Mt).\nDESCONHECIDO')
        elif n == 110:
            print('Darmastádio (Ds).\nDESCONHECIDO')
        elif n == 111:
            print('Roenstgênio (Rg).\nDESCONHECIDO')
        elif n == 112:
            print('Copernício (Cn).\nDESCONHECIDO')
        print(' ')
    # LANTANÍDEO
    elif n in lan:
        print('O elemento {} é Lantanídeo e seu nome é '.format(n),end='')
        if n == 57:
            print('Lantânio (La).')
        elif n == 58:
            print('Cério (Ce).')
        elif n == 59:
            print('Praseodímio (Pr).')
        elif n == 60:
            print('Neodímio (Nd).')
        elif n == 61:
            print('Promécio (Pm).\nDESCONHECIDO')
        elif n == 62:
            print('Samário (Sm).')
        elif n == 63:
            print('Európio (Eu).')
        elif n == 64:
            print('Gadolínio (Gd).')
        elif n == 65:
            print('Térbio (Tb).')
        elif n == 66:
            print('Disprósio (Dy).')
        elif n == 67:
            print('Hólmio (Ho).')
        elif n == 68:
            print('Erbio (Er).')
        elif n == 69:
            print('Túlio (Tm).')
        elif n == 70:
            print('Itérbio (Yb).')
        elif n == 71:
            print('Lutécio (Lu).')
        print(' ')
    # ACTINÍDEO
    elif n in act:
        print('O elemento {} é um actinídeo e seu nome é '.format(n),end='')
        if n == 89:
            print('Actínio (Ac).')
        elif n == 90:
            print('Tório (Th).')
        elif n == 91:
            print('Protactínio (Pa).')
        elif n == 92:
            print('Urânio (U).')
        elif n == 93:
            print('Neptúnio (NP).\nDESCONHECIDO')
        elif n == 94:
            print('Plutônio (Pu).\nDESCONHECIDO')
        elif n == 95:
            print('Amerício (Am).\nDESCONHECIDO')
        elif n == 96:
            print('Cúrio (Cm).\nDESCONHECIDO')
        elif n == 97:
            print('Berquélio (Bk).\nDESCONHECIDO')
        elif n == 98:
            print('Califónio (Cf).\nDESCONHECIDO')
        elif n == 99:
            print('Einstênio (Es).\nDESCONHECIDO')
        elif n == 100:
            print('Férmio (Fm).\nDESCONHECIDO')
        elif n == 101:
            print('Mendelévio (Md).\nDESCONHECIDO')
        elif n == 102:
            print('Nobélio (No).\nDESCONHECIDO')
        elif n == 103:
            print('Laurêncio (Lr).\nDESCONHECIDO')
        print(' ')
    # METAL REPRESENTATIVO
    elif n in mr:
        print('O elemento {} é um metal representativo e o seu nome é '.format(n),end='')
        if n == 13:
            print('Alumínio (Al).')
        elif n == 31:
            print('Gálio (Ga).')
        elif n == 49:
            print('Índio (In).')
        elif n == 50:
            print('Estanho (Sn).')
        elif n == 81:
            print('Tálio (Tl.')
        elif n == 82:
            print('Chumbo (Pb).')
        elif n == 83:
            print('Bismuto (Bi)')
        elif n == 113:
            print('Unintrio (Uut).\nDESCONHECIDO')
        elif n == 114:
            print('Fleróvio (Fl).\nDESCONHECIDO')
        elif n == 115:
            print('Ununpntio (Uup).\nDESCONHECIDO')
        elif n == 116:
            print('Livermório (Lv).\nDESCONHECIDO')
        print(' ')
    # SEMI METAL
    elif n in sm:
        print('O elemento {} é um semi metal e seu nome é '.format(n),end='')
        if n == 5:
            print('Boro (B).')
        elif n == 14:
            print('Silício (Si).')
        elif n == 32:
            print('Germânio (Ge)')
        elif n == 33:
            print('Arsênio(As).')
        elif n == 51:
            print('Antimônio (Sb).')
        elif n == 52:
            print('Telúrio (Te).')
        elif n == 84:
            print('Polônio (Po).')
        print(' ')
    # NÃO METAL    
    elif n in  nm:
            print('O elemento {} é um não metal e seu nome é '.format(n),end='')
            if n == 1:
                print('Hidrogênio (H).\nGASOSO.')
            elif n == 6:
                print('Carbono (C).')
            elif n == 7:
                print('Nitrogênio (N).\nGASOSO.')
            elif n == 8:
                print('Oxigênio (O).\nGasoso.')
            elif n == 15:
                print('Fosforo (P).')
            elif n == 16:
                print('Enxofre (S).')
            elif n == 32:
                print('Selênio (Se).')
            print(' ')
    # HALOGÊNIO
    elif n in ha:
            print('O elemento {} é um halogênio e seu nome é '.format(n),end='')
            if n == 9:
                print('Flúor (F).\nGASOSO.')
            elif n == 17:
                print('Cloro (Cl).\nGASOSO.')
            elif n == 35:
                print('Bromo (Br).\nObservação: O Bromo é líquido à temperatura ambiente e apresenta coloração castanho-avermelhada escura.')
            elif n == 53:
                print('Iodo (I).')
            elif n == 85:
                print('Astato (At).')
            elif n == 117:
                print('Ununséptio).\nDESCONHECIDO.')
            print(' ')
    # GASE NOBRE
    elif n in gn:
            print('O elemento {} é um gás nobre e seu nome é '.format(n),end='')
            if n == 2:
                print('Hélio (He).\nGASOSO.')
            elif n == 10:
                print('Neônio (Ne).\nGASOSO.')
            elif n == 18:
                print('Argônio (Ar).\nGASOSO.')
            elif n == 36:
                print('Cripitônio (Kr).\nGASOSO.')
            elif n == 54:
                print('Xenônio (Xe).\nGASOSO.')
            elif n == 86:
                print('Radônio (Rn).\nGASOSO.')
            elif n == 118:
                print('Ununóctio (Uuo).\nDESCONHECIDO.')
            print(' ')
    else:
        print('A tabela periódica contem números de 1 a 118. TENTE NOVAMENTE.')
print(' ')
        
