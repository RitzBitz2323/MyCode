var list = [];
//var listString = "";
var i = 0;
var name = "";
var roll = "";
function addCreature(){
  var cname = document.getElementById('name').value;
  var croll = document.getElementById('roll').value;
  var creature = new genCreature(cname,croll);
  console.log(creature);
  list.splice(i, 0, creature);
  console.log(list);
  i = i + 1;
  //list.sort(compare);
  /*
  for (var i = 0; i < list.length; i++) {
      listString = listString + list[i].cname +" " + list[i].croll + "<br>";
  }
  */

  document.getElementById("output").innerHTML = JSON.stringify(list);

}


function sortArray(){
  list.sort(function(a, b){return a - b});
}

function genCreature(cname,croll){
name = cname;
roll = croll;
}
/*
function compare(a, b) {
  const creatureA = a.roll;
  const creatureB = b.roll;

  let comparison = 0;
  if (creatureA > creatureB) {
    comparison = 1;
  } else if (creatureA < creatureB) {
    comparison = -1;
  }
  return comparison;
}*/
