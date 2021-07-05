
document.querySelector("form").querySelectorAll("input")

document.querySelector("div[ng-form='section.form']")

let pageItems = document.querySelectorAll("fieldset");
pageItems.forEach((d) => {
    let el = d.querySelectorAll("input");
    if (el.type === "radio") {
        el.checked = String.match(/Decline.+/, el.value);
    }

})

document.querySelectorAll("fieldset")[0].querySelectorAll("input")