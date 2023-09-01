
public class calculoex07 {
    int matricula;
    String nome;
    double salariobruto, deducaoinss, total;
    public void desconto() {
        total = salariobruto - salariobruto * 0.15;
        System.out.println("Matricula: "+ matricula);
        System.out.println("Nome Completo: "+ nome);
        System.out.println("Salário bruto: "+salariobruto);
        System.out.println("Dedução INSS: 15%");
        System.out.println("Salário Líquido: "+ total);
    }

}