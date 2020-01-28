var cyberStoryList = document.getElementById("list");

var cyberListItems = cyberStoryList.getElementsByTagName("a");

for(a of  cyberListItems){
  a.addEventListener('click', function(){
    if(this.classList.contains('list_active')){
      this.classList.remove("list_active");
    } else {
      this.classList.add("list_active");
    }
  });
}
