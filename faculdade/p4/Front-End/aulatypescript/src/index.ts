let numero:string[] = ["1", "2"]
let numero2 = 12


console.log(numero)

enum StatusCode {
    Sucess = 200,
    NotFound = 404,
    InternalService = 500,
}

let currentStatus:StatusCode = StatusCode.InternalService

console.log(currentStatus)

let id:number | string = "olá"

console.log(id)