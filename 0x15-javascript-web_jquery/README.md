# JavaScript - Web jQuery

This project served as preparation for learning how to manipulate the DOM with jQuery before integrating it into our AirBnB project.

## Tests ✔️

* [Tests](./tests): This folder contains HTML files for testing DOM manipulation scripts.

## Tasks 📃

* **0. No jQuery**
  * [0-script.js](./0-script.js): This JavaScript script utilizes `document.querySelector` to update the text color of the HTML tag `HEADER` to red (`#ff0`).

* **1. With jQuery**
  * [1-script.js](./1-script.js): This JavaScript script utilizes jQuery to update the text color of the HTML tag `HEADER` to red (`#ff0`).

* **2. Click and turn red**
  * [2-script.js](./2-script.js): This JavaScript script utilizes jQuery to update the text color of the HTML tag `HEADER` to red (`#ff0`) when the user clicks on the tag `DIV#red_header`.

* **3. Add `.red` class**
  * [3-script.js](./3-script.js): This JavaScript script utilizes jQuery to add the class `.red` to the HTML tag `HEADER` when the user clicks on the tag `DIV#red_header`.

* **4. Toggle classes**
  * [4-script.js](./4-script.js): This JavaScript script utilizes jQuery to toggle the class of the HTML tag `HEADER` between `.red` and `.green` when the user clicks on the tag `DIV#red_header`.

* **5. List of elements**
  * [5-script.js](./5-script.js): This JavaScript script utilizes jQuery to add a `LI` element to a list when the user clicks on the tag `DIV#add_item`. It adds the element `<li>Item</li>` to `UL.my_list`.

* **6. Change the text**
  * [6-script.js](./6-script.js): This JavaScript script utilizes jQuery to update the text of the HTML tag `HEADER` to "New Header!!!" when the user clicks on the tag `DIV#update_header`.

* **7. Star Wars character**
  * [7-script.js](./7-script.js): This JavaScript script utilizes jQuery to fetch the Star Wars API `https://swapi.co/api/people/5/?format=json` and display the name in the HTML tag `DIV#character`.

* **8. Star Wars movies**
  * [8-script.js](./8-script.js): This JavaScript script utilizes jQuery to fetch and list all movie titles from the Star Wars API `https://swapi.co/api/films/?format=json`. The titles are listed in the HTML tag `UL#list_movies`.

* **9. Say Hello!**
  * [9-script.js](./9-script.js): This JavaScript script utilizes jQuery to fetch and display how to say "Hello" in French using the API `https://fourtonfish.com/hellosalut/?lang=fr`. It displays the translation in the HTML tag `DIV#hello`. This script works when imported in the `HEAD` tag.

* **10. No jQuery - document loaded**
  * [100-script.js](./100-script.js): This JavaScript script utilizes `document.querySelector` to update the text color of the HTML tag `HEADER` to red (`#ff0`). This script works when imported in the `HEAD` tag.

* **11. List, add, remove**
  * [101-script.js](./101-script.js): This JavaScript script utilizes jQuery to add, remove, and clear `LI` elements from a list based on user click input. It adds a new element when the user clicks `DIV#add_item` and removes the last element when the user clicks `DIV#remove_item`. It also clears all elements when the user clicks `DIV#clear_list`. This script works when imported in the `HEAD` tag.

* **12. Say hello to everybody!**
  * [102-script.js](./102-script.js): This JavaScript script utilizes jQuery to fetch and display how to say "Hello" in a given language using the API `https://www.fourtonfish.com/hellosalut/hello/`. It fetches the translation for the language entered in the HTML tag `INPUT#language_code` and displays the translation in the HTML tag `DIV#hello`. This script works when imported in the `HEAD` tag.

* **13. And press ENTER**
  * [103-script.js](./103-script.js): This JavaScript script utilizes jQuery to fetch and display how to say "Hello" in a given language using the API `https://www.fourtonfish.com/hellosalut/hello/`. It is similar to [102-script.js](./102-script.js) but the translation is fetched when either the user clicks on the HTML tag `INPUT#btn_translate` or presses `ENTER` when hovering over the tag `INPUT#language_code`.

