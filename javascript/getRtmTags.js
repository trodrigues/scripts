(function(){
var tagList={}, tags=document.getElementById("tasks").getElementsByClassName("xtd_tag");
for(var i=0, l=tags.length; i<l; i++){
    var inTags=tags[i].innerHTML.split(",");
    for(var j=0, lj=inTags.length; j<lj; j++){
        var tag = inTags[j].replace(/^\s+|\s+$|\n+$/g, '');
        (tag in tagList) ? tagList[tag]++ : tagList[tag]=1;
    }
}
var str="";
for(var i in tagList){
    str += i+": "+tagList[i]+"\n";
}
alert(str);
}());
