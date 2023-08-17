`timescale 1ns / 1ps
module digital_io(
    input clk,//40M
    input usb_clk_60m,
    input rst_n,//以上为默认定义
    
    input [7:0] io_a_in, //DIO15-DIO8
    output [7:0] io_a_out, 
    output  [7:0] io_a_oe,//1输出out，0输入in
    input [7:0] io_b_in, //DIO7-DIO0
    output  [7:0] io_b_out,
    output  [7:0] io_b_oe
    
//    input uart_rx, -> io_a_in[7]
//    input A1, -> io_a_in[0]
//    input A2, -> io_a_in[1]
//    input A3, -> io_a_in[2]
//    input A4, -> io_a_in[3]
//    output B5-B1 -> out1[4-0]
//    output reg uart_tx, -> io_a_out[6]
//    output reg fan, -> io_b_out[7]
//    output reg led, -> io_b_out[6]
//    output reg ming -> io_b_out[5]
);
    reg[7:0] out1;
    reg[7:0] out2;
    assign io_b_out = out1;
    assign io_a_out = out2;
    assign io_a_oe=8'b01000000;//io_a_out[6]
    assign io_b_oe=8'b11111111;
    wire  RET;
    reg[3:0]audio;
    reg[7:0]Data;
    reg Send_en;
    reg tx_done;
    reg[7:0] out;
    reg Rx_Done;
    wire Rx_done;
    reg rst;
    reg[7:0]Data_1;
    reg send_en;
    reg [17:0]Bps_DR_1=1000000000/115200/25;
    reg [17:0]div_cnt_1;
    
    
    assign Rx_done = Rx_Done;
    always@(*)begin
    Send_en = send_en;
    end
    
    reg [1:0]Uart_rx_r;
    always@(posedge clk)begin
        Uart_rx_r[0] <= io_a_in[7];
        Uart_rx_r[1] <= Uart_rx_r[0];
    end 
    
    wire Pdege_uart_rx;
    //前一时刻0，新一时刻1，上升沿
    //assign Pdege_uart_rx = ((Uart_rx_r[1] == 0) &&(Uart_rx_r[0] == 1));
    assign Pdege_uart_rx = (Uart_rx_r == 2'b01);
    wire Nedge_uart_rx;
    //assign Pdege_uart_rx = ((Uart_rx_r[1] == 1) &&(Uart_rx_r[0] == 0));
    //前一时刻1，新一时刻0，下降沿
    assign Nedge_uart_rx = (Uart_rx_r == 2'b10);
    //设波特率为9600；1000000000/9600/16/20=325
    //设波特率为115200；1000000000/115200/16/20=27
    reg [8:0] Bps_DR = 1000000000/115200/16/25 - 1;



    wire Bps_clk_16x;
    assign Bps_clk_16x = (div_cnt == Bps_DR / 2);
    
    reg RX_EN;
    always@(posedge clk)
    if(Nedge_uart_rx)
        RX_EN <= 1;
    else if(Rx_Done || (sta_bit >= 4))
        RX_EN <= 0;
    
    
    reg [8:0]div_cnt;
    always@(posedge clk)
    if (RX_EN)begin
        if(div_cnt == Bps_DR)
            div_cnt <= 0;
        else
            div_cnt <= div_cnt + 1'b1;
    end
    else 
        div_cnt <= 0;
    
    reg [7:0]Bps_cnt;
    always@(posedge clk)
    if(RX_EN) begin
        if(Bps_clk_16x)begin 
            if(Bps_cnt == 160)//160
                Bps_cnt <= 0;
            else
                Bps_cnt <= Bps_cnt + 1'b1;
        end
        else
            Bps_cnt <= Bps_cnt;
    end
    else
        Bps_cnt <= 0;      
            
    //3位，因为16取7次，加起来最多为7（3'b111）
    //reg width name number     1+8+1
    reg[2:0]sta_bit;
    reg[2:0]r_data[7:0];
    reg[2:0]sto_bit;
    
    always@(posedge clk)
    if(Bps_clk_16x)begin
        case(Bps_cnt)
            0:begin
                sta_bit <= 0;
                sto_bit <= 0;
                r_data[0] <= 0;
                r_data[1] <= 0;
                r_data[2] <= 0;
                r_data[3] <= 0;
                r_data[4] <= 0;
                r_data[5] <= 0;
                r_data[6] <= 0;
                r_data[7] <= 0;
              end
            5,6,7,8,9,10,11:sta_bit <= sta_bit + io_a_in[7];
            21,22,23,24,25,26,27: r_data[0] <= r_data[0] + io_a_in[7];
            37,38,39,40,41,42,43: r_data[1] <= r_data[1] + io_a_in[7];
            53,54,55,56,57,58,59: r_data[2] <= r_data[2] + io_a_in[7];
            69,70,71,72,73,74,75: r_data[3] <= r_data[3] + io_a_in[7];
            85,86,87,88,89,90,91: r_data[4] <= r_data[4] + io_a_in[7];
            101,102,103,104,105,106,107: r_data[5] <= r_data[5] + io_a_in[7];
            117,118,119,120,121,122,123: r_data[6] <= r_data[6] + io_a_in[7];
            133,134,135,136,137,138,139: r_data[7] <= r_data[7] + io_a_in[7];
            149,150,151,152,153,154,155: sto_bit <= sto_bit + io_a_in[7];
            default:;
        endcase
    end
    
    always@(posedge clk)
    if(Bps_clk_16x  && (Bps_cnt == 159))begin
        Data[0] <= (r_data[0] >= 4)? 1'b1:1'b0;
        Data[1] <= (r_data[1] >= 4)? 1'b1:1'b0;
        Data[2] <= (r_data[2] >= 4)? 1'b1:1'b0;
        Data[3] <= (r_data[3] >= 4)? 1'b1:1'b0;
        Data[4] <= (r_data[4] >= 4)? 1'b1:1'b0;
        Data[5] <= (r_data[5] >= 4)? 1'b1:1'b0;
        Data[6] <= (r_data[6] >= 4)? 1'b1:1'b0;
        Data[7] <= (r_data[7] >= 4)? 1'b1:1'b0;
    end
    
    always@(posedge clk)
    //else if(Bps_clk_16x && (Bps_cnt == 159))
    //else if(div_cnt == Bps_DR/2 && (Bps_cnt == 159))
    if((div_cnt == Bps_DR/2) && (Bps_cnt == 160))
        begin Rx_Done <= 1; end
    else
        Rx_Done <= 0;
        
always@(posedge Rx_done)begin 
    case(Data)
        8'b00000000:begin
        case({io_a_in[0],io_a_in[1],io_a_in[2],io_a_in[3]})
        4'b0000: out = 8'b0000_0001;
        4'b0001: out = 8'b0000_0010;
        4'b0010: out = 8'b0000_0100;
        4'b0011: out = 8'b0000_1000;
        4'b0100: out = 8'b0001_0000;
        4'b0101: out = 8'b0010_0000;
        4'b0110: out = 8'b0100_0000;
        4'b0111: out = 8'b1000_0000;
        4'b1000: out = 8'b1000_0001;
        4'b1001: out = 8'b1000_0010;
        4'b1010: out = 8'b1000_0100;
        4'b1011: out = 8'b1000_1000;
        4'b1100: out = 8'b1001_0000;
        4'b1101: out = 8'b1010_0000;
        4'b1110: out = 8'b1100_0000;
        4'b1111: out = 8'b1100_0001;
            endcase
            Data_1 = out;
                 send_en <= 1;
        end
        8'b11110000:begin out1[4:0] = Data[4:0];end
        8'b11111000:begin out1[4:0] = Data[4:0];end
        8'b11110100:begin out1[4:0] = Data[4:0];end
        8'b11111100:begin out1[4:0] = Data[4:0];end
        8'b11110010:begin out1[4:0] = Data[4:0];end
        8'b11111010:begin out1[4:0] = Data[4:0];end
        8'b11110110:begin out1[4:0] = Data[4:0];end
        8'b11111110:begin out1[4:0] = Data[4:0];end
        8'b11111001:begin out1[4:0] = Data[4:0];end
        8'b11110001:begin out1[4:0] = Data[4:0];end
        
                        
        8'b10000100:begin out1[5] = 0;end//ming
        8'b10001000:begin out1[6] = 0;end//led
        8'b10000010:begin out1[7] = 0;end//fan
        8'b10000101:begin out1[5] = 1;end
        8'b10001001:begin out1[6] = 1;end
        8'b10000011:begin out1[7] = 1;end
        8'b00010001:begin Data_1 = Data;
                          send_en <= 1;
                          end
        8'b11111111:begin Data_1 = Data;
                          send_en <= 1;
                          end
            endcase
end


always@(posedge clk)begin
    audio = {io_a_in[0],io_a_in[1],io_a_in[2],io_a_in[3]};
end

//assign RET = (audio != {io_a_in[0],io_a_in[1],io_a_in[2],io_a_in[3]});

//always@(posedge RET)begin
    
//    end


    //发送使能  
    always@(posedge clk)begin
    case(send_en)
    1:begin
        if(div_cnt_1 == Bps_DR_1 -1)
            div_cnt_1 <=0;
        else 
            div_cnt_1 <= div_cnt_1 + 1'b1;
    end
    0:begin div_cnt_1 <=0;end
    endcase
    end
    
        
    //发送数据的计数
    reg [3:0]bps_cnt__1;
    always@(posedge clk)begin
    case(send_en)
    1:begin
        if(div_cnt_1 == 1)begin
            if(bps_cnt__1 == 12)
                bps_cnt__1 <=0;
            else 
                bps_cnt__1 <= bps_cnt__1 + 1'b1;           
        end
    end
    0:begin bps_cnt__1 <= 0;end
    endcase
    end
    //发送数据
    always@(posedge clk)
    begin
    
        case(bps_cnt__1)
            1:begin out2[6] <= 0;tx_done <=1'b0;end
            2:out2[6] <= Data_1[0];
            3:out2[6] <= Data_1[1];
            4:out2[6] <= Data_1[2];
            5:out2[6] <= Data_1[3];
            6:out2[6] <= Data_1[4];
            7:out2[6] <= Data_1[5];
            8:out2[6] <= Data_1[6];
            9:out2[6] <= Data_1[7];
            10:out2[6] <=1;
            11:begin out2[6] <= 1;tx_done <= 1'b1;
//            send_en <= 1'b0;
            end
            default:out2[6] <= 1;
        endcase
     end


always@(*)begin
    Data_1 = Data_1;
end



 initial begin
    RX_EN <= 0;
    div_cnt <= 0;
    Bps_cnt <= 0;
    sta_bit <= 0;
    sto_bit <= 0;
    r_data[0] <= 0;
    r_data[1] <= 0;
    r_data[2] <= 0;
    r_data[3] <= 0;
    r_data[4] <= 0;
    r_data[5] <= 0;
    r_data[6] <= 0;
    r_data[7] <= 0;
    Data <= 0;
    Rx_Done <= 0;
    out2[6] <= 1;
    send_en <= 0;
 end


endmodule
