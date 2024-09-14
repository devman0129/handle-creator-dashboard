$(document).ready(function () {
  $(".navbar-nav .nav-item .nav-link:link").removeClass("active");

  let path = strimSlash(location.pathname);
  path = path == "" ? "home" : path;
  $(".nav-link.nav-" + path).addClass("active");
});

const strimSlash = (path) => {
  while (path[0] == "/") {
    path = path.slice(1);
  }
  while (path[path.length - 1] == "/") {
    path = path.slice(0, path.length - 1);
  }
  return path;
};
