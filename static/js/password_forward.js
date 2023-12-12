function clearPole(id){

var poleInput=document.getElementById(id);
poleInput.value="";
//var imgg=document.getElementById("key_img");
//imgg.src="static/images/clear_off.png"

}


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
}


function copyTextButton(inputId) {
  var inputElement = document.getElementById(inputId);
  inputElement.select();
  inputElement.setSelectionRange(0, 99999); // Для поддержки мобильных устройств
  document.execCommand("copy");
}

function hash_str(a){
  var inputText = a;
  var sha512Hash = CryptoJS.SHA512(inputText);
  
  // Получаем строковое представление хэша
  var hashResult = sha512Hash.toString(CryptoJS.enc.Hex);
  
  // Выводим результат в alert
  return hashResult;
}

async function forward_trans() {
  var a = document.getElementById("key").value;
  var b = document.getElementById("password").value;
  var c = document.getElementById("spec").value;
  var len= document.getElementById("len").value;
 var x=a+b;
 var y=b+c;
 var z=c+a;
 var x=hash_str(x);
 var y=hash_str(y);
 var z=hash_str(z);
  var ret = x+y+z;
  ret = hash_str(ret);
  
  var password = await useApi(ret,len);
  var out_pole = document.getElementById("output-pole");
  out_pole.value = password;
}


const useApi = async (key,len) => {
  const url = '/api';  // URL вашей Flask-страницы
  const data = new FormData();
  data.append('key', key);
  data.append('len', len);

  try {
    const response = await fetch(url, {
      method: 'POST',
      body: data
    });

    const password = await response.text();
    //console.log(password);
    return password;
    // Дальше можно обработать полученное значение password
  } catch (error) {
    console.error('Ошибка:', error);
  }
};

function clearPoleAll(){
let ids=["key","spec","len","password","output-pole"]
ids.forEach(clearPole);


}
