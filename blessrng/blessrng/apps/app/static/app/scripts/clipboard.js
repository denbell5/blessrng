function copyToClipboardFrom(clickedElement, resultContainerId, resultElementTag) {
    const oldIcon = clickedElement.getElementsByTagName('svg')[0];

    const icon = oldIcon.cloneNode(true);
    oldIcon.parentNode.replaceChild(icon, oldIcon);
    icon.classList.add('copy-icon-mouse-up');

    const resultContainer = document.getElementById(resultContainerId);
    var text = '';
    var upperCaseTagName = resultElementTag.toUpperCase();
    resultContainer.childNodes.forEach(el => {
        if (el.tagName == upperCaseTagName) {
            text += el.innerHTML + '\n';
        }
    });
    var slicedText = text.slice(0, text.length - 1);
    navigator.clipboard.writeText(slicedText);
}