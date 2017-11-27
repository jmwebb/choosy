function appendFilter(value, isFirstQuestion, alias) {
	var queryChar = '';
	if (isFirstQuestion) {
		queryChar = '?';
	} else {
		queryChar = '&';
	}
	window.location.href += queryChar + alias + '=' + value;
}