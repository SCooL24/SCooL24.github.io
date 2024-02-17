{% include partials/header.html %}

  {% assign this_room = page %}

  <h1 class="display-5 mb-3">
    {% if page.title %}
      {{ page.title }}
    {% else %}
      {{ site.data.lang[site.conference.lang].location.title | default: "Rooms" }}
    {% endif %}
  </h1>

  {% assign this_room = page %}

  {% unless site.conference.rooms.hide %}
    {% include partials/navbar_rooms.html %}
  {% endunless %}

  {{ content }}

{% include partials/footer.html %}
