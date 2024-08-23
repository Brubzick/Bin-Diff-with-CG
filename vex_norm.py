# 把VEX IR语句依据类型标准化
def TypeNorm(stmt):
    stmt_str = str(stmt)
    tag = stmt.tag

    if tag == 'Ist_Put':
        if stmt.data.tag == 'Iex_Const':
            norm = 'Put_con'
        else:
            norm = 'Ist_Put' 

    elif tag == 'Ist_PutI':
        stmt_str_list = stmt_str.split()
        for i in range(0, len(stmt_str_list)):
            if stmt_str_list[i] == '=':
                tmp = stmt_str_list[i+1]
                break
        if tmp[0:2] == '0x':
            norm = 'PutIcons'
        else:
            norm = 'IstPutI'  
    
    elif tag == 'Ist_WrTmp':
        exType = stmt.data.tag
        if ((exType == 'Iex_Unop')or(exType == 'Iex_Binop')or(exType == 'Iex_Triop')or(exType == 'Iex_Qop')):
            op = str(stmt.data.op)
            for i in range(len(op)-1,-1,-1):
                if (not op[i:].isdigit()):
                    break
            norm = op[:i+1]
        else:
            norm = stmt.data.tag
    
    elif tag == 'Ist_Store':
        if stmt.data.tag == 'Iex_Const':
            norm = 'STl_con'
        else:
            norm = 'Ist_STl' 
    
    else:
        norm = tag
        
    return norm


