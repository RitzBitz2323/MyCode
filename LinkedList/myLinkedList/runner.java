/**
Previous printAll code:
System.out.println(y.start.data);
System.out.println(y.start.next.data);
System.out.println(y.start.next.next.data);
System.out.println(y.start.next.next.next.data); prints null

Node y = x.start;
while(y.next != null){
System.out.println(y.data);
y = y.next;

}
System.out.println(y.data);
 **/

public class runner
{   

    public static void main(String [] args){
        Node node1 = new Node(5, null);
        myLinkedList coolList = new myLinkedList(node1);
        
        
        
       
        
        
        coolList.insert(1, 135);
        coolList.insert(2, 21);
        coolList.insert(3, 43);
        coolList.insert(4, 982);
        coolList.insert(5, 34);
        coolList.insert(100, 100);
        coolList.printAll();
        
        coolList.delete(3);
        coolList.printAll();
        
        coolList.delete(57);
        coolList.printAll();
        
        //coolList.delete(coolList, 2);
        
    }
}
