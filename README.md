# mask-detetcion
## 项目说明
针对当前疫情情况，各大科技公司开始使用科技手段助力防疫。本项目通过yolov3对人脸口罩数据集进行训练，通过该模型可以识别一个人是否带了口罩，如果识别出此人没有佩戴口罩，则语音播报“请佩戴口罩”，如果此人是佩戴了口罩的，那么系统不会有反应。
## 数据集
用来训练的数据集来源于B站UP主：HamlinZheng，非常感谢该UP主的无私奉献～
## 如何使用该项目
链接：https://pan.baidu.com/s/11z6hmBitSHG4TjilDNFJfQ 
提取码：2zvl

将best.pt放入weights文件夹中，创建一个data文件夹将mask.data和mask.name放进去，配置好项目所需的环境之后，在命令行执行

 python detect.py --data-cfg data/mask.data --cfg cfg/yolov3-tiny-mask.cfg --weights weights/best.pt
 便可看到结果。
 
 语音播报的声音是我自己录的，不咋好听，如果想录自己的语音提醒可以直接运行record.py，录下自己的语音
 
 模型我使用的是yolov3-tiny，模型训练结果实际上不算特别好，计划这两天对数据进行增强，优化一下模型。
 ## 如何训练自己的数据集
 想要使用自己的数据集进行重新训练，需要对数据集的格式改成VOC数据集的形式，这个在网上有非常多的教程，我训练的时候参考的是
 https://blog.csdn.net/qq_21578849/article/details/84980298
 大家感兴趣也可以自己训练一下
## 之后的计划
最近买了nano开发板，打算学习一下模型量化、模型压缩，将模型部署到板子上。尝试使用红外摄像头再给项目加上测温的功能，超过37度会报警，这样这个项目会更加丰满一些，这也是我自己的一个学习过程。非常希望能够广交AI学习者，一起交流学习～我的博客：https://blog.csdn.net/weixin_41722370

