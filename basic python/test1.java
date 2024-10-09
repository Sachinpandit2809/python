import java.util.*;

public class test1 {
    public static void main(String args[]) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("enter your first number");
            int a = sc.nextInt();
            System.out.println("enter your second  number");
            int b = sc.nextInt();
            System.out.println("enter your third number");
            int c = sc.nextInt();
            System.out.println("enter your password for print --");
            String pass = sc.next();

            System.out.println("sum of two number" + (a + b));
            System.out.println("average of three number " + (float) (a + b + c) / 3);
            System.out.println("perimeter=" + 2 * (a + b));

            System.out.println("area=" + a * b);
            System.out.println(pass);
            System.out.println("Enter a string ");
            String str = sc.nextLine();

            // System.out.println("Enter a string ");
            // String str = sc.nextLine();
            System.out.println(str);
        }
    }
}