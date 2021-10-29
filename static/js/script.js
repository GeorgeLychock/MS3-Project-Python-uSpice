$(document).ready(function () {
    $(".tooltipped").tooltip();
    buildBannerButton("back");
    buildBannerButton("forward");
});

//Confirm deletion
function confirmDeleteRecipe() {
    var txt ="Are you sure you want to delete this recipe permanently?";
    confirm(txt);
}

//Confirm rating
function ratingConfirm() {
    let txt = "Thank you for submitting your rating!";
    confirm(txt);
}

function getLocalStorageArray(lsName) {
    if (localStorage.getItem(lsName)) {
        var storedPaths = localStorage.getItem(lsName).split(',');
        return storedPaths;
    }
}

function clearLocalStorage(lsName) {
    localStorage.clear(lsName);
}

function storeClickPath(path) {
    // Add url click path localStorage
    var lsName = "clickPathLocalStorage";
    var addPath = path;
    var storedPaths;
    if (localStorage.getItem(lsName)) {
        storedPaths = getLocalStorageArray(lsName);
        // Limit number of stored path clicks to 10
        if (storedPaths.length >= 10) {
            // remove first path item and add new path
            storedPaths.shift();
            storedPaths.push(addPath);
        } else {
            storedPaths.push(addPath);
            updateCurrentIndex("up");
        }
    } else {
        storedPaths = [];
        storedPaths.push(addPath);
        updateCurrentIndex();
    }
    localStorage.setItem(lsName, storedPaths);

    storedPaths = getLocalStorageArray(lsName);
}

function updateCurrentIndex(direction) {
        // Track current click path index in localStorage
        var lsName = "clickPathIndexLocalStorage";
        var lsName2 = "clickPathLocalStorage";
        var storedIndex;
        if (localStorage.getItem(lsName)) {
            storedIndex = parseInt(localStorage.getItem(lsName));

            if (direction == "up") {
                storedIndex = storedIndex + 1;
                localStorage.setItem(lsName, storedIndex);
            } else if (direction == "down") {
                if (storedIndex == 0) {
                    clearLocalStorage(lsName);
                    clearLocalStorage(lsName2);
                } else {
                    storedIndex = storedIndex - 1;
                    localStorage.setItem(lsName, storedIndex);
                }
            }
        } else {
            storedIndex = 0;
            localStorage.setItem(lsName, storedIndex);
        }
}

function buildBannerButton(direction) {

    var lsName = "clickPathIndexLocalStorage";
    var lsName2 = "clickPathLocalStorage";
    var urlPath;
    var iconDirection;
    var backBtnID;

    if (localStorage.getItem(lsName)) {
        var storedIndex = parseInt(localStorage.getItem(lsName));
        var storedPaths = getLocalStorageArray(lsName2);

        if (direction == "back") {
            backBtnID = "backButton";
            if (storedIndex != 0) {
                urlPath = storedPaths[storedIndex];
            } else {
                urlPath = storedPaths[0];
            }

            iconDirection = "left";
        } else if (direction == "forward") {
            backBtnID = "forwardButton";
            urlPath = storedPaths[storedIndex+1];
            iconDirection = "right";
        }
        return $("#" + backBtnID).html(`<a class="nav-link us-padding-0" onclick="updateCurrentIndex('down')" href="${urlPath}"><i class="bi bi-chevron-${iconDirection} us-user-menu-link-01 us-i-color-02"></i></a>`);
    } else {
        return $("#" + backBtnID).html(`<a class="nav-link us-padding-0"><i class="bi bi-chevron-${iconDirection} us-user-menu-link-01 us-i-color-02a"></i></a>`);
    }
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
    //grab input form data from input fields
    passIngredientData.name = document.getElementById("ingredientForm").elements.namedItem("ingredient_region_1_name").value;
    passIngredientData.quantity = document.getElementById("ingredientForm").elements.namedItem("ingredient_region_1_quantity").value;
    passIngredientData.measure = document.getElementById("ingredientForm").elements.namedItem("ingredient_region_1_measure").value;

    //Clear form
    var x = document.getElementById("ingredient_region_1_name");
    x.value = "Choose...";
    x = document.getElementById("ingredient_region_1_quantity");
    x.value = "0";
    x = document.getElementById("ingredient_region_1_measure");
    x.value = "Choose...";

    return $("#ingredient_region").append(buildIngredientForm(passIngredientData));
}

function removeIngredient(iID) {
    elementID = iID;
    //remove panel
    return $("#" + elementID).remove();

}

function buildIngredientForm(i) {
    let ing = i;

    return `
    <div class="row us-ingredient-row" id="${ing.id}">
        <input name="ingredient_id" value="${ing.id}" hidden readonly>
        <input class="col-5 us-ingredient-name" name="ingredient_name" value="${ing.name}" readonly>
        <input class="col-2 us-ingredient-quantity" name="ingredient_quantity" value="${ing.quantity}" readonly>
        <input class="col-2 md-col-3 us-ingredient-measure" name="ingredient_measure" value="${ing.measure}" readonly>
        <!-- Remove the ingredient from the form -->
        <div class="col-1">
            <button type="button" class="us-ingredient-delbtn" onclick="removeIngredient('${ing.id}')">Remove</button>
        </div>
    </div>
    `;
}

function addToLocalStorage(storeValue, lsName) {
    var localStoreName = lsName;
    var valueToSave = storeValue;

    // Check if localStorage is enabled
    if (storageAvailable('localStorage')) {
        // We can use localStorage, check if localStorage var has been initiated
        if (localStorage.getItem(localStoreName)) {
            // Add value to the localStorage string and store
            let valuesSaved = localStorage.getItem(localStoreName).split(','); //returns a string, comma delimited, convert to array
            valuesSaved.push(valueToSave);
            localStorage.setItem(localStoreName, valuesSaved); //stored as a string, comma delimited
        } else {
            // Initiate localStorage and add value
            let valuesSaved = [];
            valuesSaved.push(valueToSave);
            localStorage.setItem(localStoreName, valuesSaved);

            valuesSaved = localStorage.getItem(localStoreName).split(',');
        }
    } else {
        // no localStorage
        return alert("Your browser does not support localStorage use for this domain at this time. This will effect how your dashboard looks when you reopen The Project Management Dashboard in a new browser window.");
    }
}

function removeFromLocalStorage(storeValue, lsName) {

    var localStoreName = lsName;
    var valueToDel = storeValue;

    if (localStorage.getItem(localStoreName)) {
        let savedValues = localStorage.getItem(localStoreName).split(',');
        let delValueIndex = savedValues.indexOf(valueToDel);
        var removedWidgetIDs = savedValues.splice(delValueIndex, 1);

        localStorage.setItem(localStoreName, savedValues);

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