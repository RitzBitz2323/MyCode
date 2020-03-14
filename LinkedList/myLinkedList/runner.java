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
        coolList.insert(coolList, 1, 135);
        coolList.insert(coolList, 2, 21);
        coolList.insert(coolList, 3, 43);
        coolList.insert(coolList, 4, 982);
        coolList.insert(coolList, 5, 34);
        coolList.printAll(coolList);
        //coolList.delete(coolList, 2);
        
    }
}
