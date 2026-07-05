const log = (line) => {
  const el = document.getElementById('log')
  if (el) el.textContent += line
}
if (window.api && window.api.onLog) window.api.onLog(log)

document.querySelectorAll('nav button').forEach(b => {
  b.addEventListener('click', () => {
    document.querySelectorAll('nav button').forEach(x => x.classList.remove('on'))
    b.classList.add('on')
  })
})
