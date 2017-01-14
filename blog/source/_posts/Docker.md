title: "Docker学习笔记"
date: 2017-01-14 05-15-00
tags:
---

docker太帅了，这就是未来。虚拟化肯定是没什么前途的，随着windows和unix的衰败，虚拟化的用途已经很有限，在一个linux独霸天下的时代里，容器就是标准答案。 容器技术才标志着云计算时代的真正到来，而虚拟化技术最重要的意义是为容器趟一下这条路。
“虚拟机的本质是模拟，通过模拟物理机上的硬件，向用户提供资源。容器的基石是经过隔离与限制的Linux进程。容器提供的是性能损失更小的原生物理机的计算能力，容器之间唯一共享的是Linux内核。“
”性能和稳定性是最致命的：规模大之后，遇到很多第概率但是实实在在发生了性能与稳定性问题：如mac表满导致无法网络通信、UDP大报文阻塞、丢包、中断异常、系统slab集中回收性内存申请锁住时间过长。很快我们意识到原来做容器其实是在做Linux Kernel，一切性能和稳定性问题都回归到最根本的点--Linux Kernel。” ----京东容器集群建设之路
docker的意义在于：1，隔离机器与应用，其实是机器与应用之间的适配层。这将有史以来第一次将application与compter进行分离。docker内部属于application，docker外部属于computer，两者是不同的。从来都是application依附于computer的架构，今后将会发生彻底的改变。docker是一项并不高深、并不晦涩、并不复杂、也没有多少实质内容的技术，但它处的位置将赋予它划时代的意义。2，容器是操作系统进一步发展的完善，之前已经具备了多进程、多用户、多终端能力、但缺乏隔离虚拟环境的能力，docker的意义将是多进程、多用户、多终端意义的延续。3, 基于第一条，衍生出了两个效用，第一个是云计算时代的真正到来，因为app与computer解除耦合，包含app的docker可以运行在任意机器上，也就是说，它只需要一次封装，便具备了在整个互联网上随意迁移的能力。第二个是解决了版本冲突的问题，不同的应用依赖于不同版本库的冲突，从此成为历史。4,在lib日益庞大的情况下，docker起到了对lib封装整合的效果，lib将沿着细分与整合两条路线往前推进。

firefox放docker里面，运行参数docker run -i -t -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY image_name，出现cannot open display: unix:0.0，然后$ xhost local:root 加一个权限就好了 [link](https://github.com/jessfraz/dockerfiles/issues/6) ![Error message](/img/Docker/Docker_GUI_Firefox.jpg)
