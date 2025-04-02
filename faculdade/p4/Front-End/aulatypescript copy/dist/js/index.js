"use strict";
function PersonFunction(name, age) {
    console.log("Ol\u00E1 ".concat(name, ", voc\u00EA tem ").concat(age, " anos de idade."));
}
PersonFunction("Arrys", 18);
var Person = function (name, age) {
    console.log("Ol\u00E1 ".concat(name, ", voc\u00EA tem ").concat(age, " anos de idade."));
};
Person("Arrys", 8);
var EstadoCivil;
(function (EstadoCivil) {
    EstadoCivil["Casado"] = "Casado";
    EstadoCivil["Solteiro"] = "Solteiro";
    EstadoCivil["Amancebado"] = "Amancebado";
})(EstadoCivil || (EstadoCivil = {}));
var PersonTipada = function (_a) {
    var name = _a.name, age = _a.age, status = _a.status;
    console.log("Ol\u00E1 ".concat(name, ", voc\u00EA tem ").concat(age, " anos de idade e voc\u00EA \u00E9 ").concat(status, "."));
};
PersonTipada({ name: "Arrys", age: 18, status: EstadoCivil.Solteiro });
console.log("2" + 2);
