function togglePassword(){

    let pwd=document.getElementById("password");

    let btn=document.getElementById("toggleBtn");

    if(pwd.type==="password"){

        pwd.type="text";

        btn.innerHTML="Hide";

    }

    else{

        pwd.type="password";

        btn.innerHTML="Show";

    }

}


function checkPassword(){

    let password=document.getElementById("password").value;

    if(password===""){

        alert("Please enter a password.");

        return;

    }

    fetch("/predict",{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify({

            password:password

        })

    })

    .then(response=>response.json())

    .then(data=>{

        let result=document.getElementById("result");

        let progress=document.getElementById("progress");

        let tips=document.getElementById("tips");

        result.innerHTML=data.strength;

        if(data.strength==="Weak"){

            progress.style.width="30%";

            progress.style.background="red";

            result.style.color="red";

            tips.innerHTML="❌ Use at least 8 characters, uppercase, numbers and special symbols.";

        }

        else if(data.strength==="Medium"){

            progress.style.width="65%";

            progress.style.background="orange";

            result.style.color="orange";

            tips.innerHTML="⚠ Add more special characters and increase password length.";

        }

        else{

            progress.style.width="100%";

            progress.style.background="green";

            result.style.color="green";

            tips.innerHTML="✅ Excellent! Your password is strong.";

        }

    });

}