import pyvex

def GGEliminate(block):
    i = 0

    while (i < len(block)):
        stmt = block[i]
        delIndex = []

        if stmt.tag == 'Ist_WrTmp':
            if stmt.data.tag == 'Iex_Get':
                regOffset = stmt.data.offset
                wrTmp = pyvex.expr.RdTmp.get_instance(stmt.tmp)   

                for j in range(i+1, len(block)):
                    subStmt = block[j]
                    if subStmt.tag == 'Ist_WrTmp':
                        subWrTmp = pyvex.expr.RdTmp.get_instance(subStmt.tmp)
                        if subStmt.data.tag == 'Iex_Get':
                            if subWrTmp == wrTmp:
                                if regOffset == subStmt.data.offset:
                                    if (j not in delIndex):
                                        delIndex.append(j)
                                else:
                                    if (i not in delIndex):
                                        delIndex.append(i)
                                    break 

                            # 只有offset相同的情况
                            else:
                                if regOffset == subStmt.data.offset:
                                    if (j not in delIndex):
                                        delIndex.append(j)

                                    for k in range(j+1, len(block)):
                                        subSubStmt = block[k]
                                        if subSubStmt.tag == 'Ist_WrTmp':
                                            subSubWrTmp = pyvex.expr.RdTmp.get_instance(subSubStmt.tmp)
                                            if subSubWrTmp == subWrTmp:
                                                break
                                            else:
                                                if subSubStmt.data.tag == 'Iex_RdTmp':
                                                    if subSubStmt.data == subWrTmp:
                                                        block[k].data = wrTmp
                                                elif subSubStmt.data.tag == 'Iex_Load':
                                                    if subSubStmt.data.addr == subWrTmp:
                                                        block[k].data.addr = wrTmp
                                                # 去除了Iex_CCall，因为大多时候无更改
                                                elif ((subSubStmt.data.tag == 'Iex_Unop') | (subSubStmt.data.tag == 'Iex_Binop') | (subSubStmt.data.tag == 'Iex_Triop') | (subSubStmt.data.tag == 'Iex_Qop')):
                                                    args = subSubStmt.data.args
                                                    for l in range(0, len(args)):
                                                        if args[l] == subWrTmp:
                                                            block[k].data.args[l] = wrTmp
                                        
                                        elif subSubStmt.tag == 'Ist_Store':
                                            if subSubStmt.data == subWrTmp:
                                                block[k].data = wrTmp
                                            if subSubStmt.addr == subWrTmp:
                                                block[k].addr = wrTmp

                                        elif subSubStmt.tag == 'Ist_Exit':
                                            if subSubStmt.guard == subWrTmp:
                                                block[k].guard = wrTmp

                        else:
                            if (str(wrTmp) in str(subStmt.data)): break
                    else:
                        if (str(wrTmp) in str(subStmt)): break

        delIndex.sort(reverse=True)
        for index in delIndex:
            del block[index]
        
        i += (1 - len(delIndex))
    
    return block

