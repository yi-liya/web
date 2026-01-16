document.getElementById('btn').addEventListener('click', async () => {
  try {
    const r = await fetch('http://localhost:5000/api/time');
    const j = await r.json();
    document.getElementById('result').textContent = '服务器时间：' + j.now;
  } catch (e) {
    document.getElementById('result').textContent = '请求失败：' + e;
  }
});