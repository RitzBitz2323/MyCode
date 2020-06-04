
public class BinaryTree
{   
    Node root;
    Node left;
    Node right;

    BinaryTree(int data){
        root = new Node(data);

    }

    public void print(){
        Node temp = this.root;
        Node temp2 = this.left;

        while((temp.left != null && temp.right != null)|| (temp2.left != null && temp2.right != null) ){
            System.out.println(temp.data);
            System.out.println(temp.left.data);
            System.out.println(temp.right.data);
            System.out.println(temp2.data);
            System.out.println(temp2.left.data);
            System.out.println(temp2.right.data);
            if(temp.left != null){
                temp = temp.left;
            }
            if(temp.left != null){
                temp2 = temp.right;
            }
            

        } 
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
