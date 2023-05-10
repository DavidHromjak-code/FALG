 async function get_data_python() {
   eel.get_data()((setData) => {
       setData.forEach(object => {
           object = JSON.parse(object);
           console.log(object);
           const para = document.createElement("div");
           para.innerHTML = `<h1>${object["engName"]}</h1>`
           const element = document.getElementById("content");
           element.appendChild(para);
       })
     }
   )
 }
