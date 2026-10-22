// dut.sv — replace with your design. Example: a parameterized counter.
// Coding style: one clocked always_ff for state, always_comb for next-state/outputs.

module dut #(
    parameter int WIDTH = 8
) (
    input  logic             clk,
    input  logic             rst_n,   // active-low synchronous reset
    input  logic             en,
    output logic [WIDTH-1:0] count,
    output logic             wrap     // high for one cycle when count rolls over
);

  logic [WIDTH-1:0] count_q, count_d;

  always_comb begin
    count_d = count_q;
    wrap    = 1'b0;
    if (en) begin
      if (count_q == '1) begin
        count_d = '0;
        wrap    = 1'b1;
      end else begin
        count_d = count_q + 1'b1;
      end
    end
  end

  always_ff @(posedge clk) begin
    if (!rst_n) count_q <= '0;
    else        count_q <= count_d;
  end

  assign count = count_q;

endmodule
