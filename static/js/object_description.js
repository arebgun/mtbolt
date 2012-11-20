$(document).ready(function () {

    $('form').submit(function () {
        $('.error').remove();

        $('.object_binding').each(function () {
            if (isNaN(this.value)) {
                $(this).after('<div class="error">Please select an object</div>');
            }
        });

        if ($('.error').length > 0) {
            alert('Please answer all questions correctly.');
            return false;
        }
    });
});
