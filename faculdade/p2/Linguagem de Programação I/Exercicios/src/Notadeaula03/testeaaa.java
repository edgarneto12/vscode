package Notadeaula03;

public class testeaaa {
    public static void main(String[] args) {
        int a = 100; int b = 10; int c = 0;
        a = b;
        System.out.println("|" + a + "|");

        if ( a <12 || b > 5) {
            System.out.println("|"+ ++a + "|" + c + "|");
        }else {
            System.out.println("|"+ b + "|");
        }
    }
}
