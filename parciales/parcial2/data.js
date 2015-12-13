
var types = ['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L'];
var zonas = ['1','2','3', '4', '5', '6', '7'];

types.forEach(function (item) {
  $.extend(all, getItems('.item.Sector.'+item+'S', item+'S'));
  $.extend(all, getItems('.item.Sector.'+item+'N', item+'N'));
});

var globals = [];
function getItems(finder,type) {
  var r = {};
  var a = $(finder);
  a.each(function(a,b){
    c = $(b).text().trim();
    r[c] = {type:type};
    globals.push({name:c, type:type});
  });
  return r;
}

function rellenar(id,letra,array,items){
  var a = {};
  var arraylist = array || types;
  arrayItem = items || arraylist;
  arraylist.forEach(function(t,i){
    var x = i + 1;
    var values = $('#'+id+' tr td.row_'+x);

    var h = a[t+letra] = {};

    values.each(function (l,m) {
      if(l > 0){
       var ri = l - 1;
       var value = $(m).text().trim();

       if(!items) h[ arrayItem[ri] + letra ] = value;
       else {
         h[ arrayItem[ri] + 'N' ] = value;
         h[ arrayItem[ri] + 'S' ] = value;
         var res_1 = all[ arrayItem[ri] + 'N' ];
         var res_2 = all[ arrayItem[ri] + 'S' ];
         if(res_1){
           res_1[t+letra] = value;
         }
         if(res_2){
           res_2[t+letra] = value;
         }
        //  all[ arrayItem[ri] + 'S' ][t+letra] = value;
        //  all[ arrayItem[ri] + 'N' ][t+letra] = value;
       }

      }
    });

  });
  return a;
}

for(var a in zonas){
  for (var item in zonas[a]) {
    all[a][item] = zonas[a][item];
  }
}
