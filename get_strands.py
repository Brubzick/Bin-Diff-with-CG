from vex_norm import TypeNorm

def HandleIR(stmt_str):
    defS = set()
    refS = set()

    stmt_str = stmt_str.replace(',', ' ')
    stmt_str = stmt_str.replace('(', ' ')
    stmt_str = stmt_str.replace(')', ' ')

    stmt_str_list = stmt_str.split()
    l = len(stmt_str_list)
    
    if ((stmt_str_list[0][0] == 't') & (stmt_str_list[1] == '=')):
        defS.add(stmt_str_list[0])

        for i in range(2, l):
            if stmt_str_list[i][0] == 't':
                refS.add(stmt_str_list[i])

    else:
        for i in range(0, l):
            if stmt_str_list[i][0] == 't':
                refS.add(stmt_str_list[i]) 
    
    return (defS, refS)


def GetStrands(statements):
    strands = []

    l = len(statements)

    for i in range(l-1, -1, -1):
        stmt = statements[i]
        stmt_str = str(stmt)
        strand = []

        refS = HandleIR(stmt_str)[1]
        if (len(refS) != 0):
            strand.append(stmt)

            for j in range(i-1, -1, -1):
                stmtT = statements[j]
                stmt_str_T = str(stmtT)
                defT, refT = HandleIR(stmt_str_T)

                if (refS.intersection(defT)):
                    strand.append(stmtT)
                    refS = refS.union(refT)

            strand.reverse()
            strands.append(strand)

    strands.reverse()
    return strands

def GetAllStrandsNorm(blockList):
    strandsNorm = []

    for block in blockList:
        strands = GetStrands(block)

        for i in range(0, len(strands)):
            for j in range(0, len(strands[i])):
                strands[i][j] = TypeNorm(strands[i][j])
        
        strandsNorm.extend(strands)

    return strandsNorm