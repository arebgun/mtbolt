$(document).ready(function () {

    copy_desc = function() {
        target_id = $(this).attr('id').split('_')[0] + '_dsc_lbl'
        $('#'+target_id).text(this.value + ' is')
    };

    $('.object_description').change(copy_desc).blur(copy_desc).keyup(copy_desc);

    $('form').submit(function () {
        $('.error').remove();

        $('.object_description, .location_description').each(function () {
            if (/^\s*$/.test(this.value)) {
                $(this).after('<div class="error">This field is required.</div>');
            }
            if (/\d/.test(this.value)) {
                $(this).after('<div class="error">No digits allowed. Do not use object numbers to refer to objects.</div>');
            }
        });

        if ($('.error').length > 0) {
            alert('Please answer all questions correctly.');
            return false;
        }
    });
});
