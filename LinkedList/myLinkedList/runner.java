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
    public static void printAll(myLinkedList x){
      Node y = x.start;
      
        
      do{
          
          System.out.println(y.data);
        
          y = y.next;
        
        }while(y.next != null);
      
    
    
    }
    public static void main(String [] args){
        Node node1 = new Node(5, null);
        myLinkedList coolList = new myLinkedList(node1);
        Node node2 = new Node(12, null);
        node1.next = node2;
        Node node3 = new Node(14, null);
        node2.next = node3;
        Node node4 = new Node(26,null);
        node3.next = node4;
        printAll(coolList);
    
    }
}
