(function(){

    var button = document.getElementById('cn-button'),
      wrapper = document.getElementById('cn-wrapper'),
      overlay = document.getElementById('cn-overlay');
  
    //open and close menu when the button is clicked
    var open = false;
    button.addEventListener('click', handler, false);
    button.addEventListener('focus', handler, false);
    wrapper.addEventListener('click', cnhandle, false);
  
    function cnhandle(e){
      e.stopPropagation();
    }
  
    function handler(e){
      if (!e) var e = window.event;
      e.stopPropagation();//so that it doesn't trigger click event on document
  
        if(!open){
          openNav();
        }
      else{
          closeNav();
        }
    }
    function openNav(){
      open = true;
        button.innerHTML = "-";
        classie.add(overlay, 'on-overlay');
        classie.add(wrapper, 'opened-nav');
    }
    function closeNav(){
      open = false;
      button.innerHTML = "+";
      classie.remove(overlay, 'on-overlay');
      classie.remove(wrapper, 'opened-nav');
    }
    document.addEventListener('click', closeNav);
  
  })();
//The JavaScript for the second demo is similar to the previous one, except that we customize it for this case:
  (function(){

    var button = document.getElementById('cn-button'),
      wrapper = document.getElementById('cn-wrapper');
  
      //open and close menu when the button is clicked
    var open = false;
    button.addEventListener('click', handler, false);
    button.addEventListener('focus', handler, false);
  
    function handler(){
      if(!open){
        this.innerHTML = "Close";
        classie.add(wrapper, 'opened-nav');
      }
      else{
        this.innerHTML = "Menu";
      classie.remove(wrapper, 'opened-nav');
      }
      open = !open;
    }
    function closeWrapper(){
      classie.remove(wrapper, 'opened-nav');
    }
  
  })();