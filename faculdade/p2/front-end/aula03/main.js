console.log("A página foi carregada !")
var nome = "Edgar"

if (nome == "Edgar") {
    console.log("Olá,", nome)
}else {
    console.log("Olá usuario")
}
console.log("for normal")
for (var i=0; i<=10;i++) {
    console.log("Número nº", i)
}
var valores = [1,2,3,4,5]
console.log("for com in e lista")
for (var numero in valores){
    console.log("Numero nº", numero)
} 
var teste = true 
var cont = 0;
console.log("while normal")
while (teste == true) {
    cont++;
    console.log("Olá turma", cont)
    if (cont>=10) teste = false;
}
console.log("while com do")
do {
    cont++;
    console.log("Olá turma", cont)
    if (cont>=10) teste = false;
}while (teste == true);
