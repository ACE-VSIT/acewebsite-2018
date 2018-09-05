function getInternetExplorerVersion() {
    let test = -1;
    if (navigator.appName === 'Microsoft Internet Explorer') {
        let ua = navigator.userAgent;
        let re = new RegExp("MSIE ([0-9]{1,}[\.0-9]{0,})");
        if (re.exec(ua) !== null)
            test = parseFloat(RegExp.$1);
    }
    else if (navigator.appName === 'Netscape') {
        let ua = navigator.userAgent;
        let re = new RegExp("Trident/.*rv:([0-9]{1,}[\.0-9]{0,})");
        if (re.exec(ua) !== null)
            test = parseFloat(RegExp.$1);
    }
    return test;
}
if (getInternetExplorerVersion() !== -1) {
    document.body.innerHTML = (
        "<div class=\"ie-support\">\n" +
        " <p class='ie'>\n" +
        " The browser you are using is not supported.</p>\n" +
        " <p>Try one of them <a class='iered' href='https://www.google.com/chrome/browser/desktop/index.html'>Google\n" +
        " Chrome</a>,\n" +
        " <a class='iered' href='https://www.mozilla.org/en-US/firefox/new/'>Mozilla Firefox</a>,\n" +
        " <a class='iered' href='http://www.opera.com/download'>Opera</a>\n" +
        " </p>\n" +
        "</div>"
    );
}