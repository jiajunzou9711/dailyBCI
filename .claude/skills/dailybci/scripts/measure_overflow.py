"""量图卡正文是否溢出：不截图，只把 build 脚本的每张卡输出为 HTML，再用 Playwright 量「正文最低点到页脚顶边」的距离。
用法：python3 measure_overflow.py <build_xxx_cards.py> [脚本参数 ...]
输出每张卡的余量（2× 像素）：负数=溢出，约 97 ≈ 一行图卡注文。依赖 npx 缓存里的 playwright（PW 路径按需改）。"""
import sys, os, glob, runpy, subprocess, tempfile
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import card_generator
D=tempfile.mkdtemp(prefix="measure_")
def fake(self, html_str, output_path):
    open(os.path.join(D, os.path.basename(output_path).replace('.png','.html')),'w').write(html_str); return output_path
card_generator.CardGenerator._render=fake
sys.argv=sys.argv[1:]
runpy.run_path(sys.argv[0], run_name="__main__")
pw=os.environ.get("PW") or next(iter(sorted(glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/playwright")),reverse=True)),"playwright")
subprocess.run(["node", os.path.join(HERE,"measure_overflow.js"), D], env={**os.environ,"PW":pw})
