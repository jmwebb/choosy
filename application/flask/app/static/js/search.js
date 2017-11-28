function appendFilter(value, isFirstQuestion, alias) {
	var queryChar = '';
	if (isFirstQuestion) {
		queryChar = '?';
	} else {
		queryChar = '&';
	}
	window.location.href += queryChar + alias + '=' + value;
}

function putSelection(id, username, yelp_url) {
	$.ajax({
        type: 'GET',
        url: "/api/user/" + username + "/history/" + id
    });
	window.location = '/' + username + '/search';
	window.open(yelp_url, '_blank');
}