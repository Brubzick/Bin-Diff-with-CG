import pyvex

def RmCopy(block):
    delIndex = []

    for i in range(0, len(block)):
        stmt = block[i]

        if stmt.tag == 'Ist_WrTmp':
            if stmt.data.tag == 'Iex_RdTmp':
                wrTmp = pyvex.expr.RdTmp.get_instance(stmt.tmp)
                refTmp = stmt.data
                delIndex.append(i)
                
                for j in range(i+1, len(block)):
                    subStmt = block[j]

                    if subStmt.tag == 'Ist_WrTmp':
                        subWrTmp = pyvex.expr.RdTmp.get_instance(subStmt.tmp)
                        if subWrTmp == wrTmp:
                            break
                        else:
                            if subStmt.data.tag == 'Iex_RdTmp':
                                if subStmt.data == wrTmp:
                                    block[j].data = refTmp
                            elif subStmt.data.tag == 'Iex_Load':
                                if subStmt.data.addr == wrTmp:
                                    block[j].data.addr = refTmp
                            # 去除了Iex_CCall，因为大多时候无更改
                            elif ((subStmt.data.tag == 'Iex_Unop') | (subStmt.data.tag == 'Iex_Binop') | (subStmt.data.tag == 'Iex_Triop') | (subStmt.data.tag == 'Iex_Qop')):
                                args = subStmt.data.args
                                for k in range(0, len(args)):
                                    if args[k] == wrTmp:
                                        block[j].data.args[k] = refTmp

                    elif subStmt.tag == 'Ist_Store':
                        if subStmt.data == wrTmp:
                            block[j].data = refTmp
                        if subStmt.addr == wrTmp:
                            block[j].addr = refTmp

                    elif subStmt.tag == 'Ist_Exit':
                        if subStmt.guard == wrTmp:
                            block[j].guard = refTmp
    
    delIndex.sort(reverse=True)
    for index in delIndex:
        del block[index]

    return block
