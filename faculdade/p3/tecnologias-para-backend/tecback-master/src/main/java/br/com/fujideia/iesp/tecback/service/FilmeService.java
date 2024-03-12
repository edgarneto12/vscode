package br.com.fujideia.iesp.tecback.service;

import br.com.fujideia.iesp.tecback.model.Filme;
import br.com.fujideia.iesp.tecback.repository.FilmeRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

@AllArgsConstructor
@Service
public class FilmeService {
    private FilmeRepository repository;

    public Filme salvar(Filme filme){
        return repository.save(filme);
    }

    public List<Filme> listarTodos(){
        
    }

}
