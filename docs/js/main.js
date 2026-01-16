const API = 'https://yi-liya.github.io/web/api/time'; // 后面换成你自己的
document.getElementById('btn').addEventListener('click', async () => {
  try {
    const r = await fetch(API);
    const j = await r.json();
    document.getElementById('result').textContent = '服务器时间：' + j.now;
  } catch (e) {
    document.getElementById('result').textContent = '请求失败：' + e;
  }
});