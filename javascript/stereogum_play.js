javascript:(function(){
	function showPlayer(filePath){
		if(typeof window.BMPlayerWindow !== "undefined"){
			window.BMPlayerWindow.parentNode.removeChild(
				window.BMPlayerWindow);
		}
		var p = document.createElement("div");
		p.style.position = "absolute";
		p.style.top ="10px";
		p.style.left ="10px";
		p.style.zIndex = 100000;
		var audio = document.createElement("audio");
		audio.controls = true;
		audio.src = filePath;
		audio.load();
		audio.play();
		p.appendChild(audio);
		window.BMPlayerWindow = p;
		document.body.appendChild(window.BMPlayerWindow);
	}
	if(typeof window.BMPlayer === "undefined"){
		window.BMPlayer = {};
	}
	var mp3files = document.getElementsByClassName("mp3inline");
	var counter;
	for(var i=0, li=mp3files.length; i<li; i++){
		var f = mp3files[i];
		for(var j=0, lj=f.childNodes.length; j<lj; j++){
			var c=f.childNodes[j];
			if(c.nodeType === 1){
				if(c.tagName.toLowerCase() === "a"){
					console.log(c, c.className.indexOf("post_link"), (c.href in window.BMPlayer));
					if(!(c.href in window.BMPlayer) && 
						c.className.indexOf("post_link") >= 0){
						showPlayer(c.href);
						return;
					}
				}
			}
		}
	}
	alert("No songs to play");
}());