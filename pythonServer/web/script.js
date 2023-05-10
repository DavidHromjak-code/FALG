 async function get_data_python() {
   eel.get_data()((setData) => {
       setData.forEach(object => {
           object = JSON.parse(object);
           console.log(object);
           const para = document.createElement("div");
           para.classList.add('obal');
           para.innerHTML = `<div class="left"><h1>${object["engName"]}</h1>
            <h4>Score: ${object["score"]}</h4> <a href="${object["url"]}">Url: ${object["japName"]}</a> <h5>Episodes: ${object["eps"]}</h5></div>
            <div class="right"><img src="${object["image"]}"</img></div>`
           const element = document.getElementById("content");
           element.appendChild(para);
       })
     }
   )
 }
