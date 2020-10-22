# 第6章 并发：死锁和饥饿

## 6.1 死锁原理

定义：一组相互竞争系统资源或进行通信的进程间的“永久”阻塞。

联合进程图描述进程和计算机资源，进程进入敏感区域fatal region后死锁将不可避免。

### 6.1.1 可重用资源

资源通常分两类：

* 可重用资源：一次仅供一个进程安全使用，且使用后释放，不会耗尽。比如处理器、I/O通道、内存、外存、设备、文件、数据库、信号量等等
* 可消耗资源：可被创建和销毁的资源，数量通常没有限制，无阻塞生产进程可以创建任意数量的这类资源

死锁例子1：当执行顺序为 p0, p1, q0, q1, p2, q2 时会发生死锁。

处理这类死锁的一个策略：施加关语资源请求顺序的约束

```
进程P
步骤
p0		Request(D)
p1		Lock(D)
p2		Request(T)
p3		Lock(T)
p4		Perform function
p5		Unlock(D)
p6		Unlock(T)

进程Q
步骤
q0		Request(T)
q1		Lock(T)
q2		Request(D)
q3		Lock(D)
q4		Perform function
q5		Unlock(T)
q6		Unlock(D)
```

死锁例子2：内存可用分配空间为200KB，当两个进程都处理到第二个请求时会发生死锁。

```
P1				P2
请求80KB		请求70KB
请求60KB		请求80KB
```

处理这类死锁的一个策略：使用虚拟内存

### 6.1.2 可消耗资源

可被创建和销毁的资源，数量通常没有限制，无阻塞生产进程可以创建任意数量的这类资源，比如中断、信号、消息、I/O缓冲区中的消息

死锁例子：设计错误，难以发现

```
P1				P2
Receive(P2)		Receive(P1)
Send(P2,M1)		Send(P1,M2)
```

### 6.1.3 资源分配图

```
	请求   +----+
(P1)------>| Ra |
		  +----+
		  
	占有 	 +----+
(P1)<------| Ra |
		  +----+
```

### 6.1.4 死锁的条件

死锁存在的四个条件：前三个是必要条件，三个都存在表示可能发生死锁。四个一起构成充分必要条件。

1. 互斥
2. 占有且等待
3. 不可抢占
4. 循环等待

处理死锁的三种方法：

1. 死锁预防prevention：消除条件1~4中的一个
2. 死锁避免avoidance：基于资源分配的当前状态避免
3. 死锁检测detection：检测死锁并从中恢复

## 6.2 死锁预防 deadlock prevention

设计一种系统来排除发生死锁的可能性，破坏条件1~4之一。

死锁预防分为两类：

1. 间接死锁预防：防止条件1~3
2. 直接死锁预防：防止条件4

### 6.2.1 互斥

一般不可能禁止。可以同时读，但不能同时写，无法预防死锁。

### 6.2.2 占有且等待

要求进程一次性请求所有需要的资源，并阻塞这个进程直到所有请求都同时满足。

两个低效性：

1. 可能阻塞很长时间。可能只需要一部分资源进程就可以继续运行。可能资源分配给进程后很长时间不使用，但又因为互斥访问无法被别的进程使用。
2. 可能事先不知道需要的所有资源。

### 6.2.3 不可抢占

一般有两种方法：

1. 占有某些资源的进程进一步申请资源的时候被拒绝，则释放已经占有的资源，下次重新申请。
2. 当一个进程请求资源，但已经被另一个进程占有时，操作系统可以抢占另一个进程，要求释放。这种方法只有在优先级不同的条件下才能预防死锁。

只有在资源状态很容易保存和恢复的情况下，这种方法才实用。

### 6.2.4 循环等待

定义资源类型的线性顺序，只能按顺序请求资源。类似于预防占有且等待，这种方法是低效的。

## 6.3 死锁避免 deadlock avoidance

比死锁预防更高效。

两种死锁避免方法：

1. 进程启动拒绝：如果一个进程的请求会导致死锁，则不启动进程。
2. 资源分配拒绝：如果一个进程增加资源的请求会导致死锁，则不允许分配。

### 6.3.1 进程启动拒绝

n个进程和m个资源

```
Resource=R=[R1,R2,...,Rm]  // 每种资源的总量
Available=V=[V1,V2,...,Vm] // 未分配的每种资源的总量

Claim=C=[				// Cij=进程i对资源j的需求的数量
[C11,C12,...,C1m],
[C21,C22,...,C2m],
...
[Cn1,Cn2,...,Cnm]]

Allocation=A=[			// Aij=当前分配给进程i的资源j的数量
[A11,A12,...,A1m],
[A21,A22,...,A2m],
...
[An1,An2,...,Anm]]
```

以下关系成立：

1. $R_j=V_j+\sum_{i=1}^{N}{A_{ij}}$
2. $C_{ij} \le R_i$
3. $A_{ij} \le C_{ij}$

新进程$P_{n+1}$，仅当$R_j\ge C_{(n+1)j} + \sum_{i=1}^{n}C_{ij}对所有j $ 成立时，才启动进程。这个策略不是最优的，因为假设了最坏情况，所有进程同时发出最大请求。

### 6.3.2 资源分配拒绝

银行家算法

状态：包含Resource，Available，Claim，Allocation

安全状态：至少有一个资源分配序列不会导致死锁，否则为不安全状态

