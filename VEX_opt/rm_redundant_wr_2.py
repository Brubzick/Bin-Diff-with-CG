# Remove redundant write to the same reg
def RmRedunantR(block): # block is a list of IR stmt
    i = len(block) - 1

    while (i >= 0):
        stmt = block[i]
        delIndexList = []

        if stmt.tag == 'Ist_Put':
            reg = stmt.offset

            for j in range(i-1, -1, -1):
                preStmt = block[j]

                if preStmt.tag == 'Ist_WrTmp':
                    if preStmt.data.tag == 'Iex_Get':
                        if preStmt.data.offset == reg:
                            break
                
                elif preStmt.tag == 'Ist_Put':
                    if preStmt.offset == reg:
                        delIndexList.append(j)

        for index in delIndexList:
            del block[index]
        
        i -= (1 + len(delIndexList))

    return block