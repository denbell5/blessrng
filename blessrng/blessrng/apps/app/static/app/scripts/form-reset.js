function resetForm(clickedElement, id) {
    const form = document.getElementById(id);
    if (!form) {
        return;
    }

    const oldIcon = clickedElement.getElementsByTagName('svg')[0];
    const icon = oldIcon.cloneNode(true);
    oldIcon.parentNode.replaceChild(icon, oldIcon);
    icon.classList.add('refresh-icon-mouse-up');

    const controls = form.querySelectorAll('input, textarea');
    controls.forEach(el => {
        if (el.type != 'hidden' && el.type != 'submit') {
            el.value = '';
        }
    });
}