```python
import numpy as np

n_processes = int(input('Number of processes? '))
n_resources = int(input('Number of resources? '))

available_resources = [int(x) for x in input('Claim vector? ').split(' ')]

currently_allocated = np.array([[int(x) for x in input('Currently allocated for process ' + str(i + 1) + '? ').split(' ')] for i in range(n_processes)])
max_demand = np.array([[int(x) for x in input('Maximum demand from process ' + str(i + 1) + '? ').split(' ')] for i in range(n_processes)])

total_available = available_resources - np.sum(currently_allocated, axis=0)

running = np.ones(n_processes)  # An array with n_processes 1's to indicate if process is yet to run

while np.count_nonzero(running) > 0:
    at_least_one_allocated = False
    for p in range(n_processes):
        if running[p]:
            if all(i >= 0 for i in total_available - (max_demand[p] - currently_allocated[p])):
                at_least_one_allocated = True
                print(str(p) + ' is running')
                running[p] = 0
                total_available += currently_allocated[p]
    if not at_least_one_allocated:
        print('Unsafe')
        exit()
                
print('Safe')
```

优点：

* 无需死锁预防中的抢占和回滚
* 限制较少

缺点：

* 必须事先声明每个请求的最大资源
* 进程必须是无关的，执行顺序没有任何同步要求
* 分配的资源数量必须是固定的
* 占有资源时进程不能退出

## 6.4 死锁检测 deadlock detection

只要有可能，就给进程分配资源。周期性地执行一个算法检测条件4

### 6.4.1 死锁检测算法

使用矩阵Allocation，向量Available。此外还有一个请求矩阵$Q$，其中$Q_{ij}$表示 $i$ 进程请求 $j$ 资源的数量。

1. 标记Allocation中一行全为0的进程。
2. 初始化临时向量$W$，令$W$=Available。
3. 查找下标 $i$，使进程 $i$ 当前未标记且Q的第$i$行小于等于W，即 $ 对所有的1 \le k \le m , Q_{ik} \le W_k $。若找不到，终止算法。（这一步检查资源足够分配给$i$）
4. 若找到这样的行，标记进程 $i$，并把Allocation矩阵中的相应行加到W中，即 $ 对所有的1 \le k \le m , 令W_k=W_k + A_{ik}$。返回步骤3。（这一步模拟了资源分配给 $i$ 后，释放占有的所有资源）

当且仅当算法的最终结果有未标记的进程时，存在死锁，每个未标记的进程都是死锁的。

### 6.4.2 恢复

按复杂度递增

1. 取消所有死锁进程，最常用。
2. 把每个死锁进程回滚到检查点，并重启所有进程。
3. 连续取消死锁进程直到不再存在死锁。取消的进程顺应某种最小代价原则，并且需要重新调用检测算法。
4. 连续抢占资源直到不存在死锁。取消的进程顺应某种最小代价原则，并且需要重新调用检测算法。

## 6.5 综合的死锁策略

不同情况下使用不同的解决死锁策略。

* 把资源分成不同的资源类
* 预防在资源类之间循环等待产生死锁，用线性排序策略
* 一个资源类内，用最合适的算法

例子：

* 可交换空间：外存中的存储块。一次性分配所有请求的资源。
* 进程资源：可分配的设备，磁带设备和文件。死锁避免，或者资源排序。
* 内存：按页或段分配给进程。抢占预防。
* 内部资源：I/O通道，可以基于资源排序预防。

## 6.6 哲学家就餐问题

### 6.6.1 信号量解决方案

同时最多4人进入餐厅

### 6.6.2 管程解决方案

同时只有一个进程进入管程

## 6.7 Unix并发机制

* 管道
* 消息
* 共享内存
* 信号量
* 信号

管道、消息、共享内存用来在进程间传递数据，信号量和信号用于触发其他进程的行为。

### 6.7.1 管道

* 命名管道

* 匿名管道

### 6.7.2 消息

msgsnd和msgrcv系统调用

### 6.7.3 共享内存

速度最快

### 6.7.4 信号量

sem_ctl和sem_op系统调用

### 6.7.5 信号

向一个进程通知发生异步事件的机制。类似于硬件中断，但没有优先级。SIGHUP，SIGTERM，SIGKILL等等

## 6.8 Linux内核并发机制

除了管道、消息、共享内存、信号之外，还支持实时信号RT-signals。实时信号和标准Unix信号的不同点：

* 支持按优先级顺序排列的信号传递
* 多个信号排队
* 可以将数值随信号一起发送给进程

### 6.8.1 原子操作

* 原子整数操作：atomic_t类型，atomic_read，atomic_set 等原子函数
* 原子位图操作：set_bit，clear_bit 等原子函数

### 6.8.2 自旋锁

忙等，在等待时间少于2次上下文切换时间时，会很高效。

基本自旋锁有4个版本：

* 普通：临界区代码不被中断处理程序执行或禁用中断时。
* _irq：中断一直被启用时，用irq自旋锁。
* _irqsave：不知道中断是否启用时，获得锁后中断状态会被保存，锁释放时会恢复状态。
* _bh：发生中断时，中断处理器只处理最少量的必要工作。

读写自旋锁，允许多个线程同时读，互斥写，也有多个版本。

### 6.8.3 信号量

函数down对应semWait，up对应semSignal。

内核提供三种信号量：

* 二元信号量，mutex
* 计数信号量
* 读写信号量

### 6.8.4 屏障

内存屏障，防止编译器或处理器对内存访问指令重新排序。包括函数 rmb()，wmb()，mb()，Barrier()，smp_rmb()，smp_wmb()，smp_mb() 等等。SMP表示对称多处理器。

## 6.9 Solaris线程同步原语

略

## 6.10 Windows 7并发机制

略

## 6.11 Android进程间通信

在内核中新增一个连接器，提供轻量级RPC功能。使用的通信方法时ioctl系统调用。