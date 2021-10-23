$(document).ready(function () {
    $(".tooltipped").tooltip();
});

function clearLocalStorage(lsName) {
    localStorage.clear(lsName);
}

function ratingConfirm() {
    let txt = "Thank you for submitting your rating!";
    confirm(txt)
}

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

    // Add ingredient ID to localStorage
    lsName = "ingredientIDLocalStorage";
    addToLocalStorage(passIngredientData.id, lsName);

    return $("#ingredient_region").append(buildIngredientForm(passIngredientData));
}

function removeIngredient(iID) {
    // Remove ingredient ID from localStorage and remove ingredient from user input form
    console.log(iID);
    lsName = "ingredientIDLocalStorage";
    elementID = iID;
    removeFromLocalStorage(elementID, lsName);
    //remove panel
    return $("#" + elementID).remove();

}

function buildIngredientForm(i) {
    let ing = i;

    return `
    <div class="row us-ingredient-row" id="${ing.id}">
        <div class="col-5 us-ingredient-name">
            <label for="ingredient_name" class="form-label">Ingredient Name</label>
            <input class="us-ingredient-name"" type="text" id="ingredient_name" name="ingredient_name" value="${ing.name}">
        </div>
        <div class="col-3 us-ingredient-quantity">
            <label for="ingredient_quantity" class="form-label">Quantity</label>
            <input id="ingredient_quantity" name="ingredient_quantity" class="" value="${ing.quantity}">
        </div>
        <div class="col-3 us-ingredient-measure">
            <label for="ingredient_measure" class="form-label">Measure</label>
            <input id="ingredient_measure" name="ingredient_measure" class="" value="${ing.measure}">
        </div>
        <!-- Remove the ingredient from the form -->
        <div class="col-1">
            <button type="button" class="us-ingredient-addbtn" onclick="removeIngredient('${ing.id}')">Remove</button>
        </div>
    </div>
    `
}

function addToLocalStorage(storeValue, lsName) {
    var localStoreName = lsName;
    var valueToSave = storeValue;

    // Check if localStorage is enabled
    if (storageAvailable('localStorage')) {
        // We can use localStorage, check if localStorage var has been initiated
        if (localStorage.getItem(localStoreName)) {
            // Add widget ID to the localStorage string and store
            let valuesSaved = localStorage.getItem(localStoreName).split(','); //returns a string, comma delimited, convert to array
            valuesSaved.push(valueToSave);
            localStorage.setItem(localStoreName, valuesSaved); //stored as a string, comma delimited
        } else {
            // Initiate localStorage and add project ID
            let valuesSaved = [];
            valuesSaved.push(valueToSave);
            localStorage.setItem(localStoreName, valuesSaved);

            valuesSaved = localStorage.getItem(localStoreName).split(',');
            console.log("Add to LS" + valuesSaved);
        }
    } else {
        // no localStorage
        return alert("Your browser does not support localStorage use for this domain at this time. This will effect how your dashboard looks when you reopen The Project Management Dashboard in a new browser window.");
    }
}

function removeFromLocalStorage(storeValue, lsName) {

    var localStoreName = lsName;
    var valueToDel = storeValue;

    console.log(localStoreName);
    console.log(valueToDel);

    if (localStorage.getItem(localStoreName)) {
        let savedValues = localStorage.getItem(localStoreName).split(',');
        let delValueIndex = savedValues.indexOf(valueToDel);
        var removedWidgetIDs = savedValues.splice(delValueIndex, 1);

        localStorage.setItem(localStoreName, savedValues);

        valuesSaved = localStorage.getItem(localStoreName).split(',');
        console.log("Remaining ingredients" + valuesSaved);

    } // else capture error, if needed
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