const { app, BrowserWindow, ipcMain } = require('electron')
const path = require('path')
const { spawn } = require('child_process')

const WORKERS = path.join(__dirname, 'workers')
const MODULES = {
  generate: 'email_generator',
  clean: 'email_cleaner',
  seek: 'seeker',
}
let win = null

function createWindow() {
  win = new BrowserWindow({
    width: 1180, height: 760, frame: false,
    webPreferences: { preload: path.join(__dirname, 'preload.js'), contextIsolation: true }
  })
  win.loadFile('app/renderer/index.html')
}

ipcMain.handle('run', async (_e, payload) => {
  const mod = MODULES[payload && payload.module]
  if (!mod) return { ok: false, error: 'unknown module' }
  const py = spawn('python', [path.join(WORKERS, mod + '.py'), ...(payload.args || [])])
  py.stdout.on('data', d => win && win.webContents.send('log', String(d)))
  py.stderr.on('data', d => win && win.webContents.send('log', String(d)))
  return new Promise(resolve => py.on('close', code => resolve({ ok: code === 0, code })))
})

app.whenReady().then(createWindow)
app.on('window-all-closed', () => app.quit())
