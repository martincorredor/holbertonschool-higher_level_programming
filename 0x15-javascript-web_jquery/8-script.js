//Fetches and lists the title for all movies by using an URL
//All movie titles must be list in the HTML tag UL#list_movies
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const film of data.results) {
    $('#list_movies').append(`<li>${film.title}</li>`);
  }
});
