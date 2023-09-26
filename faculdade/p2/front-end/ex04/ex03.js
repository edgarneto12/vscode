var notas = [];

for (var i = 1; i <= 3; i++) {
    var nota = parseFloat(prompt("Digite a" + i + "º nota: "));
    notas.push(nota);
}

var soma = 0;
for (var i = 0; i < notas.length; i++) {
    soma += notas[i];
}
var media = soma / notas.length;

if (media <= 4) {
    console.log("Aluno Reprovado! \nMédia: " + media)
} else if (media >= 7) {
    console.log("Aluno aprovado! \nMédia: " + media)
} else {
    console.log("Aluno em recuperação");

    var notaRec = parseFloat(prompt("Digite a nota da recuperação: "));
    var mediaFinal = (media + notaRec) / 2;

    if (mediaFinal >= 5) {
        console.log("Aluno aprovado, após a recuperação \nMédia: " + mediaFinal)
    } else {
        console.log("Aluno reprovado, após a recuperação");
    }
}