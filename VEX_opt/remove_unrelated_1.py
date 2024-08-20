# Remove IMark and AbiHint
def RmUnrelated(block): # block is a list of IR stmt
    i = 0
    while (i < len(block)):
        stmt = block[i]
        if ((stmt.tag == 'Ist_IMark') | (stmt.tag == 'Ist_AbiHint')):
            del block[i]
        else:
            i += 1 
    
    return block