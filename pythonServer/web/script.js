 async function get_data_python() {
   let prompt = eel.helloWorld()((setData) => {
       setData.forEach(object => {
         const para = document.createElement("p");
         const node = document.createTextNode(object);
         para.appendChild(node);
         const element = document.getElementById("content");
         element.appendChild(para);
       })
     }
   )
   console.log(prompt);

 }
