 async function get_data_python() {
   eel.get_data()((setData) => {
       setData.forEach(object => {
           console.log(object);
           object = JSON.parse(object);
           console.log(object);
         const para = document.createElement("p");
         const node = document.createTextNode(object["engName"]);
         para.appendChild(node);
         const element = document.getElementById("content");
         element.appendChild(para);
       })
     }
   )
 }
