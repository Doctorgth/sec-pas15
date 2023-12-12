

function showHidePole(id){

  var passwordInput = document.getElementById(id);
 var img_b=document.getElementById(id+"_s_b");
if (passwordInput.type=="text")
{
passwordInput.type="password";
//img_b.src="static/images/show_button.png"
img_b.className = "show-button";
}
else
{
  passwordInput.type = "text";
//img_b.src="static/images/hide_button.png"
img_b.className = "hide-button";

}
};



const useApi = async (location) => {
  const url = '/api_sorry';  // URL вашей Flask-страницы
  var nickPole=document.getElementById("spec");
  
  const data = new FormData();
  data.append('name', nickPole.value);
  data.append('location', location);
  
  if (checkStatus(location,nickPole.value))
{
data.append('type', "activate");
}
else
{
data.append('type', "deactivate");
}

  try {
    const response = await fetch(url, {
      method: 'POST',
      body: data
    });

    const password = await response.text();
    //console.log(password);
    //alert(password);
    // Дальше можно обработать полученное значение password
  } catch (error) {
    console.error('Ошибка:', error);
  }



};

function checkStatus(id,name){
var img=document.getElementById(id+"_img");
var imagePath = img.src;
var text=document.getElementById(id);
var last=imagePath.slice(-7);
var first=imagePath.slice(0, -7);
if (last=="off.jpg")
{
var newPath=first+"onn.jpg";
img.src=newPath;
text.textContent="Чекается by: "+name;
return true;
}

else
{
var newPath=first+"off.jpg";
img.src=newPath;
text.textContent="Не чекается";
return false;
}


};