"use strict";
let numero = ["1", "2"];
let numero2 = 12;
console.log(numero);
var StatusCode;
(function (StatusCode) {
    StatusCode[StatusCode["Sucess"] = 200] = "Sucess";
    StatusCode[StatusCode["NotFound"] = 404] = "NotFound";
    StatusCode[StatusCode["InternalService"] = 500] = "InternalService";
})(StatusCode || (StatusCode = {}));
let currentStatus = StatusCode.InternalService;
console.log(currentStatus);
let id = "olá";
console.log(id);
