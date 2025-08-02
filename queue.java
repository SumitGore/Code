import java.util.*;

class MyQueue {
    public
        int bottom;
        int top;
        int size;
        int []arr;
    
    MyQueue() {
        this.bottom = -1;
        this.top = -1;
        this.size = 10;
        arr = new int[10];
    }

    boolean isFull() {
        return ((this.size - 1) == this.top);
    }

    boolean isEmpty() {
        return this.bottom == this.top;
    }

    void enqueue(int d) {
        if(this.isFull()) {
            System.out.println("Queue is full!!");
            return;
        }

        this.arr[++this.top] = d;
    }

    int dequeue() {
        if(this.isEmpty()) {
            System.out.println("Queue is Empty!!");
            return -1;
        }

        return this.arr[++this.bottom];
    }
}

public class queue {
    public static void main(String[] argv) {
        MyQueue q = new MyQueue();

        // First Come first out. -> 1, 2, 3, 4 [same order].

        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        q.enqueue(4);

        System.out.println("Dequeue -> " + q.dequeue());
        System.out.println("Dequeue -> " + q.dequeue());
        System.out.println("Dequeue -> " + q.dequeue());
        System.out.println("Dequeue -> " + q.dequeue());
        System.out.println("Dequeue -> " + q.dequeue());
    }
}