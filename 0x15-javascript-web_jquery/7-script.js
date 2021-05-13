//Fetches the character name from a URL
//The name must be displayed in the HTML tag DIV#character
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
