function PersonFunction(name: string, age: number){
    console.log(`Olá ${name}, você tem ${age} anos de idade.`)
}

PersonFunction("Arrys", 18);

const Person = (name: string, age: number) => {
    console.log(`Olá ${name}, você tem ${age} anos de idade.`)
}

Person("Arrys", 8);

type IPerson = {
    name: string;
    age: number;
    status: EstadoCivil;
}

enum EstadoCivil {
    Casado = "Casado",
    Solteiro = "Solteiro",
    Amancebado = "Amancebado"
}

const PersonTipada = ({name, age, status}:IPerson) => {
    console.log(`Olá ${name}, você tem ${age} anos de idade e você é ${status}.`)
}

PersonTipada({name: "Arrys", age: 18, status: EstadoCivil.Solteiro})

console.log("2" + 2)