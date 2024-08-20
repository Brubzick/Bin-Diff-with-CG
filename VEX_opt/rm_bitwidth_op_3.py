
bitwidthOp = {'Iop_8Uto16','Iop_8Uto32','Iop_8Uto64','Iop_16Uto32', 'Iop_16Uto64','Iop_32Uto64','Iop_8Sto16', 'Iop_8Sto32','Iop_8Sto64','Iop_16Sto32', 'Iop_16Sto64','Iop_32Sto64',
            'Iop_64to8','Iop_32to8','Iop_64to16','Iop_16to8','Iop_16HIto8','Iop_8HLto16','Iop_32to16','Iop_32HIto16','Iop_16HLto32','Iop_64to32','Iop_64HIto32','Iop_32HLto64',
            'Iop_128to64','Iop_128HIto64','Iop_64HLto128','Iop_Not1','Iop_32to1','Iop_64to1','Iop_1Uto8','Iop_1Uto32','Iop_1Uto64','Iop_1Sto8','Iop_1Sto16','Iop_1Sto32','Iop_1Sto64'}


# Remove bitwidth and endianness operation
def RmBitwidthOp(block):
    for i in range(0, len(block)):
        stmt = block[i]
        if stmt.tag == 'Ist_WrTmp':
            if stmt.data.tag == 'Iex_Unop':
                if (stmt.data.op in bitwidthOp):
                    block[i].data = stmt.data.args[0]
    
    return block