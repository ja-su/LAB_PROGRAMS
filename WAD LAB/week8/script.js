function validation() {
    var userid = document.form.user.value;
    var password = document.form.pass.value;
    var uname = document.form.uname;
    var addr = document.form.address;
    var count = document.form.country;
    var zipcode = document.form.zip;
    var em = document.form.email;
    var eng = document.form.englang;
    var noneng = document.form.nonenglang;
    var x = 0;
    var y = 0;
    var letter = /^[A-Za-z]+$/;
    var letterNumber = /^[0-9a-zA-Z]+$/;
    var number = /^[0-9]+$/;
    var mailform = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    //check userid
    if (userid.length == 0 || userid.length < 5 || userid.length > 12) {
        alert("User ID should not be empty and should be min of 5 characters and max of 12 characters only");
        return false;
    }

    //check password
    if (password.length == 0 || password.length < 7 || password.length > 12) {
        alert("Password should not be empty and  be min of 7 characters and max of 12 characters only");
        return false;
    }
    //check username
    if (!uname.value.match(letter)) {
        alert("Name must contain alphabets only!!");
        return false;
    }
    //check address
    if (!addr.value.match(letterNumber)) {
        alert("Address must contain alphabets and numbers only!!");
        return false;
    }
    //check country
    if (count.value == "Default") {
        alert("Select any country!!");
        return false;
    }
    //check zipcode
    if (!zipcode.value.match(number)) {
        alert("Only numbers are allowed!!");
        return false;
    }
    //check email
    if (!em.value.match(mailform)) {
        alert("Enter a valid email id!!");
        return false;
    }
    //check gender 2.0
    if ((form.sex[0].checked == false) && (form.sex[1].checked == false)) {
        alert("Select either male or female!!");
        return false;
    }
    //check language
    if (y != 0 || !eng.checked && !noneng.checked) {
        alert("Select any language!!");
        return false;
    }
}