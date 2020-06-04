
public class Runner
{
    public static void main(String [] args){
        BinaryTree myTree = new BinaryTree(5);
        myTree.root.left = new Node(3);
        myTree.root.right = new Node(7);
        myTree.insert(50);
        myTree.insert(23);
        myTree.insert(14);
        myTree.insert(123);
        myTree.print();
        
        
    
    }
}
