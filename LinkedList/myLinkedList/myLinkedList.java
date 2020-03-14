
public class myLinkedList
{
    Node start;
    myLinkedList(Node x){
        start = x;
    }

    public static void delete(myLinkedList y, int pos){
        if(pos == 0){
            pos = pos;
        }
        else{
            pos = pos - 1;
        }
        Node temp = y.start;
        for(int i = 0; i < pos - 1; i++){

            temp = temp.next;
        }
        Node tempNext = temp.next.next;
        temp.next = tempNext;

    }

    public static void printAll(myLinkedList x){
        Node y = x.start;

        while(y.next != null){
            System.out.print(y.data + ", ");
            y = y.next;
        }
        System.out.print(y.data);
        System.out.println();

    }

    public static void insert(myLinkedList y, int pos, int data){
        if(pos == 0){
            pos = pos;
        }
        else{
            pos = pos - 1;
        }
        Node temp = y.start;
        //insertNum = insertNum + 1;
        for(int i = 0; i < pos - 1; i++){

            temp = temp.next;
        }
        Node inserted = new Node(data, temp.next);
        temp.next = inserted;

    }

    public static void delHead(myLinkedList y){
        int pos = 0;
        Node temp = y.start;

    }

}
