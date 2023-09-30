package Notadeaula01.ex02;

public class calculoex08 {
    Float n1,n2,n3,total;
    String nome;
    public void media() {
        total = ((n1 + n2 + n3) / 3);
        if (total >= 7){
            System.out.printf(nome + " foi Aprovado, sua nota foi: %.2f ", total);
        }else{
            System.out.println(nome + " foi Reprovado, sua nota foi: "+ total);
        }

        
    }
}