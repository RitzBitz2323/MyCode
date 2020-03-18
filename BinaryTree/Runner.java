
public class Runner
{
    public static void main(String [] args){
        BinaryTree myTree = new BinaryTree(5);
        myTree.root.left = new Node(3);
        myTree.root.right = new Node(7);
        myTree.root.left.left = new Node(15);
        myTree.root.left.right = new Node(23);
        myTree.root.right.left = new Node(47);
        myTree.root.right.right = new Node(109);
        
        
    
    }
}
