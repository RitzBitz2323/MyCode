
public class BinaryTree
{   
    Node root;
    Node left;
    Node right;
    
    BinaryTree(int data){
        root = new Node(data);

    }

    public void insert(int data){
        Node temp = new Node(data);
        
        if(this.left == null){
            this.left = temp;

        }
        else if(this.right == null){
            this.right = temp;
        }

    }
}
