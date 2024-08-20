import pyvex

def ConstFloding(block):
    delIndex = []

    for i in range(0, len(block)):
        stmt = block[i]

        if stmt.tag == 'Ist_WrTmp':
            if stmt.data.tag == 'Iex_Const':
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
                            if subStmt.data.tag == 'Iex_Load':
                                if subStmt.data.addr == wrTmp:
                                    block[j].data.addr = refTmp
                            elif ((stmt.data.tag == 'Iex_Unop') | (stmt.data.tag == 'Iex_Binop') | (stmt.data.tag == 'Iex_Triop') | (stmt.data.tag == 'Iex_Qop') | (stmt.data.tag == 'Iex_CCall')):
                                args = subStmt.data.args
                                for k in range(0, len(args)):
                                    if args[k] == wrTmp:
                                        block[j].data.args[k] = refTmp

                    elif subStmt.tag == 'Ist_Store':
                        if subStmt.data == wrTmp:
                            block[j].data = refTmp
                        if subStmt.addr == wrTmp:
                            block[j].addr = refTmp

                    elif stmt.tag == 'Ist_Exit':
                        if subStmt.guard == wrTmp:
                            block[j].guard = refTmp

    delIndex.sort(reverse=True)
    for index in delIndex:
        del block[index]

    return block


