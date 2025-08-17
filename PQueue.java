import java.util.*;

class node {
    public
        int data;
        int pri;
    
    node(int e, int p) {
        this.data = e;
        this.pri = p;
    }
}

class queue {
    public
        node []arr;
        int top;
        int bottom;

    queue(int size) {
        this.arr = new node[size];
        this.top = -1;
        this.bottom = -1;
    }

    void enqueue(node e) {
        this.arr[++this.bottom] = e;
        this.arr = bubbleSort(this.arr);
    }

    node dequeue() {
        return this.arr[++this.top];
    }

    // Lower the number higher priority -> 8, 9, 10
    // node []bubbleSort(node []arr)
    // {
    //     for (int i = 0; i < this.bottom; i++) {
    //         for (int j = 0; j < this.bottom; j++) {
    //             // System.out.println(arr[i].pri + " | " + arr[j + 1].pri);
    //             if (arr[j].pri > arr[j + 1].pri) {
    //                 // swap temp and arr[i]
    //                 node temp = arr[j];
    //                 arr[j] = arr[j + 1];
    //                 arr[j + 1] = temp;
    //             }
    //         }
    //     }

    //     return arr;
    // }

    // Higher the number higher the priority -> 10, 9, 8
    node []bubbleSort(node []arr)
    {
        for (int i = 0; i < this.bottom; i++) {
            for (int j = 0; j < this.bottom; j++) {
                // System.out.println(arr[i].pri + " | " + arr[j + 1].pri);
                if (arr[j].pri < arr[j + 1].pri) {
                    // swap temp and arr[i]
                    node temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        return arr;
    }
}

public class PQueue {
    public static void main(String[] argv) {
        queue q = new queue(5);

        q.enqueue(new node(5, 6));
        q.enqueue(new node(1, 10));
        q.enqueue(new node(2, 9));
        q.enqueue(new node(3, 11));
        q.enqueue(new node(4, 7));

        node n = q.dequeue();
        System.out.println(n.data + " " + n.pri);

        n = q.dequeue();
        System.out.println(n.data + " " + n.pri);

        n = q.dequeue();
        System.out.println(n.data + " " + n.pri);

        n = q.dequeue();
        System.out.println(n.data + " " + n.pri);

        n = q.dequeue();
        System.out.println(n.data + " " + n.pri);
    }
}