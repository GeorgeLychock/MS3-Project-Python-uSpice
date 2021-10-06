$(document).ready(function () {
    $(".tooltipped").tooltip();
});


function addIngredient() {
    if (localStorage.getItem("ingredientNumber")) {
        var i = Number(localStorage.getItem("ingredientNumber")) + 1;
        console.log(i);

    } else {
        var i = 1;
    }
    localStorage.setItem("ingredientNumber", i);
    return $("#ingredient_region").append(buildIngredientForm(i));

}

function buildIngredientForm(i) {
    let inc = i;

    return `
    <label for="ingredient_region${inc}" class="form-label">Region</label>
    <select id="ingredient_region${inc}" name="ingredient_region${inc}" class="form-select us-dropdown">
        <option selected>Choose...</option>
        {% for region in regions %}
        <option>{{region.region_name}}</option>
        {% endfor %}
    </select>
    `
}

function addIngredientNumber() {
    var localStoreName = "ingredientNumber";
    var iNum;

    // Check if localStorage is enabled
    if (storageAvailable('localStorage')) {
        // We can use localStorage, check if localStorage var has been initiated
        if (localStorage.getItem(localStoreName)) {
            // Add widget ID to the localStorage string and store
            let ingredientNumber = localStorage.getItem(localStoreName); //returns a string, comma delimited, convert to array
            ingredientNumber =+ 1;
            localStorage.setItem(localStoreName, ingredientNumber); //stored as a string, comma delimited
        } else {
            // Initiate localStorage and add project ID
            let ingredientNumber = 1;
            localStorage.setItem(localStoreName, ingredientNumber);
        }
    } else {
        // no localStorage
        return alert("Your browser does not support localStorage use for this domain at this time. This will effect how your dashboard looks when you reopen The Project Management Dashboard in a new browser window.");
    }
}

/* Check to make sure localStorage is usuable in the browser */
/* CODE REUSE - localStorage Check MDN, see README.md  */
function storageAvailable(type) {
    var storage;
    try {
        storage = window[type];
        var x = '__storage_test__';
        storage.setItem(x, x);
        storage.removeItem(x);
        return true;
    }
    catch(e) {
        return e instanceof DOMException && (
            // everything except Firefox
            e.code === 22 ||
            // Firefox
            e.code === 1014 ||
            // test name field too, because code might not be present
            // everything except Firefox
            e.name === 'QuotaExceededError' ||
            // Firefox
            e.name === 'NS_ERROR_DOM_QUOTA_REACHED') &&
            // acknowledge QuotaExceededError only if there's something already stored
            (storage && storage.length !== 0);
    }
}