var app = new Vue({
  el: '#app',
  data: {
    content: {},
    loading: true
  },
  methods: {
    format: function(list) {
      return list != null ? list.map(i => `<div>${i}</div>`).join("") : null;
    },
    special_format: function(list) {
      if(list == null) {
        return null;
      }
      return list.map(i => {
        var style = "primary";
        var text = i;
        if(text[0] == "!") {
            style = "unacceptable";
            text = text.substring(1);
        } else if(text[0] == "^") {
          style = "secondary";
          text = text.substring(1);
        }
        return `<div class="${style}">${text}</div>`;
      }).join("");
    }
  }
});

let url = "https://gitcdn.link/repo/davidluzgouveia/kanji-data/master/kanji-jouyou.json";
$.getJSON(url, data => {
    app.content = data;
    app.loading = false;
});