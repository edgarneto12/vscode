package notadeaula02;

public class Pessoa {
    

    private Double peso;
    private Double altura;
 

    public void setPeso(Double peso) {
        this.peso = peso;
    }

    public Double getPeso() {
        return peso;
    }

    public void setAltura(Double altura) {
        this.altura = altura;
    }
    public Double getAltura() {
        return altura;
    }
    public Double getImc() {
        return peso / (altura * 2);
    }

    // get e set para nome
}