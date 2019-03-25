# Docker命令总结

```docker create``` 创建一个容器，但不启动它。

```docker rename``` 重命名容器。

```docker run``` 在一次操作中创建并启动容器。

```docker rm``` 删除容器。
[docker update]（https://docs.docker.com/engine/reference/commandline/update/）更新容器的资源限制。

通常，如果你运行一个没有选项的容器，它会立即启动和停止，如果你想让它保持运行你可以使用命令docker run -td container_id这将使用将分配伪TTY的选项-t会话和-d将自动分离容器（在后台和打印容器ID中运行容器）。
如果你想要一个瞬态容器，docker run --rm将在它停止后删除容器。
如果要将主机上的目录映射到docker容器，docker run -v $ HOSTDIR：$ DOCKERDIR。另请参阅[Volumes]（https://github.com/wsargent/docker-cheat-sheet/#volumes）。
如果要删除与容器关联的卷，则删除容器必须包含``v开关，如docker rm -v`。
还有一个[日志驱动程序]（https://docs.docker.com/engine/admin/logging/overview/）可用于docker 1.10中的各个容器。要使用自定义日志驱动程序（即syslog）运行docker，请使用docker run --log-driver = syslog。
另一个有用的选项是docker run --name yourname docker_image，因为当你在run命令中指定--name时，这将允许你通过使用你在创建它时指定的名称调用容器来启动和停止容器。 。
开始和停止

[docker start]（https://docs.docker.com/engine/reference/commandline/start）启动一个容器，使其运行。
[docker stop]（https://docs.docker.com/engine/reference/commandline/stop）停止正在运行的容器。
[docker restart]（https://docs.docker.com/engine/reference/commandline/restart）停止并启动容器。
[docker pause]（https://docs.docker.com/engine/reference/commandline/pause/）暂停正在运行的容器，将其“冻结”到位。
[docker unpause]（https://docs.docker.com/engine/reference/commandline/unpause/）将取消暂停正在运行的容器。
[docker wait]（https://docs.docker.com/engine/reference/commandline/wait）阻塞，直到运行容器停止。
[docker kill]（https://docs.docker.com/engine/reference/commandline/kill）将SIGKILL发送到正在运行的容器。
[docker attach]（https://docs.docker.com/engine/reference/commandline/attach）将连接到正在运行的容器。

作者：iOSDevLog
链接：https://www.jianshu.com/p/0ab62a339218
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。


查找镜像
docker search <image>
--automated=false
--no-trunc=false
-s, --stars=0显示star数>=n的镜像, n=0,1,2,3,4....

获取镜像
docker pull <image> 
比如
docker search nginx
docker pull nginx
docker run nginx

默认的注册服务器registry是registry.hub.docker.com
docker pull nginx相当于docker pull registry.hub.docker.com/nginx:latest
也可以用其他的registry

列出本机上的所有镜像
docker images

repository:tag 来定义不同的镜像
比如ubuntu:16.04
如果不输入tag默认:latest

运行镜像，并执行/bin/bash命令
docker run -t -i ubuntu:15.10 /bin/bash 

给镜像打标签
docker tag dl.dockerpool.com:5000/ubuntu:latest ubuntu:latest

镜像详细信息
docker inspect <image id>  打印json格式信息
docker inspect -f {{".Architecture"}} training/webapp

删除镜像
docker rmi image [image...]
docker rmi dl.dockerpool.com:5000/ubuntu
image可以是镜像或标签，当有多个标签时，删除标签不会影响镜像。但是只有1个标签时，镜像也会被删除。
如果有依赖于镜像的容器在系统中时无法删除镜像，可以用-f强制删除，但不推荐，应该先删除所有容器。


docker build -t yeefea/centos:6.7 .
-t ：指定要创建的目标镜像名
. ：Dockerfile 文件所在目录，可以指定Dockerfile 的绝对路径

为镜像添加一个新的标签
docker tag 
docker tag 860c279d2fec yeefea/centos:dev


保存镜像
docker save
-o

载入镜像
docker load
--input

上传镜像
docker push



Docker容器使用

创建
docker create -it ubuntu:latest
docker start ...

运行hello world
docker run hello-world

在容器内运行应用程序
docker run ubuntu:16.04 echo "hello world"

运行交互式的容器
docker run -i -t ubuntu:16.04 /bin/bash
-t:在新容器内指定一个伪终端或终端。
-i:允许你对容器内的标准输入 (STDIN) 进行交互。


启动容器（后台模式）
docker run -d ubuntu:16.04 /bin/sh -c "while true; do echo hello world; sleep 5; done"

查询正在运行的容器
docker ps

查询最后一次创建的容器
docker ps -l 

查询种终止状态的容器
docker ps -a -q

docker logs <container>

docker stop <container>
-t, --time=10

docker kill

输入docker查看所有命令和参数
输入docker <command> --help查看命令详细介绍

Web App
docker pull training/webapp

docker run -d -P training/webapp python app.py
-d:让容器在后台运行。
-P:将容器内部使用的网络端口(Flask默认5000)映射到外部的主机上外部端口(随机)。

docker run -d -p 80:5000 training/webapp python app.py
-p 80:5000把外部的80端口映射到内部的5000端口上，让浏览器能访问


docker logs -f <container>
不加-f会一次性打出到目前为止的所有log然后结束。
-f: 让 docker logs 像使用 tail -f 一样来输出容器内部的标准输出。会持续更新。


docker top <container>
查看容器内部运行的进程

docker inspect <container>
查看 Docker 的底层信息。它会返回一个 JSON 文件记录着 Docker 容器的配置和状态信息。

docker stop <container>停止
docker start <cotainer> 启动已经停止的容器
docker restart <container>重启正在运行中的容器
docker rm <container>删除容器
docker container ls 列出所有镜像
docker container prune 删除所有停止的镜像


进入容器
docker attach <container_id> 不方便，退出困难
docker exec -ti <container_id> /bin/


容器迁移
docker export导出容器
docker import导入容器



容器连接

docker run -d -P training/webapp python app.py
-P :是容器内部端口随机映射到主机的高端口。
-p <port_outer>:<port_inner> 是容器内部端口绑定到指定的主机端口。
-p <ip_address>:<port_outer>:<port_inner> 绑定ip 端口
-p <ip_address>:<port_outer>:<port_inner>/udp 绑定udp端口

查看端口绑定情况
docker port <container_id> 5000

容器命名
docker run -d -P --name runoob training/webapp python app.py

