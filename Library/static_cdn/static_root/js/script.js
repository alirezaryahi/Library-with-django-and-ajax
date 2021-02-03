$(document).ready(function () {
    $('.ui.dropdown').dropdown()

    $("[name='active']").submit(function (e) {
        e.preventDefault()
        const url = $(this).attr('action')
        const user_id = parseInt($(this).find("[name='user_id']").attr('value'))
        const checkbox = $(this).find(`input[type=checkbox]`).prop('checked');
        const token = $(this).find("[name='token']").attr('value')
        if (checkbox) {
            $(this).find(`input[type=checkbox]`).prop('checked', false);
        } else {
            $(this).find(`input[type=checkbox]`).prop('checked', true);
        }
        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': token,
                'user_id': user_id,
            },
            success: function (res) {
                console.log("Success!", res);
            },
            error: function (err) {
                console.log('error', err)
            }
        })
    })
})