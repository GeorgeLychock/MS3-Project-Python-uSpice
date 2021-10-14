$(document).ready(function () {
    $(".tooltipped").tooltip();
});

function addIngredient() {
    var passIngredientData = {
        name: "",
        quantity: "",
        measure: "",
        id: ""
    };
        //Add a unique-ish ingredient ID to the data
        passIngredientData.id = "ing" + Math.floor(Math.random()*10000000);
        //grab input form data from modal
        passIngredientData.name = document.getElementById("ingredientForm").elements.namedItem("ingredient_region_1_name").value;
        passIngredientData.quantity = document.getElementById("ingredientForm").elements.namedItem("ingredient_region_1_quantity").value;
        passIngredientData.measure = document.getElementById("ingredientForm").elements.namedItem("ingredient_region_1_measure").value;

    return $("#ingredient_region").append(buildIngredientForm(passIngredientData));
}

function buildIngredientForm(i) {
    let ing = i;

    return `
    <div class="row">
        <div class="col-4 us-ingredient-name">
            <label for="ingredient_name" class="form-label">Ingredient Name</label>
            <input class="" type="text" id="ingredient_name" name="ingredient_name" value="${ing.name}">
        </div>
        <div class="col-4 us-ingredient-quantity">
            <label for="ingredient_quantity" class="form-label">Quantity</label>
            <input id="ingredient_quantity" name="ingredient_quantity" class="" value="${ing.quantity}">
        </div>
        <div class="col-2 us-ingredient-measure">
            <label for="ingredient_measure" class="form-label">Measure</label>
            <input id="ingredient_measure" name="ingredient_measure" class="" value="${ing.measure}">
        </div>
        <!-- Remove the ingredient from the form -->
        <div class="col-2">
            <button type="button" class="us-ingredient-addbtn" onclick="removeIngredient(${ing.id})">+ Remove</button>
        </div>
    </div>
    `
}

function buildIngredientForm2(i) {
    let inc = i;

    return `
    <div class="ingredient_region${inc}">
        <label for="ingredient_region${inc}_name" class="form-label">Ingredient Name</label>
        <input class="" id="ingredient_region${inc}_name" name="ingredient_region${inc}_name">
        <label for="ingredient_region${inc}_measure" class="form-label">Measure</label>
        <select id="ingredient_region${inc}_measure" name="ingredient_region${inc}_measure" class="form-select us-dropdown">
            <option selected>Choose...</option>
            {% for measure in measures %}
            <option>{{ measure.measure_name }}</option>
            {% endfor %}
        </select>
    </div>
    `
}

function addIngredientStorage(iNum) {
    var localStoreName = "ingredientNumber";
    var ingredientNum = iNum;

    // Check if localStorage is enabled
    if (storageAvailable('localStorage')) {
        // We can use localStorage, check if localStorage var has been initiated
        if (localStorage.getItem(localStoreName)) {
            // Add widget ID to the localStorage string and store
            let ingredientNumToSave = localStorage.getItem(localStoreName).split(','); //returns a string, comma delimited, convert to array
            ingredientNumToSave.push(ingredientNum);
            localStorage.setItem(localStoreName, ingredientNumToSave); //stored as a string, comma delimited
        } else {
            // Initiate localStorage and add project ID
            let ingredientNumToSave = [];
            ingredientNumToSave.push(ingredientNum);
            localStorage.setItem(localStoreName, ingredientNumToSave);
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