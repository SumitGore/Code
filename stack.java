import java.util.*;

class MyStack {
    public
        int top;
        int []arr;
        int size;
    
    MyStack(int size) {
        this.top = -1;
        this.size = size;
        this.arr = new int[size];
    }

    void push(int d) {
        if(this.top == this.size - 1) {
            System.out.println("Stack is full!!");
            return;
        }

        this.arr[++this.top] = d;
    }

    int pop() {
        if(this.top == -1) {
            System.out.println("Stack is empty!!");
            return -1;
        }

        return this.arr[this.top--];
    }

    int peep() {
        if(this.top == -1) {
            System.out.println("Stack is empty!!");
            return -1;
        }

        return this.arr[this.top];
    }
}

public class stack {
    public static void main(String[] argv) {
        MyStack q = new MyStack(10);

        // First Come first out. -> 1, 2, 3, 4 => 4, 4, 3, 2, 1

        q.push(1);
        q.push(2);
        q.push(3);
        q.push(4);

        System.out.println("Peep -> " + q.peep());
        System.out.println("Pop -> " + q.pop());
        System.out.println("Pop -> " + q.pop());
        System.out.println("Pop -> " + q.pop());
        System.out.println("Pop -> " + q.pop());
    }
}