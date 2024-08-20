from VEX_opt.remove_unrelated_1 import RmUnrelated
from VEX_opt.rm_redundant_wr_2 import RmRedunantR
from VEX_opt.rm_bitwidth_op_3 import RmBitwidthOp
from VEX_opt.Put_Get_combine_4 import PGComb
from VEX_opt.rm_copy_5 import RmCopy
from VEX_opt.const_folding_6 import ConstFloding
from VEX_opt.Get_Get_Elimination_7 import GGEliminate
from VEX_opt.Load_Store_Op_8 import LLEliminate, LSEliminate,SSEliminate

def VexOpt(block):
    
    block = RmUnrelated(block)
    block = RmRedunantR(block)
    block = RmBitwidthOp(block)
    block = PGComb(block)
    block = RmCopy(block)
    block = ConstFloding(block)
    block = GGEliminate(block)
    block = LLEliminate(block)
    block = LSEliminate(block)
    block = SSEliminate(block)

    return block