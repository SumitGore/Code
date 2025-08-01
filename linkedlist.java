package linkedlist;

class Node {
	public
		int data;
		Node next;
	
	Node(int d) {
		this.data = d;
		this.next = null;
	}
}

class LL {
	public
		Node head;
	
	LL() {
		this.head = null;
	}
	
	void incert(int d) {
		Node n = new Node(d);
		
		// if head is empty.
		if(this.head == null) {
			this.head = n;
			return;
		}
		
		// already have some elements.
		Node t = this.head;
		while(t.next != null) t = t.next;
		t.next = n;
	}
	
	void display() {
		Node t = this.head;
		while(t != null) {
			System.out.println(" -> " + t.data);
			t = t.next;
		}
	}
};

public class linkedlist {
	public static void main(String[] argv) {
		LL ll = new LL();
		ll.incert(1);
		ll.incert(2);
		ll.incert(3);
		
		ll.display();
	}
}
