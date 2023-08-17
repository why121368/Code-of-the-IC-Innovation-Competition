//====================================================================================================================//
//使用本转接板分四步调用函数：
//第一步：打开usb
//第二步：配置UART或者SPI或者IIC参数
//第三步：发送或接收数据
//第四步：关闭USB
//====================================================================================================================//
//关于每个函数中UsbIndex参数的说明：
//    1. 如果您的电脑上只连接了一个转接板，这个参数使用默认值0
//    2. 如果您的电脑上连接了两个或者两个以上设备，这个参数指连接到电脑的第几个转接板，从0开始，最大99
//====================================================================================================================//
//关于函数返回值的说明：
//    所有的函数的返回值都是int型
//    返回值大于等于0都是正确的结果
//    返回值小于0的都是错误的结果
//====================================================================================================================//
#ifndef __USB2UARTSPIIICDLL_H__
#define	__USB2UARTSPIIICDLL_H__

#if defined(_WIN32) || defined(__CYGWIN__) || defined(_WIN32_WCE)
	#ifdef USB2UARTSPIIICDLL_EXPORTS
	#define USB2UARTSPIIICDLL_API extern "C" __declspec(dllexport)
	#else
	#define USB2UARTSPIIICDLL_API extern "C" __declspec(dllimport)
	#endif
#else
    #define USB2UARTSPIIICDLL_API
	#define __stdcall
#endif



//UART奇偶校验位
#define UART_Parity_No                      0
#define UART_Parity_Odd                     1
#define UART_Parity_Even                    2

//UART停止位
#define UART_StopBits_1                     0
#define UART_StopBits_1_5                   1
#define UART_StopBits_2                     2

//SPI速率
#define SPI_Rate_281K						0
#define SPI_Rate_562K						1
#define SPI_Rate_1_125M						2
#define SPI_Rate_2_25M						3
#define SPI_Rate_4_5M						4
#define SPI_Rate_9M							5
#define SPI_Rate_18M						6
#define SPI_Rate_36M						7

//SPI帧格式
#define SPI_MSB								0
#define SPI_LSB								1

//SPI时钟模式
#define SPI_SubMode_0						0
#define SPI_SubMode_1						1
#define SPI_SubMode_2						2
#define SPI_SubMode_3						3

//IIC速率
#define IIC_Rate_1K							0
#define IIC_Rate_5K							1
#define IIC_Rate_10K						2
#define IIC_Rate_20K						3
#define IIC_Rate_50K						4
#define IIC_Rate_80K						5
#define IIC_Rate_100K						6
#define IIC_Rate_200K						7
#define IIC_Rate_400K						8
#define IIC_Rate_600K						9
#define IIC_Rate_800K						10
#define IIC_Rate_1M							11

//IIC 寻址模式
#define	IIC_ADDRMOD_7BIT					0
#define	IIC_ADDRMOD_10BIT					1

//内建列表功能1
#define	LINE_FUN1_SPI_CS0_0_1		    	0
#define	LINE_FUN1_SPI_CS0_1_0		    	1
#define	LINE_FUN1_SPI_CS0_1_1		    	2
#define	LINE_FUN1_SPI_CS0_0_0		    	3
#define	LINE_FUN1_SPI_CS1_0_1		    	4
#define	LINE_FUN1_SPI_CS1_1_0		    	5
#define	LINE_FUN1_SPI_CS1_1_1		    	6
#define	LINE_FUN1_SPI_CS1_0_0		    	7
#define	LINE_FUN1_SPICS_0    		    	8
#define	LINE_FUN1_SPICS_1    		    	9
#define	LINE_FUN1_IIC_AddStart 		    	10
#define	LINE_FUN1_IIC_NoStart		    	11
#define	LINE_FUN1_IICd_send  		    	12
#define	LINE_FUN1_IICd_read  		    	13
#define	LINE_FUN1_IICr_send  		    	14
#define	LINE_FUN1_IICr_read  		    	15
#define	LINE_FUN1_UART_      		    	16
#define	LINE_FUN1_IO_0       		    	17
#define	LINE_FUN1_IO_1       		    	18
#define	LINE_FUN1_PWM_start  		    	19
#define	LINE_FUN1_PWM_stop   		    	20
#define	LINE_FUN1_ADC_0       		    	21
#define	LINE_FUN1_ADC_1				        22

//内建列表功能2
#define	LINE_FUN2_null						0             
#define	LINE_FUN2_SPI_full					1
#define	LINE_FUN2_SPI_half					2
#define	LINE_FUN2_SPICS_h					3
#define	LINE_FUN2_SPICS_l					4
#define	LINE_FUN2_IIC_AddStop				5
#define	LINE_FUN2_IIC_NoStop				6
#define	LINE_FUN2_IICd_7bit					7
#define	LINE_FUN2_IICd_10bit				8
#define	LINE_FUN2_IICr_7bit					9
#define	LINE_FUN2_IICr_10bit				10
#define	LINE_FUN2_IO_w						11
#define	LINE_FUN2_IO_r						12








