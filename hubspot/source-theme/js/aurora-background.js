/**
 * Interactive Parallax Overlay
 * Adds mouse-reactive wave layers on top of CSS body background
 * Creates depth and interactivity
 */
(function(){
  'use strict';

  var waves = [
    {y:0,   c:'#063d1e', o:0.9, b:25, s:0.08, h:120, sk:-3},
    {y:15,  c:'#074a24', o:0.85,b:20, s:0.12, h:100, sk:2},
    {y:35,  c:'#053518', o:0.88,b:28, s:0.06, h:110, sk:-2},
    {y:55,  c:'#064020', o:0.82,b:22, s:0.1,  h:105, sk:3},
    {y:75,  c:'#053d1c', o:0.85,b:25, s:0.09, h:115, sk:-2.5},
    {y:5,   c:'#0a6b35', o:0.55,b:15, s:0.25, h:80,  sk:2.5},
    {y:25,  c:'#0d7a3c', o:0.5, b:12, s:0.3,  h:75,  sk:-3},
    {y:45,  c:'#096330', o:0.55,b:18, s:0.22, h:85,  sk:1.5},
    {y:65,  c:'#0b7238', o:0.45,b:14, s:0.28, h:70,  sk:-2},
    {y:85,  c:'#0a6b35', o:0.5, b:16, s:0.25, h:80,  sk:3},
    {y:8,   c:'#0f8d42', o:0.3, b:8,  s:0.45, h:60,  sk:-2},
    {y:30,  c:'#109945', o:0.25,b:6,  s:0.5,  h:50,  sk:2.5},
    {y:50,  c:'#0d8040', o:0.3, b:10, s:0.42, h:55,  sk:-1.5},
    {y:70,  c:'#0f8d42', o:0.25,b:7,  s:0.48, h:50,  sk:2},
    {y:90,  c:'#109945', o:0.28,b:9,  s:0.44, h:55,  sk:-2.5}
  ];

  var els=[], wrap=null, mouseX=0.5, mouseY=0.5, tMX=0.5, tMY=0.5, sY=0, pH=1;

  function init(){
    var old=document.getElementById('parallax-blob-wrapper');
    if(old) old.remove();
    old=document.getElementById('organic-blob-bg');
    if(old) old.remove();

    pH=Math.max(document.body.scrollHeight,document.documentElement.scrollHeight);
    wrap=document.createElement('div');
    wrap.id='parallax-blob-wrapper';
    wrap.style.cssText='position:absolute;top:0;left:0;width:100%;height:'+pH+'px;overflow:hidden;pointer-events:none;z-index:0;';

    waves.forEach(function(w,i){
      var el=document.createElement('div');
      var tp=(w.y/100)*pH;
      var br='50% 50% 50% 50% / '+(30+(i%5)*8)+'% '+(35+(i%4)*7)+'% '+(30+(i%3)*10)+'% '+(35+(i%6)*6)+'%';
      el.style.cssText='position:absolute;top:'+tp+'px;left:-20vw;width:140vw;height:'+w.h+'vh;background:'+w.c+';border-radius:'+br+';filter:blur('+w.b+'px);opacity:'+w.o+';transform:skewY('+w.sk+'deg);will-change:transform;';
      wrap.appendChild(el);
      els.push({el:el,spd:w.s,sk:w.sk});
    });

    document.body.insertBefore(wrap,document.body.firstChild);
    window.addEventListener('scroll',onS,{passive:true});
    window.addEventListener('mousemove',onM,{passive:true});
    window.addEventListener('resize',onR,{passive:true});
    requestAnimationFrame(tick);
    console.log('[ParallaxWaves] Initialized '+els.length+' waves');
  }

  function onS(){sY=window.pageYOffset||document.documentElement.scrollTop;}
  function onM(e){tMX=e.clientX/window.innerWidth;tMY=e.clientY/window.innerHeight;}
  function onR(){
    var np=Math.max(document.body.scrollHeight,document.documentElement.scrollHeight);
    if(Math.abs(np-pH)>200){pH=np;if(wrap)wrap.style.height=pH+'px';}
  }

  function tick(){
    mouseX+=(tMX-mouseX)*0.03;
    mouseY+=(tMY-mouseY)*0.03;
    var mx=(mouseX-0.5)*2;
    var my=(mouseY-0.5)*2;
    for(var i=0;i<els.length;i++){
      var b=els[i];
      var so=sY*(1-b.spd);
      var msx=mx*b.spd*30;
      b.el.style.transform='skewY('+b.sk+'deg) translateY(-'+so+'px) translateX('+msx+'px)';
    }
    requestAnimationFrame(tick);
  }

  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded',function(){setTimeout(init,200);});
  } else {
    setTimeout(init,200);
  }
})();
