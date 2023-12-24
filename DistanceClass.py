class Distance():
    def __init__(self, 
        l_ir_a_a, l_ir_a_b, l_ir_b_a, l_ir_b_b,
        c_ir_a_a, c_ir_a_b, c_ir_b_a, c_ir_b_b,
        r_ir_a_a, r_ir_a_b, r_ir_b_a, r_ir_b_b):
        #intializing all the left sensor coefficients
        self.l_ir_a_a = l_ir_a_a
        self.l_ir_a_b = l_ir_a_b
        self.l_ir_b_a = l_ir_b_a
        self.l_ir_b_b = l_ir_b_b
        #intializing all the center sensor coefficients
        self.c_ir_a_a = c_ir_a_a
        self.c_ir_a_b = c_ir_a_b
        self.c_ir_b_a = c_ir_b_a
        self.c_ir_b_b = c_ir_b_b
        #intializing all the right sensor coefficients
        self.r_ir_a_a = r_ir_a_a
        self.r_ir_a_b = r_ir_a_b
        self.r_ir_b_a = r_ir_b_a
        self.r_ir_b_b = r_ir_b_b

    def calcdist(self, IR_object):
        IR_object.scan()
        #calculates and print the distances from the ir values
        dist_lir_a = IR_object.lir_a *  self.l_ir_a_a + self.l_ir_a_b 
        dist_lir_b = IR_object.lir_b *  self.l_ir_b_a + self.l_ir_b_b
        dist_cir_a = IR_object.cir_a *  self.c_ir_a_a + self.c_ir_a_b 
        dist_cir_b = IR_object.cir_b *  self.c_ir_b_a + self.c_ir_b_b 
        dist_rir_a = IR_object.rir_a *  self.r_ir_a_a + self.r_ir_a_b 
        dist_rir_b = IR_object.rir_b *  self.r_ir_b_a + self.r_ir_b_b 
        print(
        "dist_lir_a:", dist_lir_a, "\t", "dist_lir_b:", dist_lir_b, "\t",
        "dist_cir_a:", dist_cir_a, "\t", "dist_cir_b:", dist_cir_b, "\t",
        "dist_rir_a:", dist_rir_a, "\t", "dist_rir_b:", dist_rir_b)
    
    def getdist(self, IR_object):
        #returns the distance values calculated from the ir values
        dist_lir_a = IR_object.lir_a *  self.l_ir_a_a + self.l_ir_a_b 
        dist_lir_b = IR_object.lir_b *  self.l_ir_b_a + self.l_ir_b_b
        dist_cir_a = IR_object.cir_a *  self.c_ir_a_a + self.c_ir_a_b 
        dist_cir_b = IR_object.cir_b *  self.c_ir_b_a + self.c_ir_b_b 
        dist_rir_a = IR_object.rir_a *  self.r_ir_a_a + self.r_ir_a_b 
        dist_rir_b = IR_object.rir_b *  self.r_ir_b_a + self.r_ir_b_b 
        return dist_lir_a, dist_lir_b, dist_cir_a, dist_cir_b, dist_rir_a, dist_rir_b
