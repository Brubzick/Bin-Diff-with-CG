import pyvex

def PGComb(block):
    delIndex = []

    for i in range(0, len(block)):
        stmt = block[i]

        if stmt.tag == 'Ist_Put':
            for j in range(i+1, len(block)):
                subStmt = block[j]
                if subStmt.tag == 'Ist_Put':
                    if subStmt.offset == stmt.offset:
                        break
                elif subStmt.tag == 'Ist_WrTmp':
                    if subStmt == 'Iex_Get':
                        if subStmt.data.offset == stmt.offset:
                            block[j].data = stmt.data
                            if (i not in delIndex):
                                delIndex.append(i)
                    else:
                        wrTmp = pyvex.expr.RdTmp.get_instance(subStmt.tmp)
                        if wrTmp == stmt.data:
                            break
        
    delIndex.sort(reverse=True)
    for index in delIndex:
        del block[index]

    return block