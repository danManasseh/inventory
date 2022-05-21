function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(events) {
    if (!events.target.matches('.dropbtn')) {
      var navdrop = document.getElementsByClassName("dropdown-content");
      var j;
      for (j = 0; j < navdrop.length; j++) {
        var dropdownOpen = navdrop[j];
        if (dropdownOpen.classList.contains('show')) {
          dropdownOpen.classList.remove('show');
        }
      }
    }
  }
  

  function myFunction1() {
    document.getElementById("dashdrop").classList.toggle("shows");
  }
  
  // Close the dropdown if the user clicks outside of it
  // window.onclick = function(event) {
  //   if (!event.target.matches('.dropbtns')) {
  //     var dropdowns = document.getElementsByClassName("dashdrop-content");
  //     var i;
  //     for (i = 0; i < dropdowns.length; i++) {
  //       var openDropdown = dropdowns[i];
  //       if (openDropdown.classList.contains('shows')) {
  //         openDropdown.classList.remove('shows');
  //       }
  //     }
  //   }
  // }