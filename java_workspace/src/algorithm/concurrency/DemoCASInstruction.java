package algorithm.concurrency;

import java.util.concurrent.atomic.AtomicBoolean;

class Demo implements Runnable {
    private AtomicBoolean flag;

    public Demo(AtomicBoolean flag) {
        this.flag = flag;
    }

    @Override
    public void run() {
        String tName = Thread.currentThread().getName();
        System.out.println(tName + " running");
        for (int i = 0; i < 10; i++) {
            while (!flag.compareAndSet(false, true)) {
                System.out.println(tName + " spin");
            }
            System.out.println(tName + " enter critical area");
            System.out.println(tName + " exit critical area");
            flag.set(false);
        }
        System.out.println(tName + " ends");
    }
}

public class DemoCASInstruction {

    public static void main(String[] args) {
        AtomicBoolean flag = new AtomicBoolean(false);
        Thread th0 = new Thread(new Demo(flag));
        Thread th1 = new Thread(new Demo(flag));
        th0.start();
        th1.start();
        try {
            th0.join();
            th1.join();
        } catch (Exception e) {
            System.out.println("join failed");
        }
    }
}
