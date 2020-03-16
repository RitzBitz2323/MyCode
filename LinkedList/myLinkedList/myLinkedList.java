
public class myLinkedList
{
    Node start;

    myLinkedList(Node x){
        start = x;

    }

    public void delete(int pos){
        int lengthLL = this.length();
        if(pos > lengthLL){
            pos = lengthLL;
        }

        if(pos == 0){
            pos = pos;
        }
        else{
            pos = pos - 1;
        }
        Node temp = this.start;
        for(int i = 0; i < pos - 1; i++){

            temp = temp.next;
        }
        Node tempNext = temp.next.next;
        temp.next = tempNext;

    }

    public void printAll(){
        Node y = this.start;

        while(y.next != null){
            System.out.print(y.data + ", ");
            y = y.next;
        }
        System.out.print(y.data);
        System.out.println();

    }

    public void insert(int pos, int data){
        int lengthLL = this.length();
        if(pos > lengthLL){
            pos = lengthLL;
        }

        Node temp = this.start;
        //insertNum = insertNum + 1;
        for(int i = 0; i < pos - 1; i++){

            temp = temp.next;
        }
        Node inserted = new Node(data, temp.next);
        temp.next = inserted;

    }

    private int length(){
        Node temp = this.start;
        int count = 0;
        while(temp != null){
            count++;
            temp = temp.next;
        }
        return count;
    }

}
