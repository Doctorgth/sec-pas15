function copyPassword() {
  var passwordInput = document.getElementById("password-input");
  passwordInput.select();
  document.execCommand("copy");
}

function showPassword() {
  //var passwordInput = document.getElementById("password-input");
  //var maskedPasswordInput = document.getElementById("masked-password-input");
  //maskedPasswordInput.value = passwordInput.value;
  var passwordInput = document.getElementById("password-input");
 var buttonText=document.getElementById("")
if (passwordInput.type=="text")
{
passwordInput.type="password";
}
else
{
  passwordInput.type = "text";
}
}



function showHidePole(id){

  var passwordInput = document.getElementById(id);
 var img_b=document.getElementById(id+"_img");
if (passwordInput.type=="text")
{
passwordInput.type="password";
img_b.src="static/images/show_on.png"
}
else
{
  passwordInput.type = "text";
img_b.src="static/images/hide_on.png"
}

}

function clearPole(id){

var poleInput=document.getElementById(id);
poleInput.value="";
//var imgg=document.getElementById("key_img");
//imgg.src="static/images/clear_off.png"

}

async function hash_str(str){

  const encoder = new TextEncoder();
  const data = encoder.encode(str);
  const hashBuffer = await crypto.subtle.digest('SHA-512', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashHex = hashArray.map(byte => byte.toString(16).padStart(2, '0')).join('');
  return hashHex;

}

function forward_trans(){
var a=document.getElementById("key");
var b=document.getElementById("base_w");
var c=document.getElementById("place_w");
a=a.value;
b=b.value;
c=c.value;
var x=a+b;
var y=b+c;
var z=c+a;
x=hash_str(x);
alert(x);

}