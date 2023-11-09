public class PessoaFisica extends Pessoa {
    @Override
    public String toString() {
        return "PessoaFisica [Nome: "+ getNome() + ", idade:" + getIdade() + ", Tipo Pessoa Física]";
    }
    
}
