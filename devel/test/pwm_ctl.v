`timescale 1ns / 1ps
// pwm_ctl.v ver 1.0
// Kazushi Yamashina
// kazushi@virgo.is.utsunomiya-u.ac.jp
// 
// para_in <= 0 ~ 32767
//  -Interval of asserting "en_out" will change 
//          depending on the value of the "para_in".
//  -The more you increase the value the interval will increase.
// 
// dir_in <= 1: positive rotate, 0: negative rotate

module pwm_ctl(
input clk,
input rst,
input [14:0] para_in,
input [0:0] dir_in,
output [0:0] dir_out,
output [0:0] en_out
);

// //copy this instance to top module
//pwm_ctl pwm_ctl
//(
//.clk(bus_clk),
// .rst(rst),
// .para_in(para_in),
// .direction(direction),
// .enable(enable)
//);
reg dir;
reg en;
reg [14:0] in_;
reg [31:0] counter;
wire [31:0] divflag;
reg [31:0] PWMctl_clk;

initial PWMctl_clk = 19999;

assign divflag = PWMctl_clk - in_;

assign dir_out = dir;
assign en_out = en;

always @(posedge clk)begin
	if(rst)
		in_ <= 19999;
	else if(0 < para_in && para_in < PWMctl_clk)
		in_ <= para_in;
	else
		in_ <= 19999;
end

always @(posedge clk)begin
		if(rst)begin
			dir <= 0;
			en <= 0;
		end
		else if(divflag > counter)begin
			dir <= dir_in;
			en <= 1;
		end
		else begin
			en <= 0;
		end
	end

always @(posedge clk)begin
		if(rst)begin
			counter <= 0;
		end
		else if(PWMctl_clk == counter)
			counter <= 0;
		else
			counter <= counter + 1;
	end

endmodule