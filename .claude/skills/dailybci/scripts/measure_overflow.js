const { chromium } = require(process.env.PW);
const fs=require('fs'), path=require('path');
(async()=>{
  const dir=process.argv[2];
  const b=await chromium.launch(); const p=await b.newPage({viewport:{width:2160,height:2880}});
  for (const f of fs.readdirSync(dir).filter(x=>x.endsWith('.html')).sort()){
    await p.goto('file://'+path.join(dir,f)); await p.waitForTimeout(150);
    const r=await p.evaluate(()=>{
      const card=document.querySelector('.card'), foot=document.querySelector('.footer');
      let maxb=0; for(const el of card.querySelectorAll('.annot,.para,.lead,.ref,.figwrap,.sigblock,.read-body,.subtitle,.conceptwrap')){maxb=Math.max(maxb,el.getBoundingClientRect().bottom);}
      return {gap: foot.getBoundingClientRect().top-maxb};
    });
    console.log(f, Math.round(r.gap));
  }
  await b.close();
})();
