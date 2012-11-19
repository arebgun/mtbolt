$(document).ready(function () {

    $('form').submit(function () {
        $('.error').remove();

        /* insert validation here */
        /*
        $('.object_description, .location_description').each(function () {
            if (/^\s*$/.test(this.value)) {
                $(this).after('<div class="error">This field is required.</div>');
            }
            if (/\d/.test(this.value)) {
                $(this).after('<div class="error">No digits allowed. Do not use object numbers to refer to objects.</div>');
            }
        });
        */

        if ($('.error').length > 0) {
            alert('Please answer all questions correctly.');
            return false;
        }
    });
});
