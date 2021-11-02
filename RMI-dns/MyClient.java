import java.rmi.*;
import java.util.*;  

public class MyClient {

  public static void main(String args[]) {
    Scanner sc=new Scanner(System.in);
    try {
      Adder stub = (Adder) Naming.lookup("rmi://localhost:5000/sonoo");
      System.out.println("Enter domain name: ");
      String domainname=sc.nextLine();
      System.out.println(domainname);

      System.out.println(stub.add(34, 4));
    } catch (Exception e) {
      System.out.println(e);
    }
  }
}
