function resetForm(id) {
    const form = document.getElementById(id);
    if (!form) {
        return;
    }

    const controls = form.querySelectorAll('input, textarea');
    controls.forEach(el => {
        if (el.type != 'hidden' && el.type != 'submit') {
            el.value = '';
        }
    });
}