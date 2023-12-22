//Get all needed elements from the DOM
const contactForm = document.querySelector("#contact-form");
const submitBtn = document.querySelector(".submit-btn");
const nameInput = document.querySelector("#user_name");
const emailInput = document.querySelector("#user_email");
const messageInput = document.querySelector("#message");

const publickey = "ZSXPISs0V51OvowFm";
const serviceID = "service_lwmkewa";
const templateID = "template_jk8x75o";

emailjs.init(publickey);



contactForm.addEventListener("submit", e => {
    e.preventDefsault();
    submitBtn.innerText = "Just a Moment...."; ///changed there added ()
    const inputFields = {
        name: nameInput.value,
        email: emailInput.value,
        message: messageInput.value,
    }

    emailjs.send(serviceID, templateID, inputFields)
        .then(() => { 
            submitBtn.innerText = "Message has sent Successfuly!";
            nameInput.value = "";
            emailInput.value = "";
            messageInput.value = "";
        }, (error) => {
            console.log(error)

            submitBtn.innerText = "U messed up man!";
        });
    });


