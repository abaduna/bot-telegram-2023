const  llamada_A_la_API=async()=>{
    let url ="https://api.chucknorris.io/jokes/random"
    const api = await fetch(url)
    const  data = await api.json()
    console.log(data)
    escrivirData(data)
}
const escrivirData = (data)=>{
    divRes = document.querySelector("#resultado")
    divRes.innerHTML = ` <div class="card " style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">${data.value}</h5>
      <p class="card-text"> fue creada el ${data.created_at}</p>
      <button class="btn  boton" onclick="llamada_A_la_API()" type="submit">Buscar otra</button>
    </div>
  </div>`

}
llamada_A_la_API()