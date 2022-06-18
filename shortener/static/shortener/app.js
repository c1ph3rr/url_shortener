function copyFunction() {
    var text = document.getElementById('copy-url');
    var button = document.getElementById('copy-button')
    text.select();
    text.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(text.value);
    button.innerHTML = 'Copied!'
  }