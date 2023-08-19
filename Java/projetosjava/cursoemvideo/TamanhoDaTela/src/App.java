import java.awt.Dimension;
import java.awt.Toolkit;

public class App {
    public static void main(String[] args) throws Exception {
        Dimension d = Toolkit.getDefaultToolkit().getScreenSize();
        int lar = (int) d.getWidth();
        int alt = (int) d.getHeight();
        System.out.println(lar + "x" + alt);
    }
}
