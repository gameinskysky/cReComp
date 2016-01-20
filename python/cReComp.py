#!/usr/bin/python
# -*- coding: utf-8 -*-
# NAME
#         "cReComp.py"
# DESCRIPTION
#         This is a code generator for Reconfigurable Component
# 		  creator Reconfigurable HW componet
# VERSION
#         0.0.3
# LICENCE
#		  new BSD
#
# (c) Kazushi Yamashina
import sys
sys.path.append("lib/")
import check_option
import scrp_conf
import option_port
import common
# 		self.module_name = ""
# 		self.module_type = ""
# 		self.use_fifo_32 = False
# 		self.use_fifo_8 = False
# 		self.option_port = False
# 		self.port_stack = []
# 		self.make_32_alw = False
# 		self.alw32_stack = []
# 		self.make_8_alw = False
# 		self.alw8_stack = []
# 		self.sub_module = False
# 		self.sub_module_name = []
# 		self.assign_target_module = []
# 		self.assign_port_stack = []
# 		self.fi=dsl_file
# 		self.line = 1

if __name__ == "__main__":
	
	argvs = sys.argv
	argc = len(argvs)
	argv0 = ""
	argv1 = ""

	if(argc == 3):
		argv0 = argvs[1]
		argv1 = argvs[2]
	elif (argc == 2):
		argv0 = argvs[1]

	check_option.option(argv0,argv1)

	dsl_file = argv0
	flag = scrp_conf.ConfigFlag(dsl_file)
	flag.check_format(dsl_file)
	flag.set(dsl_file)
	module_name = flag.module_name
	fo = open("devel/%s.v" % module_name,"w")
	module_type = flag.module_type
	if module_type == "normal":
		ans_hs_s = False
		ans_hs_m = False
	elif module_type == "hs_mst":
		ans_hs_m = True
	elif module_type == "hs_slv":
		ans_hs_s = True
	else:
		print "Error! module_type"
		quit()
	
	ans_32 = flag.use_fifo_32
	ans_8 = flag.use_fifo_8
	
	if flag.option_port:
		ans_o = True
	else:
		ans_o = False
	if ans_32:
		ans_32_alw = flag.make_32_alw != False
	if ans_8:
		ans_8_alw = flag.make_8_alw != False
	ans_sub = flag.sub_module

	# define io port
	fo.write("`timescale 1ns / 1ps\n")
	fo.write("//this code was generated by cReComp\n")
	fo.write("module %s("%module_name)
	fo.write ("\ninput [0:0] clk,\n")

	if ans_32 == False and ans_8 == False:
		fo.write("input rst,\n")
	if ans_32:
		common.read_lib(fo,"lib/lib32")
		if ans_8 or ans_o:
			fo.write(",\n")
	if ans_8:
		common.read_lib(fo,"lib/lib8")
		if ans_o:
			fo.write(",\n")
	if ans_hs_s:
		common.read_lib(fo,"lib/hs_slv_port")
		if ans_o:
			fo.write(",\n\n")
	#generate option port
	port_stack = []
	if ans_o:
		port_stack = option_port.make(flag,fo)
	fo.write(");\n")

	# generate instance for top module
	fo.write ("// //copy this instance to top module\n")
	fo.write ("//%s %s(\n"%(module_name,module_name))
	fo.write ("//.clk(bus_clk),\n")
	if ans_32:
		common.read_lib(fo,"lib/lib32inst")
		if ans_8 or ans_o:
			fo.write(",\n//")
	if ans_8:
		common.read_lib(fo,"lib/lib8inst")
	if ans_hs_s:
		common.read_lib(fo,"lib/hs_slv_inst")
	if ans_o:
		if ans_32 or ans_8:
			fo.write("\n")
		else:
			fo.write("// .rst(rst),\n")
		ix = 0
		while ix < len(port_stack):
			inst = str(port_stack[ix]).split(" ")
			fo.write("// .%s(%s)"%(inst[2],inst[2]))
			ix = ix + 1
			if ix < len(port_stack):
				fo.write(",\n")
	fo.write("\n//);\n")

	# define prameter
	if ans_hs_s:
		common.read_lib(fo,"lib/hs_slv_para")
	if ans_32:
		common.read_lib(fo,"lib/fifo_32_para")
	if ans_8:
		common.read_lib(fo,"lib/fifo_8_para")

	# generate register for 32bit FIFO
	