//===============================打开和关闭USB的函数,查询设备信息函数============================================================//
USB2UARTSPIIICDLL_API int __stdcall OpenUsb(unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall CloseUsb(unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall IsFirstPowerUp(unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall  GetBoardInformation (unsigned char *UIDBuf,unsigned int *isHsUSB,unsigned int *FwVersion, unsigned int UsbIndex);


//===============================UART相关的函数=================================================================//
USB2UARTSPIIICDLL_API int __stdcall ConfigUARTParam (unsigned int baudRate,unsigned int parity,unsigned int stopBits,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall UARTSendData(unsigned char *sendBuf, unsigned int len,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall UARTRcvData(unsigned char *rcvBuf, unsigned int len,unsigned int UsbIndex);


//===============================SPI主模式相关的函数============================================================//
USB2UARTSPIIICDLL_API int __stdcall ConfigSPIParam(unsigned int rate,unsigned int fistBit,unsigned int subMode,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall SPISetCS0(unsigned char cs,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall SPISetCS1(unsigned char cs,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall SPISendAndRcvData(unsigned char CSshelect,unsigned char startCS, unsigned char endCS, unsigned int CSdelay, unsigned char duplex,unsigned char dummy,
														unsigned char *sendBuf,unsigned char *rcvBuf,unsigned int slen,unsigned int rlen,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall SPISendData(unsigned int startCS, unsigned int endCS,unsigned char *sendBuf, unsigned int len,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall SPIRcvData(unsigned int startCS, unsigned int endCS,unsigned char *rcvBuf, unsigned int len,unsigned int UsbIndex);


//===============================SPI从模式相关的函数============================================================//
USB2UARTSPIIICDLL_API int __stdcall ConfigSPIParamSlave(unsigned int fistBit,unsigned int subMode,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall SPISlavePreloadData(unsigned char *pBuf, unsigned int len,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall SPISlaveRcvData(unsigned char *rcvBuf, unsigned int len,unsigned int UsbIndex);


//===============================I2C主模式相关的函数============================================================//
USB2UARTSPIIICDLL_API int __stdcall ConfigIICParam(unsigned int rate,unsigned int clkSLevel,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall IICSendAndRcvData(unsigned char strartBit,unsigned char stopBit,unsigned char *sendBuf,unsigned char *rcvBuf, unsigned int slen,unsigned int rlen,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall IICSendData(unsigned char strartBit,unsigned char stopBit,unsigned char *sendBuf,unsigned int slen,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall IICRcvData(unsigned char stopBit,unsigned char *rcvBuf,unsigned int rlen,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall IICCheckSlaveAddr(unsigned char addrMod,unsigned int addr,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall IICRegisterSend(unsigned char addrMod,unsigned int addr,unsigned char *regBuf,unsigned char *sendBuf,unsigned char reglen,unsigned int slen,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall IICRegisterRead(unsigned char addrMod,unsigned int addr,unsigned char *regBuf,unsigned char *rcvBuf,unsigned char reglen,unsigned int rlen,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall IICDirectSend(unsigned char addrMod,unsigned int addr,unsigned char *sendBuf,unsigned int slen,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall IICDirectRead(unsigned char addrMod,unsigned int addr,unsigned char *rcvBuf,unsigned int rlen,unsigned int UsbIndex);


//===============================I2C从模式相关的函数============================================================//
USB2UARTSPIIICDLL_API int __stdcall ConfigIICParamSlave(unsigned char addrMod,unsigned int addr,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall IICSlavePreloadData(unsigned char *pBuf, unsigned int len,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall IICSlaveRcvData(unsigned char *rcvBuf, unsigned int len,unsigned int UsbIndex);


//===============================ADC相关的函数==================================================================//
USB2UARTSPIIICDLL_API int __stdcall GetADCVal(unsigned char ch,unsigned int UsbIndex);


//===============================PWM相关的函数==================================================================//
USB2UARTSPIIICDLL_API int __stdcall PWMOut(unsigned int prescaler,unsigned int period,unsigned int pulse,unsigned int PulseNum,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall PWMClose(unsigned int UsbIndex);


//===============================IO口相关的函数=================================================================//
USB2UARTSPIIICDLL_API int __stdcall IOSetAndRead(unsigned int IONum, unsigned int IODir, unsigned int IOBit,unsigned int UsbIndex);


//===============================内建列表相关的函数=============================================================//
USB2UARTSPIIICDLL_API int __stdcall InternalListInitAllLine(unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall InternalListSetLine(unsigned int lineNum,unsigned int listFun1,unsigned int listFun2,
													unsigned int listParama,unsigned char* listParamb,unsigned int listParambLen,
													unsigned char* listSend,unsigned int listSendLen,unsigned int listDelay1,
													unsigned int listRcvLen,unsigned int listDelay2,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall InternalListDisableLine(unsigned int lineNum,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall InternalListTsetOnce(unsigned int *period,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall InternalListIO0Start(unsigned int IOTrigger,unsigned int times,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall InternalListTimerStart(unsigned int period,unsigned int times,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall InternalListReceive(unsigned char *rcvBuf,unsigned int len,unsigned int UsbIndex);
USB2UARTSPIIICDLL_API int __stdcall InternalListStop(unsigned int UsbIndex);





#endif






