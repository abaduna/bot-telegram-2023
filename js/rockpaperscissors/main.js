let jugada_n_1 = ""
let jugador_n_2 =""
const agregarJugada=(valor,jugador)=>{

    if (jugador === "jugador_1") {
        jugada_n_1 = valor

    } else if (jugador === "jugador_2") {
        jugador_n_2 = valor
        
    }

    console.log(`el jugada del jugador n1 es ${jugada_n_1}`) //aca da lo que tien que dar
    console.log(`el jugada del jugador n2 es ${jugador_n_2}`)//aca da lo que tien que dar
    ganar()
}
const ganar =(jugada_n_1,jugador_n_2)=>{
    console.log(`el jugada del jugador n1 es ${jugada_n_1}`) //aca da undefined
    console.log(`el jugada del jugador n2 es ${jugador_n_2}`)//aca da undefined

}
const start=()=>{
    document.getElementById("tijera").addEventListener("click",()=>agregarJugada("tijera","jugador_1"))
    document.getElementById("paper").addEventListener("click",()=>agregarJugada("paper","jugador_1"))
    document.getElementById("rock").addEventListener("click",()=>agregarJugada("rock","jugador_1"))
    document.getElementById("tijera_2").addEventListener("click",()=>agregarJugada("tijera","jugador_2"))
    document.getElementById("paper_2").addEventListener("click",()=>agregarJugada("paper","jugador_2"))
    document.getElementById("rock_2").addEventListener("click",()=>agregarJugada("rock","jugador_2"))


}


window.onload = start