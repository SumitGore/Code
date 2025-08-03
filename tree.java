class Node {
    public
        int data;
        Node left;
        Node right;
    
    Node(int d) {
        this.data = d;
        this.left = null;
        this.right = null;
    }

    // DFS -> Defth first search.
    static void preOrder(Node root) {
        if(root != null) {
            System.out.printf(root.data + " ");
            preOrder(root.left);
            preOrder(root.right);
        }
    }

    static void inOrder(Node root) {
        if(root != null) {
            inOrder(root.left);
            System.out.printf(root.data + " ");
            inOrder(root.right);
        }
    }

    static void postOrder(Node root) {
        if(root != null) {
            postOrder(root.left);
            postOrder(root.right);
            System.out.printf(root.data + " ");
        }
    }

    // BFS -> Breth first search.
    static void levelOrder(Node root) {
        MyQueue q = new MyQueue();
        q.enqueue(root);

        Node t = null;

        while(!q.isEmpty()) {
            t = q.dequeue();
            System.out.printf(t.data + " ");
            if(t.left != null) {
                q.enqueue(t.left);
            }
            if(t.right != null) {
                q.enqueue(t.right);
            }
        }
    }
}

class MyQueue {
    public
        int bottom;
        int top;
        int size;
        Node []arr;
    
    MyQueue() {
        this.bottom = -1;
        this.top = -1;
        this.size = 10;
        arr = new Node[15];
    }

    boolean isFull() {
        return ((this.size - 1) == this.top);
    }

    boolean isEmpty() {
        return this.bottom == this.top;
    }

    void enqueue(Node d) {
        if(this.isFull()) {
            System.out.println("Queue is full!!");
            return;
        }

        this.arr[++this.top] = d;
    }

    Node dequeue() {
        if(this.isEmpty()) {
            System.out.println("Queue is Empty!!");
            return new Node(-1);
        }

        return this.arr[++this.bottom];
    }
}

public class tree {
    public static void main(String[] argv) {
        Node root = new Node(0);
        root.left = new Node(1);
        root.right = new Node(2);
        root.left.left = new Node(3);
        root.left.right = new Node(4);
        root.right.left = new Node(5);
        root.right.right = new Node(6);

        System.out.printf("Preorder: ");
        Node.preOrder(root);
        System.out.printf("\nInorder: ");
        Node.inOrder(root);
        System.out.printf("\nPostorder: ");
        Node.postOrder(root);
        System.out.printf("\n\nLevelOrder: ");
        Node.levelOrder(root);
    }
}