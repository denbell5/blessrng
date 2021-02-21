function copyToClipboardFrom(resultContainerId, resultElementTag) {
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