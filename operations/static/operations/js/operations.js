// calculate price = package * quantity.
function calcPrices() {
    elems = document.querySelectorAll('input[id^="id_package_"]');

    total_price = 0.0
    for (var i = 0, len = elems.length; i < len; i++) {
        pkg_price = _calcTotalPackagePrice(elems[i].id);
        //update label next to quantity input box
        document.getElementById(elems[i].id + "_label").innerHTML = "$" + pkg_price.toFixed(2);

        total_price += pkg_price;
    }

    //update total sales price input box
    document.getElementById('id_sales_price').value = total_price.toFixed(2);

    //update tax input box
    tax_rate = Number(document.getElementById('id_tax_rate').value);
    document.getElementById('id_tax').value = (total_price * tax_rate).toFixed(2);

    //online store charge
    calcOnlineStoreCharge()
}

function _calcTotalPackagePrice(id_package) {
    qty = document.getElementById(id_package).value;
    price = document.getElementById(id_package + "_price").innerHTML;
    price = price.replace("$", "");

    return Number(price) * Number(qty);
}

function calcOnlineStoreCharge() {
    chkbox = document.getElementById('id_online_store_charge_chkbox');

    if (chkbox.checked) {
        total_price = document.getElementById('id_sales_price').value;
        prct = document.getElementById('id_online_store_prct').value;
        markup = document.getElementById('id_online_store_markup').value;

        //calculate
        charge = (Number(total_price) * Number(prct) + Number(markup)).toFixed(2);
        document.getElementById('id_online_store_charge').value = charge;
    } else {
        document.getElementById('id_online_store_charge').value = null;
    }
}

function submitOrder() {
    // get all package elements
    elems = document.querySelectorAll('input[id^="id_package_"]');
    //create two arrays of package_ids and respective qty
    packages = []
    quantities = []
    for (var i = 0, len = elems.length; i < len; i++) {
        packages.push(elems[i].name);
        quantities.push(elems[i].value)
    }
    //set on hidden fields
    document.getElementById('id_ids_packages').value = packages;
    document.getElementById('id_quantities').value = quantities;

    //all good to submit
    return true;
}

// on load of shopping list page, check selected dishes (if any)
function checkSelectedDishes() {
    if (document.getElementById('id_selected_dishes') == null) {
        return true;
    }
    selected_dish_ids = document.getElementById('id_selected_dishes').value;
    if (selected_dish_ids != null && selected_dish_ids.length > 0) {
        selected_dish_ids = selected_dish_ids.split(",");
        for (var i = 0; i < selected_dish_ids.length; i++) {
            document.getElementById('id_dish_' + selected_dish_ids[i]).checked = true;;
        }
    }
}

function colorCodeOrderStatus() {
    elems = document.querySelectorAll('td[id="id_order_status"]');
    for (var i = 0, len = elems.length; i < len; i++) {
        //color code Green if COMPLETE
        if (elems[i].innerHTML == "COMPLETED") {
            elems[i].style="color:#09ba00";
        }
    }
}