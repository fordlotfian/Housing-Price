//DESIGN FROM THIS DRIBBLE SHOT: https://dribbble.com/shots/3209056-Synthwave

var xmlns = "http://www.w3.org/2000/svg",
  xlinkns = "http://www.w3.org/1999/xlink",
  select = function(s) {
    return document.querySelector(s);
  },
  selectAll = function(s) {
    return document.querySelectorAll(s);
  }
  

TweenMax.set('svg', {
  visibility: 'visible'
})

var tl = new TimelineMax();


ScrubGSAPTimeline(tl);