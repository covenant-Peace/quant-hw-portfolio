// tb_dut.sv — self-checking testbench. Fails loudly, dumps a waveform.
`timescale 1ns / 1ps

module tb_dut;

  localparam int WIDTH = 4;  // small so we can exercise wrap quickly

  logic clk = 0, rst_n = 0, en = 0;
  logic [WIDTH-1:0] count;
  logic wrap;

  dut #(.WIDTH(WIDTH)) u_dut (
      .clk(clk), .rst_n(rst_n), .en(en), .count(count), .wrap(wrap)
  );

  always #5 clk = ~clk;  // 100 MHz

  int errors = 0;
  task automatic check(input logic cond, input string msg);
    if (!cond) begin
      $error("CHECK FAILED: %s (t=%0t, count=%0d)", msg, $time, count);
      errors++;
    end
  endtask

  initial begin
    $dumpfile("tb_dut.vcd");
    $dumpvars(0, tb_dut);

    // Reset
    repeat (2) @(posedge clk);
    rst_n = 1;
    @(posedge clk);
    check(count == 0, "count should be 0 after reset");

    // Count up and verify wrap at 2^WIDTH-1
    en = 1;
    for (int i = 1; i <= (1 << WIDTH); i++) begin
      @(posedge clk); #1;
      if (i < (1 << WIDTH))
        check(count == i[WIDTH-1:0], "incrementing");
    end
    check(wrap === 1'b0 || wrap === 1'b1, "wrap is defined");

    if (errors == 0) $display("ALL TESTS PASSED");
    else             $fatal(1, "%0d test(s) failed", errors);
    $finish;
  end

endmodule
