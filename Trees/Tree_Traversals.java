import java.io.*;
import java.util.*;

class Node{
    int data;
    Node left,right;
    Node(int d){
        data = d;
        left = null;
        right = null;
    }
}
public class Solution {
    public static Node Insert(Node r, int d)
    {
        if(r==null)
            return new Node(d);
        if (d<r.data)
            r.left = Insert(r.left,d);
        else
            r.right = Insert(r.right,d);
        return r;
    }
    public static void PreOrder(Node r)
    {
        if (r==null)
            return;
        System.out.print(r.data+" ");
        PreOrder(r.left);
        PreOrder(r.right);
    }
    public static void InOrder(Node r)
    {
        if (r==null)
            return;
        InOrder(r.left);
        System.out.print(r.data+" ");
        InOrder(r.right);
    }
    public static void PostOrder(Node r)
    {
        if (r==null)
            return;
        PostOrder(r.left);
        PostOrder(r.right);
        System.out.print(r.data+" ");
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int test=0 ; test<T ; test++)
        {
            Node root = null;
            int N = sc.nextInt();
            for ( int i=0 ; i<N ; i++)
            {
                int data = sc.nextInt();
                root = Insert(root,data);
            }
            PreOrder(root);
            System.out.println();
            InOrder(root);
            System.out.println();
            PostOrder(root);
            System.out.println();
            System.out.println();
        }
    }
}
